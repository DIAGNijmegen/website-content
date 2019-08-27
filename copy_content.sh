# #!/usr/bin/env bash

# Break build on error
set -e

# List of websites to build
declare -a websites=("website-diag" "website-ai-for-health" "website-pathology" "website-neuro" "website-rse" "website-retina" "website-bodyct" "website-aiimnijmegen" "website-rtc")

# Distribute the content pages
python parse_content.py

for website in "${websites[@]}"
do
  echo "Copying content for $website"

  # Copy default base pages
  cp -r --no-clobber content/pages/defaults/. $website/content/pages/
  # Copy images
  cp -r --no-clobber imgoptim/optimized_images/. $website/content/images

done
