FROM osrf/ros:noetic-desktop-full

# Enable nvidia-container-runtime support
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# Set environment variables
ENV CMU_VLA_CHALLENGE_PATH=/workspace/cmu_vla_challenge_unity
ENV AI_MODULE_PATH=/workspace/ai_module

# Set ROS distribution
ENV ROS_DISTRO noetic

# C++ 17 setting
ENV CXX_FLAGS="-std=c++17"

# Install essential system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    dirmngr \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Install GCC 8 and G++ 8
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get install -y gcc-8 g++-8 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 && \
    rm -rf /var/lib/apt/lists/*

# Install essential libraries (PCL, Eigen, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    curl \
    git \
    wget \
    unzip \
    libatlas-base-dev \
    libeigen3-dev \
    libpcl-dev \
    libgoogle-glog-dev \
    libsuitesparse-dev \
    libglew-dev \
    libusb-dev \
    python3-pip \
    python3-osrf-pycommon \
    python3-rosdep \
    python3-catkin-tools \
    python3-vcstool \
    python-yaml \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/*

# Install gdown
RUN pip3 install gdown

# Install additional ROS Noetic packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-tf \
    ros-noetic-cv-bridge \
    ros-noetic-pcl-conversions \
    ros-noetic-xacro \
    ros-noetic-robot-state-publisher \
    ros-noetic-rviz \
    ros-noetic-image-transport \
    ros-noetic-image-transport-plugins \
    ros-noetic-pcl-ros \
    ros-noetic-eigen-conversions \
    ros-noetic-tf-conversions \
    ros-noetic-catkin \
    && rm -rf /var/lib/apt/lists/*

# Clone CMU VLA Challenge Unity repository
RUN git clone https://github.com/jizhang-cmu/cmu_vla_challenge_unity.git ${CMU_VLA_CHALLENGE_PATH} && \
    cd ${CMU_VLA_CHALLENGE_PATH} && \
    git checkout noetic

# Load ROS environment at each run
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Configure /workspace/ai_module as a safe directory, so that Weights & Biases can be used.
RUN git config --global --add safe.directory /workspace/ai_module

# Set working directory
WORKDIR ${AI_MODULE_PATH}

CMD ["bash"]
