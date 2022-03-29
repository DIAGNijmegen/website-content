# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE

# Copy default base pages
cp --no-clobber content/pages/defaults/404.md $WEBSITE/content/pages/404.md
cp --no-clobber content/pages/defaults/colofon.md $WEBSITE/content/pages/colofon.md
cp --no-clobber content/pages/defaults/home.md $WEBSITE/content/pages/home.md

# Copy bib files
cp content/bibitems.json $WEBSITE/content/bibitems.json
cp content/authorkeys.json $WEBSITE/content/authorkeys.json
cp content/groupkeys.json $WEBSITE/content/groupkeys.json

# Copy images when deploying locally (for development)
if [ "$LOCAL" = "1" ]; then
  rm -rf $WEBSITE/output/
  mkdir $WEBSITE/output
  cp -r --no-clobber assets/images/. $WEBSITE/output/images
  cp -r --no-clobber content/images/. $WEBSITE/output/images
fi
