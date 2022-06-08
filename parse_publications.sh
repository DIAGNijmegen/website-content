# #!/usr/bin/env bash

set -e

curl -o content/diag.bib \
     -s -f -S \
     -L https://raw.githubusercontent.com/DIAGNijmegen/Literature/main/diag.bib

curl -o content/fullstrings.bib \
     -s -f -S \
     -L https://raw.githubusercontent.com/DIAGNijmegen/Literature/main/fullstrings.bib

python ./bibliography/bibparser.py
