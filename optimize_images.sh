# #!/usr/bin/env bash

# Break build on error
set -e

# Check if we are up to date with the remote master branch.
# If not we skip optimization to prevent conflicts and save time.
currentcommit="$(git rev-parse HEAD)"
git checkout master # Travis starts on a detached head
if [ $currentcommit != "$(git rev-parse HEAD)" ]; then
  echo "Not on latest commit, skipping optimization."
  exit 0;
fi

# Optimize the images before building the website`
cd imgoptim
echo "Starting image optimization script"
node optimize.js

# Set user to the webteam deploy bot
git config --global user.email "webteamdiag@gmail.com"
git config --global user.name "DIAGWebTeam"

# Get latest version, there could be a new commit
git checkout master 
# Check if we are still on the latest commit
if [ $currentcommit != "$(git rev-parse HEAD)" ]; then
  echo "Not on latest commit, skipping optimization."
  exit 0;
fi

# Add changed files
git add --all ../assets/images
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

# Go back to starting dir
cd ..

# Copy non-optimized images (non-overwrite)
# This makes sure that content is always available, even if it is not processed by the optimizer.
cp -r --no-clobber content/images/. assets/images