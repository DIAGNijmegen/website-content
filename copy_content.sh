# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py

for website in $WEBSITES
do
  echo "Copying content for $website"

  # Copy default base pages
  cp -r --no-clobber content/pages/defaults/. $website/content/pages/
  # Copy images
  cp -r --no-clobber imgoptim/optimized_images/. $website/content/images

done
