# #!/usr/bin/env bash

curl -o $WEBSITE/content/diag.bib -u ${BIB_TOKEN} ${BIB_URL} >/dev/null 2>&1

python ./bibliography/bibparser.py
