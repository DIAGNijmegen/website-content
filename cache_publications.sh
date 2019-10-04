# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

EXCLUDES=(website-ai-for-health website-base)
gitdiff='git diff --quiet HEAD~ ./content/diag.bib'

echo "Content before generation"
ls -a ./website-pathology/content/pages/publications

for WEBSITE in website-p*
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
      #if true || ! $gitdiff; then
        echo "Generating publications for $WEBSITE"
        # Copy bib generator script
        cp -r plugins/bibtex $WEBSITE/plugins
        cp plugins/bib_writer.py $WEBSITE/plugins/bib_writer.py

        # Copy literature
        cp content/diag.bib $WEBSITE/content/diag.bib

        # Run the bib plugin
        cd $WEBSITE
        python plugins/bib_writer.py

        echo "Content after generation"
        ls -a content/pages/publications

        cd ..

#      else
        #echo "Diag bib not changed. Skipping generation of publiction (using current publications files)"
      #fi
    fi
done


# Optimize the images before building the website`
git config --global user.email "webteamdiag@gmail.com"
git config --global user.name "DIAGWebTeam"

## Add changed files
git checkout feature/publications
#git pull origin feature/publications

echo "Content after checkout"
ls -a website-pathology/content/pages/publications

#if ! $gitdiff; then
  echo status before add
  git status -v
  pwd
  git add -v --all ./website-*/content/pages/publications/*
  echo status after add
  git status -v

  git add --all website-pathology/content/pages/publications
  git status --verbose
  #echo cd
  #cd ./website-pathology/content/pages/publications
  #ls
  #echo done cd and ls

  #git add --all ./website-*/content/pages/publications/*
  #git add --all ./website-*/content/dict_pubs.json

  #git status
  #echo "Files changed, commiting new publications."
  #git commit --message "Adding publications to repository." -- .
  #git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "feature/publications"
#else
  #echo "Nothing new to commit, skipping push."
#fi
