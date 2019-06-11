const glob = require('glob');
const fs = require('fs');
const dirname = require('path').dirname;
const md5 = require('md5');
const mkdirp = require('mkdirp');
const { promisify } = require('util');
const sharp = require('sharp');
const imagemin = require('imagemin');
const imageminMozjpeg = require('imagemin-mozjpeg');
const imageminSvgo = require('imagemin-svgo');
const imageminWebp = require('imagemin-webp');
const imageminPngquant = require('imagemin-pngquant');

const writeFile = promisify(fs.writeFile);
const readFile = promisify(fs.readFile);

const sourceBasePath = '../content/images';
const outputPath = "./optimized_images";
const outputSizes = [160, 320, 480, 768, 1024];

/**
 * Resize an image using sharp (async).
 * @param  {String} path   Original image path
 * @param  {String} target Target path
 * @param  {array} sizes  Target widths (in pixels)
 * @return {array} List of target paths.
 */
async function resizeImage(path, target, sizes) {
  const image = sharp(path);
  const metadata = await image.metadata();

  // Save the original file to a <filename>-full.<ext>
  const baseFile = new Promise(resolve => {
    const originalFileTarget = target.replace(/(\.[\w\d_-]+)$/i, '-full$1');
    return fs.copyFile(path, originalFileTarget, () => resolve(originalFileTarget));
  });

  const availableSizes = outputSizes.filter(s => s <= metadata.width);
  const resizedFiles = availableSizes.map(async size => {
    let resizedTarget;
    if(size == Math.max(...availableSizes)) {
      // Save the highest resolution image to the original filename
      // This makes sure that an optimized image is always available, even
      // when the utility functions in pelican are not used.
      resizedTarget = target;
    } else {
      resizedTarget = target.replace(/(\.[\w\d_-]+)$/i, `-${size}$1`);
    }

    await image
      .resize({width: size})
      .toFile(resizedTarget);

    return resizedTarget;
  });

  return Promise.all([baseFile, ...resizedFiles]);
}

/**
 * Compress an image using imagemin
 * @param  {array} paths     List of images to compress
 * @param  {string} targetDir Output folder
 * @return {Promise}
 */
function compressImages(paths, targetDir) {

  return imagemin(paths, targetDir, {
    plugins: [
      imageminPngquant(),
      imageminMozjpeg({quality: 70}),
      // imageminWebp({quality: 70}),
      // imageminSvgo({plugins: [{removeViewBox: false}]}),
    ]
  });
}

// Main program
(async () => {

  const imgCache = fs.existsSync('image-cache.json') ? JSON.parse(fs.readFileSync('image-cache.json', 'utf8')) : {};
  const imgPaths = glob.sync(`${sourceBasePath}/**/*.+(png|jpg|jpeg|JPG|PNG)`);

  // Get MD5 hash of all images
  const imgHashes = await Promise.all(imgPaths.map(async path => {
    const buffer = await readFile(path);
    const hash = md5(buffer);
    const target = path.replace(sourceBasePath, outputPath);
    return {path, hash, target};
  }));

  // Create intermediate dirs if they do not exist
  await Promise.all(imgHashes.map(async ({target}) => await mkdirp(dirname(target))));

  // Filter images that have not been changed
  const changedImages = imgHashes
    .filter(({path, hash}) => !(path in imgCache) || imgCache[path] != hash);

  // Resize images
  await Promise.all(changedImages.map(async ({path, target, hash}) => {
    try {
      console.log(`Optimizing ${path}.`);
      // Create resized versions of the image
      const resizedImages = await resizeImage(path, target, outputSizes);

      // Compress resized images
      await compressImages(resizedImages, dirname(resizedImages[0]));

      // Update the cache
      imgCache[path] = hash;
    } catch(err) {
      console.error(err);
    }
  }));

  // Save new hash file
  await writeFile('image-cache.json', JSON.stringify(imgCache), 'utf8');

  console.log("Completed");
})();
