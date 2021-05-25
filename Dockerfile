FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

MAINTAINER Matsushita Lab

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    subversion \
    cmake \
    libx11-dev \
    libxxf86vm-dev \
    libxcursor-dev \
    libxi-dev \
    libxrandr-dev \
    libxinerama-dev \
    libglew-dev \
    htop

RUN apt update && \
    apt -y upgrade && \
    apt install -y python3-pip

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV CPATH=/usr/local/include:$CPATH
ENV CUDA_PATH=/usr/local/cuda
ENV PATH=$CUDA_PATH/bin:$PATH
ENV CPATH=$CUDA_PATH/include:$CPATH
ENV LD_LIBRARY_PATH=$CUDA_PATH/lib64:$CUDA_PATH/lib:/usr/local/lib:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH

RUN mkdir /blender-git && \
    cd /blender-git && \
    git clone https://git.blender.org/blender.git

RUN mkdir /blender-git/lib && \
    cd /blender-git/lib && \
    svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64

SHELL ["/bin/bash", "-c"]

RUN cd /blender-git/blender/source/blender/compositor/operations && \
    sed -i -e "56,58d" COM_ViewerOperation.h && \
    set +H && \
    sed -i -e "48 s/!G.background/true/g" COM_PreviewOperation.h && \
    set -H

RUN cd /blender-git/blender && \
    make update && \
    make
