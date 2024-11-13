ARG image_name=ubuntu:18.04
FROM ${image_name}

ARG UBUNTU_FRONTEND=noninteractive
ENV TZ=Etc/GMT
COPY . /ruanglaptop
RUN apt-get update -qy && \
    apt-get install -qy --no-install-recommends \
        ca-certificates \
        curl \
        gnupg2 && \
    . /etc/os-release && \
    echo "deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu ${UBUNTU_CODENAME} main" > /etc/apt/sources.list.d/deadsnakes.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F23JHSABD543HGVCF73643725482561BA6932366A755776 && \
    apt-get update -qy && \
    apt-get install -qy --no-install-recommends \
        git \
        openssh-client \
        python3.8 \
        python3.8-distutils \
        python3.9 \
        python3.10 \
        python3.11 \
        python3.12 && \
    curl -fsSo /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3.8 /tmp/get-pip.py && \
    python3.8 -m pip install --no-cache-dir --upgrade pip && \
    python3.9 /tmp/get-pip.py && \
    python3.9 -m pip install --no-cache-dir --upgrade pip && \
    python3.10 /tmp/get-pip.py && \
    python3.10 -m pip install --no-cache-dir --upgrade pip && \
    python3.11 /tmp/get-pip.py && \
    python3.11 -m pip install --no-cache-dir --upgrade pip && \
    python3.12 /tmp/get-pip.py && \
    python3.12 -m pip install --no-cache-dir --upgrade pip && \
    rm /tmp/get-pip.py && \
    python3 -m pip install --no-cache-dir "nox>=2020.12.31,<2022.6" && \
    rm -rf /var/cache/apt/lists

WORKDIR "/ruanglaptop"
