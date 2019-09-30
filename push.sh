# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

# Optimize the images before building the website`
git config --global user.email "webteamdiag@gmail.com"
git config --global user.name "DIAGWebTeam"

# Add changed files
git checkout feature/publications  
git pull feature/publications

gitdiff='git diff --quiet HEAD^ ./content/diag.bib'
if ! $gitdiff; then
  git add --all ./website-*/content/pages/publications/
  git add --all ./website-*/dict_pubs.json
  echo "Files changed, commiting new publications."
  git commit --message "Adding publications to repository." -- .
  git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "feature/publications"
else
  echo "Nothing new to commit, skipping push."
fi

