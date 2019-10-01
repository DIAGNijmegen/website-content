# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

EXCLUDES=(website-ai-for-health website-base)
gitdiff='git diff --quiet HEAD^ ./content/diag.bib'

for WEBSITE in website-*
do
    GENERATE_PUB=1
    for EXCLUDE in ${EXCLUDES[*]}
    do
        if [ $WEBSITE == $EXCLUDE ]; then
            GENERATE_PUB=0
        fi
    done

    echo $WEBSITE $GENERATE_PUB
    if [[ $GENERATE_PUB != '1' ]]; then
      echo "Skipping generation of publication pages for $WEBSITE."
    else

      # Check if diag bib changed 
      if ! $gitdiff; then

        echo "Generating publications for $WEBSITE"

        # Copy bib generator script
        cp -r plugins/bibtex $WEBSITE/plugins
        cp plugins/bib_writer.py $WEBSITE/plugins/bib_writer.py

        # Copy literature
        cp content/diag.bib $WEBSITE/content/diag.bib

        # Run the bib plugin
        cd $WEBSITE
        python plugins/bib_writer.py
        cd ..

      else
        echo "Diag bib not changed. Skipping generation of publiction (using current publications files)"
      fi
    fi
done

# Optimize the images before building the website`
git config --global user.email "webteamdiag@gmail.com"
git config --global user.name "DIAGWebTeam"

# Add changed files
git checkout feature/publications  
git pull origin feature/publications

gitdiff='git diff --quiet HEAD^ ./content/diag.bib'
if ! $gitdiff; then
  git add --all ./website-*/content/pages/publications
  git add --all ./website-*/content/dict_pubs.json
  echo "Files changed, commiting new publications."
  git commit --message "Adding publications to repository." -- .
  git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "feature/publications"
else
  echo "Nothing new to commit, skipping push."
fi

