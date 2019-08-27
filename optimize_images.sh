# #!/usr/bin/env bash

# Break build on error
set -e

echo $WEBSITES

for website in "${WEBSITES[@]}"
do
  echo "\n"
  echo $website
done

if [[ $TRAVIS_BRANCH != 'master' ]]; then
  echo "Not on travis-master build, skip running image optimzer (value: $TRAVIS_BRANCH)"
else
  # Optimize the images before building the website`
  cd imgoptim
  echo "Starting image optimization script"
  node optimize.js

  git config --global user.email "webteamdiag@gmail.com"
  git config --global user.name "DIAGWebTeam"

  # Add changed files
  git checkout master
  git add --all ./optimized_images
  git add image-cache.json

  # Commit optimized images back to the repo
  gitdiff='git diff-index --quiet HEAD .'
  if ! $gitdiff; then
    echo "Files changed, commiting new images."
    git commit --message "Adding optimized images to repository. [ci skip]" -- .
    git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "master"
  else
    echo "Nothing new to commit, skipping push."
  fi
fi
