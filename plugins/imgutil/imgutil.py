import os

from pelican import signals

SIZE_TO_WIDTH_MAPPING = {
    'tiny': '160',
    'small': '320',
    'medium': '480',
    'large': '768',
    'full': 'full',
}

# Path where the optimized images are stored in the repo
optim_path = os.path.join(os.getcwd(), '../imgoptim/optimized_images')

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
    
    for name, size in SIZE_TO_WIDTH_MAPPING.items():
        # Don't make the full size part of the srcset to save bandwidth
        if name == 'full':
            continue

        resized_path  = f"{parts[0]}-{size}{parts[1]}"
        
        if os.path.isfile(os.path.join(optim_path, resized_path.replace('images/', ''))):
            srcset.append(f'{base_url}/{resized_path} {size}w')
        elif name == 'large':
            # If there is no 'large' version, we use the 'full' version of the image instead for this size.
            # This makes sure the browser will load the highest resolution iamge for large viewports.
            # Ideally we would inject the correct width here, 768 is a best-effor guess.
            srcset.append(f'{base_url}/{parts[0]}-full{parts[1]} 768w')

    return ', '.join(srcset)


def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'resize_image': get_resized_image, 'srcset_image': srcset_image})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
