#!/bin/bash:

# Cloning website repo
echo "Cloning website repository."
echo
rm -rf /home/user/source/website-content
git clone https://github.com/DIAGNijmegen/website-content.git /home/user/source/website-content
chown --recursive user:user /home/user/source/website-content
chmod 777 /home/user/source/website-content/copy_content.sh

# Check if extra arguments were given and execute it as a command.
if [ -z "$1" ]
    then
        # Print the command for logging.
        echo "No extra arguments given, running jupyter and sshd"
        echo

        # Start the SSH daemon and a Jupyter notebook.
        /usr/sbin/sshd
        cd /home/user && sudo  --set-home --preserve-env --user=user  /bin/bash -c '/usr/local/bin/jupyter lab --ip=0.0.0.0 --port=8888 --NotebookApp.token='

    else
        # Print the command for logging.
        echo "Going to initialize website: ${@}"
        echo
        
        cd /home/user/source/website-content
        WEBSITE=website-"${@}" sh ./copy_content.sh
        cd /home/user

        cd /home/user/source/website-content/website-"${@}" && pelican --autoreload --listen &>/dev/null &

        # Start the SSH daemon and a Jupyter notebook.
        /usr/sbin/sshd
        cd /home/user && sudo  --set-home --preserve-env --user=user  /bin/bash -c '/usr/local/bin/jupyter lab --ip=0.0.0.0 --port=8888 --NotebookApp.token='
fi
