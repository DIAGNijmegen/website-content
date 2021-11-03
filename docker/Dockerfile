# This dockerfile configures a base docker image for the computational pathology group.
#
FROM doduo1.umcn.nl/uokbaseimage/diag:tf2.5-pt1.9-v1

COPY .bashrc /home/user/.bashrc

COPY requirements.txt ./

RUN sudo apt-get update -y
RUN sudo apt-get upgrade -y
RUN sudo apt-get install nodejs -y
RUN sudo curl -qL https://www.npmjs.com/install.sh | sh

# Prioritize python3
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10

RUN pip3 install --no-cache-dir -r requirements.txt

# Install website  port.
#
EXPOSE 8000

# Copy the entry point script and set the entry point.
#
COPY run.sh /root
ENTRYPOINT ["/bin/bash", "/root/run.sh"]
