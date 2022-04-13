#!/bin/bash:

cd /home/user/website-content
echo "Going to initialize website: ${@}"
echo 

# Copy bib files and parse, if output files do not exist.
if [ ! -f /home/user/website-content/content/bibitems.json ]; then
    cp docker/bibfiles/diag.bib content/diag.bib
    cp docker/bibfiles/fullstrings.bib content/fullstrings.bib
    python ./bibliography/bibparser.py
fi

# Execute copy content script.
LOCAL=1 WEBSITE=website-"${@}" sh ./copy_content.sh

# Run pelican.
cd /home/user/website-content/website-"${@}"
pelican --autoreload --listen --bind 0.0.0.0
