# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

function travis-branch-commit() {

    if ! git checkout "$TRAVIS_BRANCH"; then
        err "failed to checkout $TRAVIS_BRANCH"
        return 1
    fi

    if ! git add --all .; then
        err "failed to add modified files to git index"
        return 1
    fi
    # make Travis CI skip this build
    if ! git commit -m "Travis CI update [ci skip]"; then
        err "failed to commit updates"
        return 1
    fi
    # add to your .travis.yml: `branches\n  except:\n  - "/\\+travis\\d+$/"\n`
    local git_tag=SOME_TAG_TRAVIS_WILL_NOT_BUILD+travis$TRAVIS_BUILD_NUMBER
    if ! git tag "$git_tag" -m "Generated tag from Travis CI build $TRAVIS_BUILD_NUMBER"; then
        err "failed to create git tag: $git_tag"
        return 1
    fi
    local remote=origin
    if [[ $GITHUB_TOKEN ]]; then
        remote=https://$GITHUB_TOKEN@github.com/$TRAVIS_REPO_SLUG
    fi
    if [[ $TRAVIS_BRANCH != master ]]; then
        msg "not pushing updates to branch $TRAVIS_BRANCH"
        return 0
    fi
    if ! git push --quiet --follow-tags "$remote" "$TRAVIS_BRANCH" > /dev/null 2>&1; then
        err "failed to push git changes"
        return 1
    fi
}

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
git commit --message "Adding optimized images to repository. [ci skip]"
if [[ $TRAVIS_BRANCH != master ]]; then
  msg "not pushing updates to branch $TRAVIS_BRANCH"
else
  git push "https://${GH_TOKEN}@github.com/DIAGNijmegen/website-content.git" "master" > /dev/null 2>&1
fi

# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
# if git diff --quiet; then
#     echo "No changes to the output on this push."
# else


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
  cp -r --no-clobber content/images $website/content
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
