# #!/usr/bin/env bash

# Break build on error
set -e

# # Check if we are up to date with the remote master branch.
# # If not we skip optimization to prevent conflicts and save time.
# currentcommit="$(git rev-parse HEAD)"
# git checkout master # Travis starts on a detached head
# if [ $currentcommit != "$(git rev-parse HEAD)" ]; then
#   echo "Not on latest commit, skipping optimization."
#   exit 0;
# fi

# Optimize the images before building the website`
cd imgoptim
echo "Starting image optimization script"
node optimize.js


# new github action

# # Add cache file
# git add image-cache.json

# Add all exported iamges
cd ..
# git add --all assets/images

# Copy non-optimized images (non-overwrite) to deploy directory
# This makes sure that content is always available, even if it is not processed by the optimizer.
cp -r --no-clobber ./content/images/. assets/images