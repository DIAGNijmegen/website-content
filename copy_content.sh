# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE

# Copy default base pages
cp --no-clobber content/pages/defaults/404.md $WEBSITE/content/pages/404.md
cp --no-clobber content/pages/defaults/colofon.md $WEBSITE/content/pages/colofon.md
cp --no-clobber content/pages/defaults/home.md $WEBSITE/content/pages/home.md

# copy bib files
cp content/bibitems.json $WEBSITE/content/bibitems.json
cp content/authorkeys.json $WEBSITE/content/authorkeys.json
cp content/groupkeys.json $WEBSITE/content/groupkeys.json