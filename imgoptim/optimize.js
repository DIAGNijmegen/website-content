const glob = require('glob');
const fs = require('fs');
const basename = require('path');
const dirname = require('path').dirname;
const md5 = require('md5');
const mkdirp = require('mkdirp');
const { promisify } = require('util');
const sharp = require('sharp');
const imagemin = require('imagemin');
const imageminMozjpeg = require('imagemin-mozjpeg');
//const imageminSvgo = require('imagemin-svgo');
//const imageminWebp = require('imagemin-webp');
const imageminPngquant = require('imagemin-pngquant');

const writeFile = promisify(fs.writeFile);
const readFile = promisify(fs.readFile);
const removeFile = promisify(fs.unlink);

const sourceBasePath = '../content/images';
const outputPath = "../assets/images";
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
  
  // If the source image is smaller than the smallest output size, copy the original file
  // to the output directory.
  if(availableSizes.length == 0) {
    new Promise(resolve => {
      return fs.copyFile(path, target, () => resolve(target));
    });
  }

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
      imageminMozjpeg({quality: 85}),
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

  // Resize images
  const updatedCache = {}
  let updatedImages = 0
  await Promise.all(imgHashes.map(async ({path, target, hash}) => {
    if (!(path in imgCache) || imgCache[path] != hash) {
      // Only create new images for updated source files
      try {
        console.log(`Optimizing ${path}.`);
        // Create resized versions of the image
        const resizedImages = await resizeImage(path, target, outputSizes);

        // Compress resized images
        await compressImages(resizedImages, dirname(resizedImages[0]));

        updatedImages += 1

      } catch(err) {
        console.error(err);
      }
    }

    // Update the cache
    updatedCache[path] = hash;
  }));

  if(updatedImages > 0) {
    // Save new hash file, only if at least one image was updated
    await writeFile('image-cache.json', JSON.stringify(updatedCache), 'utf8');
  }

  const generatedImages = glob.sync(`${outputPath}/**/*.+(png|jpg|jpeg|JPG|PNG)`);
  // Targets for mapping generated filenames back to the original names
  const replaceRegex = new RegExp(outputSizes.reduce((a, c) => `${a}|-${c}.`, '-full.'), 'g');
  // Remove all images that are not in the cache anymore
  await Promise.all(generatedImages.map(async (path) => {
    const originalPath = path.replace(replaceRegex, '.')
                             .replace(outputPath, sourceBasePath);

    if(!(originalPath in updatedCache)) {
      console.log(`Removing file ${path}`);
      return removeFile(path);
    }
  }));

  console.log("Completed image optimization.");
})();
