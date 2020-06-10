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

    if os.path.isfile(os.path.join(optim_path, resized_path)):
        return resized_path

    return path

def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'resize_image': get_resized_image})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
