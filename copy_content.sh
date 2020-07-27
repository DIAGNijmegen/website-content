# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE

# Copy default base pages
cp -r --no-clobber content/pages/defaults/. $WEBSITE/content/pages/

# copy bib files
cp content/bibitems.json $WEBSITE/content/bibitems.json
cp content/authorkeys.json $WEBSITE/content/authorkeys.json
cp content/groupkeys.json $WEBSITE/content/groupkeys.json