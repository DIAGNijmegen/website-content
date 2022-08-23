#!/bin/bash:

echo "Going to clone website-content repository..."
git clone https://github.com/DIAGNijmegen/website-content.git /home/user/website-content-repository-clone
echo "Done cloning."
echo "Going to checkout at branch: $2"
cd /home/user/website-content-repository-clone
git fetch
git checkout $2

echo "Going to install requirements.txt"
python3 -m pip install --no-cache-dir -r requirements.txt

echo "Going to clone Literature repository..."
rm -r docker/literature_repository
git clone https://github.com/DIAGNijmegen/Literature.git docker/literature_repository
echo "Done cloning."
cp docker/literature_repository/diag.bib content/diag.bib
cp docker/literature_repository/fullstrings.bib content/fullstrings.bib
rm -r docker/literature_repository
python ./bibliography/bibparser.py
echo "Done with bibparser.py" 

# Execute copy content script.
LOCAL=1 WEBSITE=website-"$1" sh ./copy_content.sh

# Run pelican.
cd website-"$1"
pelican --autoreload --listen --bind 0.0.0.0
