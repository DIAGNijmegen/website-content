FROM ubuntu:20.04

# Install python3.8
RUN : \
    && apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository -y ppa:deadsnakes \
    && apt-get install -y --no-install-recommends python3.8-venv \
    && apt-get install -y --no-install-recommends git \
    && apt-get install libpython3.8-dev -y \
    && apt-get clean \
    && :
    
# Add env to PATH
RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH

# Website specific requirements
RUN apt-get install nodejs -y
RUN apt-get install curl -y

EXPOSE 8000

# Copy the entry point script and set the entry point.
COPY run.sh /root
ENTRYPOINT ["/bin/bash", "/root/run.sh"]
