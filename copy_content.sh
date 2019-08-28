# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE

# Copy default base pages
cp -r --no-clobber content/pages/defaults/. $WEBSITE/content/pages/
# Copy images
cp -r --no-clobber imgoptim/optimized_images/. $WEBSITE/content/images
