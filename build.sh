# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

if [[ $TRAVIS_BRANCH != 'master' ]]; then
  echo "Not on travis-master build, skip running image optimzer (value: $TRAVIS_BRANCH)"
else
  # Optimize the images before building the website`
  cd imgoptim
  echo "Starting image optimization script"
  node optimize.js

  # Commit optimized images back to the repo
  echo "Commit new images to repository"
  git config --global user.email "webteamdiag@gmail.com"
  git config --global user.name "DIAGWebTeam"

  # Add changed files
  git checkout master
  git add --all ./optimized_images
  git add image-cache.json

  gitdiff='git diff-index --quiet HEAD .'
  if ! $gitdiff; then
    echo "Files changed, commiting new images."
    git commit --message "Adding optimized images to repository. [ci skip]" -- .
    git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "master"
  else
    echo "Nothing new to commit, skipping push."
  fi

  # Go back to main dir
  cd ..
fi

# List of websites to build
declare -a websites=("website-diag" "website-msc-projects" "website-pathology" "website-neuro" "website-rse" "website-retina" "website-bodyct" "website-aiimnijmegen")
declare -a websites_without_bibtex=("website-msc-projects")

# Distribute the content pages
python parse_content.py

for website in "${websites[@]}"
do
  echo "Building $website"

  # Copy default base pages
  cp -r --no-clobber content/pages/defaults/. $website/content/pages/
  # Copy images
  cp -r --no-clobber imgoptim/optimized_images/. $website/content/images
  # Copy bib generator script
  cp -r plugins/bibtex $website/plugins
  cp plugins/bib_writer.py $website/plugins/bib_writer.py

  # Copy literature
  cp content/diag.bib $website/content/diag.bib

  cd $website
  pwd

  if [[ $website != 'website-msc-projects' ]]; then
    # Generate publications
    python plugins/bib_writer.py
  fi

  if [[ $website == 'website-pathology' ]] || [[ $website == 'website-diag' ]]; then
    # Init repo
    echo "Cloning ${website} output repository"
    git clone --depth 1 "https://${GH_PAGES}@github.com/DIAGNijmegen/${website}.git" output
  else
    echo "Website not in deploy pilot, using clean directory."
  fi

  # Build pelican website
  pelican content -s publishconf.py

  # Copy files for github
  cp README.md output/README.md
  cp .nojekyll output/.nojekyll

  # Push to github
  if [[ $website == 'website-pathology' ]]; then
    cp CNAME output/CNAME

    cd output
    git add .
    git status

    gitdiff='git diff-index --quiet HEAD .'
    if ! $gitdiff; then
      echo "Files changed, commiting new images."
      git commit --message "Pushing new version of ${website}" -- .
      git push "https://${GH_PAGES}@github.com/DIAGNijmegen/${website}.git" "master"
    else
      echo "Nothing new to commit, skipping push."
    fi

    cd ..
  else
    echo "Website is not in new pilot deploy"
  fi

  # Go back to root directory
  cd ..
done
