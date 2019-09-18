# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

if [[ $GENERATE_PUB != '1' ]]; then
  echo "Skipping generation of publication pages for $WEBSITE."
else

  gitdiff='git diff-index --quiet HEAD ./content/diag.bib'
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
    
    git config --global user.email "webteamdiag@gmail.com"
    git config --global user.name "DIAGWebTeam"

    # Add changed files
    git checkout feature/publications 
    git add --all ./content/pages/publications

    # Commit optimized images back to the repo
    echo "Publications changed, commiting publications."
    git commit --message "Adding publications to repository. [ci skip]" -- .
    git push "https://${GH_PAGES}@github.com/DIAGNijmegen/website-content.git" "feature/publications"
  else
   echo "Diag bib not changed. Skipping generation of publiction (using current publications files)"
  fi
  
  cd ..
fi
