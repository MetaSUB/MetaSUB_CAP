FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y locales git python3-dev python3-pip libyaml-dev \
    && pip3 install --upgrade pip \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && useradd -ms /bin/bash metasub

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# MetaSUB_CAP Dependencies
RUN mkdir /opt/metasub/ \
    && cd /opt/metasub/ \
    && git clone https://github.com/dcdanko/DataSuper.git \
    && cd DataSuper \
    && python3 setup.py develop \
    && cd .. \
    && git clone https://github.com/dcdanko/PackageMega.git \
    && cd PackageMega \
    && python3 setup.py develop \
    && cd .. \
    && git clone https://github.com/dcdanko/gimme_input.git \
    && cd gimme_input \
    && python3 setup.py develop \
    && cd .. \
    && git clone https://github.com/dcdanko/ModuleUltra.git \
    && cd ModuleUltra \
    && python3 setup.py develop \
    && cd .. \
    && pip3 install blessings


USER metasub
RUN cd /home/metasub \
    && moduleultra init \
    && echo y | moduleultra install https://github.com/MetaSUB/MetaSUB_QC_Pipeline.git \
    && echo y | moduleultra install https://github.com/MetaSUB/MetaSUB_CAP \
    && moduleultra add pipeline metasub_cap \
    && moduleultra add pipeline metasub_qc_cap

WORKDIR /home/metasub
