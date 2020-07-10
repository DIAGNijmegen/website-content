# #!/usr/bin/env bash

curl -H 'Authorization: token ${GH_BIB_TOKEN}' \
    -o content/diag.bib \
    -s \
    -L https://raw.githubusercontent.com/DIAGNijmegen/diag-literature/master/diag.bib

curl -H 'Authorization: token ${GH_BIB_TOKEN}' \
    -o content/fullstrings.bib \
    -s \
    -L https://raw.githubusercontent.com/DIAGNijmegen/diag-literature/master/fullstrings.bib

python ./bibliography/bibparser.py
