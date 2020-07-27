# #!/usr/bin/env bash

# Break build on error
set -e

# Distribute the content pages
python parse_content.py $WEBSITE

# Copy default base pages
cp -r --no-clobber content/pages/defaults/. $WEBSITE/content/pages/

# Copy images
if [[ -z "$SKIP_IMG_COPY" ]]; then
    echo "Start copying images"
    
    cp -r --no-clobber assets/images/. $WEBSITE/content/images

    # Copy non-optimized images (non-overwrite)
    # This makes sure that content is always available, even if it is not processed by the optimizer.
    # TODO: This can be removed if all websites use the CDN.
    cp -r --no-clobber content/images/. $WEBSITE/content/images
else
    echo "Skipping copying images for this build."
fi

# copy bib files
cp content/bibitems.json $WEBSITE/content/bibitems.json
cp content/authorkeys.json $WEBSITE/content/authorkeys.json
cp content/groupkeys.json $WEBSITE/content/groupkeys.json