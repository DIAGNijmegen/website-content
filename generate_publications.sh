# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

if [[ $GENERATE_PUB != '1' ]]; then
  echo "Skipping generation of publication pages for $WEBSITE."
else
  echo "Generating publications for $WEBSITE"

  # Copy bib generator script
  cp -r plugins/bibtex $WEBSITE/plugins
  cp plugins/bib_writer.py $WEBSITE/plugins/bib_writer.py

  # Download bib file for publications
  curl -o $WEBSITE/content/diag.bib -u ${BIB_TOKEN} ${BIB_URL} >/dev/null 2>&1

  # Run the bib plugin
  cd $WEBSITE
  python plugins/bib_writer.py
  cd ..
fi
