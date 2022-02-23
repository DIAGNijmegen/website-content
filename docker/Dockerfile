# This dockerfile configures a docker image for building websites of DIAG
FROM ubuntu:20.04

# Website specific requirements
COPY requirements.txt ./

# Ignore interactive calls during apt-get installs below
ARG DEBIAN_FRONTEND=noninteractive

# === Install libs ===
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
        man \
        openssh-server \
        ca-certificates apt-transport-https \
        sudo \
        git subversion \
        nano vim \
        tmux screen \
        htop \
        g++ ninja-build \
        rsync \
        pv \
        curl wget \
        bzip2 zip unzip \
        dcmtk libboost-all-dev \
        libgomp1 \
        libjpeg-turbo8 \
        libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
        libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev gcovr libffi-dev uuid-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /var/run/sshd && \
    cat /etc/sudoers | grep -v secure_path > /tmp/sudoers && mv /tmp/sudoers /etc/sudoers

RUN env | grep '^PATH=\|^LD_LIBRARY_PATH=\|^LANG=\|^LC_ALL=\|^CUDA_ROOT=' > /etc/environment

# === Setup user ===
RUN useradd -ms /bin/bash user && \
    (echo user ; echo user) | passwd user && \
    gpasswd -a user ssh && \
    gpasswd -a user sudo

# === Install python with up-to-date pip ===
ENV PYTHON_VERSION="3.9.10"
RUN cd /tmp && \
    wget "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz" && \
    tar xfv Python*.xz && \
    cd Python-3*/ && \
    ./configure --enable-shared LDFLAGS="-fprofile-arcs" && \
    make altinstall && \
    cd ~ && \
    rm -rf /tmp/Python-3* && \
    ldconfig

# Required to install pip3
RUN sudo apt-get update
RUN sudo apt-get install -y python3-pip

# Copy custom bashrc to docker image
COPY .bashrc /home/user/.bashrc

RUN pip3 install --upgrade pip pip-tools wheel setuptools && \
    printf '#!/bin/bash\necho "Please use pip3 instead of pip to install packages for python3"' > /usr/local/bin/pip && \
    chmod +x /usr/local/bin/pip && \
    rm -rf ~/.cache/pip

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install nodejs -y
RUN apt-get install curl -y

# https://stackoverflow.com/questions/55258124/docker-npm-not-found
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs
RUN curl -qL https://www.npmjs.com/install.sh | sh

# Prioritize python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN pip3 install jupyterlab

# Install website  port.
EXPOSE 8000
EXPOSE 8888
EXPOSE 22

# Copy the entry point script and set the entry point.
COPY run.sh /root
ENTRYPOINT ["/bin/bash", "/root/run.sh"]
