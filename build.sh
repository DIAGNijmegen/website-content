# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -ev

# Optimize the images before building the website`
cd imgoptim
echo "Starting image optimization script"
node optimize.js

# Commit optimized images back to the repo
echo "Commit new images to repository"
git config --global user.email "webteamdiag@gmail.com"
git config --global user.name "DIAGWebTeam"

git checkout master
git add --all ./optimized_images
git commit --message "Adding optimized images to repository. [ci skip]" -- .
if [[ $TRAVIS_BRANCH != 'master' ]]; then
  echo "not pushing updates to branch $TRAVIS_BRANCH"
else
  echo "Pushing changes back to repository"
  git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "master"
fi

# Go back to main dir
cd ..

# List of websites to build
declare -a websites=("website-pathology" "website-rse" "website-retina")

# Distribute the content pages
python parse_content.py

for website in "${websites[@]}"
do
  echo "Building $website"

  # Copy default base pages
  cp -r content/pages/defaults/. $website/content/pages/
  # Copy images
  cp -r --no-clobber imgoptim/optimized_images/. $website/content/images
  # Copy bib generator script
  cp -r plugins/bibtex $website/plugins
  cp plugins/bib_writer.py $website/plugins/bib_writer.py

  # Copy literature
  cp content/diag.bib $website/content/diag.bib

  cd $website
  pwd

  # Generate publications
  python plugins/bib_writer.py

  # Build pelican website
  pelican content -s publishconf.py

  # Copy files for github
  #cp CNAME output/CNAME
  cp README.md output/README.md
  # Go back to root directory
  cd ..
done
