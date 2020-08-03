import os

from pelican import signals

SIZE_TO_WIDTH_MAPPING = {
    'tiny': '160',
    'small': '320',
    'medium': '480',
    'large': '768',
    'full': 'full',
}
SIZES = ['160', '320', '480', '768']

# Path where the optimized images are stored in the repo
optim_path = os.path.join(os.getcwd(), '../assets/images')

def get_resized_image(path, size):

    if size not in SIZE_TO_WIDTH_MAPPING:
        return path

    parts = os.path.splitext(path)
    resized_path  = f"{parts[0]}-{SIZE_TO_WIDTH_MAPPING[size]}{parts[1]}"

    # Check if the image is present in the optim directory.
    # The `resized_path` still points to 'images' becase this is where images
    # are eventually deployed.
    if os.path.isfile(os.path.join(optim_path, resized_path.replace('images/', ''))):
        return resized_path

    return path

def srcset_image(path, base_url):

    srcset = []

    # Split image path in extension and path (to inject img size)
    parts = os.path.splitext(path)
    
    # loop through sizes from low to high
    for size in SIZES:
        resized_path  = f"{parts[0]}-{size}{parts[1]}"
        
        if os.path.isfile(os.path.join(optim_path, resized_path.replace('images/', ''))):
            srcset.append(f'{base_url}/{resized_path} {size}w')
        # else:
        #     # There is no version of this image at this size, and by definition
        #     # none of a higher size (given the order of the loop).
        #     # To make sure the browser can always load the highest resolution image,
        #     # we set the 'large' version to this size.
        #     # The width is not completely correct, but makes sure the browser loads this image
        #     # if a high-res version is required.
        #     srcset.append(f'{base_url}/{parts[0]}-full{parts[1]} {2*int(size)}w')

        #     # No higher-res images available
        #     break

    if len(srcset) == 0:
        # If no images were found with a specific size, we add the original image as a fallback
        srcset.append(f'{base_url}/{path} 160w')

    return ', '.join(srcset)


def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'resize_image': get_resized_image, 'srcset_image': srcset_image})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
