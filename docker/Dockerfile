ARG CUDA_VERSION=10.0
FROM nvidia/cuda:${CUDA_VERSION}-devel
LABEL maintainer="Brian Team <team@briansimulator.org>"

ARG DEBIAN_FRONTEND=noninteractive

# Install conda
ARG MINICONDA_VERSION=4.7.12
ARG MINCONDA_MD5=0dba759b8ecfc8948f626fa18785e3d8
ENV CONDA_DIR=/opt/conda
RUN apt-get -qq update && \
    apt-get -qq -y install --no-install-recommends \
    bzip2 \
    # curl \
    wget && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "${MINCONDA_MD5} *Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash /Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    # apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    # RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    # /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    # rm ~/miniconda.sh && \
    # ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    # echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    # echo "conda activate base" >> ~/.bashrc

    # && curl -sSL https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    # && bash /tmp/miniconda.sh -bfp /usr/local \
    # && rm -rf /tmp/miniconda.sh \
    # && conda install -y python=2 \
    # && conda update conda \
    # && apt-get -qq -y autoremove \
    # && apt-get autoclean \
    # && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    # && conda clean --all --yes

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    g++ \
    gcc \
    git \
    make && \
    apt-get -qq -y autoremove && \
    # apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/dpkg.log

ENV CUDA_PATH=/usr/local/cuda-${CUDA_VERSION} \
    PATH=${CONDA_DIR}/bin:${CUDA_PATH}/bin:$PATH \
    LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs:${LD_LIBRARY_PATH}"

WORKDIR /root

ARG PYTHON_VERSION=3.7
ENV BRIAN2_VERSION=2.2.2.1 \
    BRIAN2GENN_VERSION=1.3.1 \
    GENN_VERSION=4.0.2 \
    GENN_PATH=/root/genn
RUN conda config --prepend channels conda-forge
RUN conda install --quiet --yes \
    brian2=${BRIAN2_VERSION} \
    cudatoolkit=${CUDA_VERSION} \
    matplotlib \
    pip \
    python=${PYTHON_VERSION} && \
    pip install brian2genn==${BRIAN2GENN_VERSION} && \
    conda clean --all -f -y
RUN git clone -b $GENN_VERSION https://github.com/genn-team/genn $GENN_PATH

CMD ["/bin/bash"]