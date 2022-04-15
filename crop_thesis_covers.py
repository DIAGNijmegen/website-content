import pathlib
import imageio.v3 as iio

target_aspect_ratio = 0.71
imgdir = pathlib.Path("./content/images/theses")

for imgfile in imgdir.glob("*.png"):
    # Read image and compute current aspect ratio
    image = iio.imread(imgfile)
    aspect_ratio = image.shape[1] / image.shape[0]
    shape = image.shape

    # Crop image to match target aspect ratio
    if aspect_ratio > target_aspect_ratio:
        new_width = round(target_aspect_ratio * image.shape[0])
        if image.shape[1] - new_width > 1:  # ignore 1 pixel differences
            offset = (image.shape[1] - new_width) // 2
            image = image[:, offset : offset + new_width]
    else:
        new_height = round(image.shape[1] / target_aspect_ratio)
        if image.shape[0] - new_height > 1:
            offset = (image.shape[0] - new_height) // 2
            image = image[offset : offset + new_height, :]

    # If the image size has changed, overwrite image file
    if image.shape != shape:
        print(f"Resized {imgfile.relative_to(imgdir)} from {shape} to {image.shape}")
        iio.imwrite(imgfile, image)
