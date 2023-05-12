# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE
# Copy default base pages
cp --no-clobber content/pages/defaults/404.md $WEBSITE/content/pages/404.md
cp --no-clobber content/pages/defaults/colofon.md $WEBSITE/content/pages/colofon.md
cp --no-clobber content/pages/defaults/home.md $WEBSITE/content/pages/home.md

if [ "$WEBSITE" = "website-cara-lab" ]; then
  cp content/bibitems_cara.json $WEBSITE/content/bibitems_cara.json
  cp content/authorkeys_cara.json $WEBSITE/content/authorkeys_cara.json
  cp content/groupkeys_cara.json $WEBSITE/content/groupkeys_cara.json
else
  cp content/bibitems_diag.json $WEBSITE/content/bibitems_diag.json
  cp content/authorkeys_diag.json $WEBSITE/content/authorkeys_diag.json
  cp content/groupkeys_diag.json $WEBSITE/content/groupkeys_diag.json
fi

# Copy images when deploying locally (for development)
# Do not overwrite existing images to save time 
if [ "$LOCAL" = "1" ]; then
  if [ -d $WEBSITE/output/images ]; then
    mv $WEBSITE/output/images $WEBSITE/temp_dir
    rm -rf $WEBSITE/output/
    mkdir $WEBSITE/output
    mv $WEBSITE/temp_dir $WEBSITE/output/images
    rm -rf $WEBSITE/temp_dir
  fi
  cp -r --no-clobber assets/images/. $WEBSITE/output/images
  cp -r --no-clobber content/images/. $WEBSITE/output/images
fi
