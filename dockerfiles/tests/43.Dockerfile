# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:xenial

# This base image doesn't ship with sudo.
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

COPY scripts/install_debs_cmake.sh cartographer/scripts/
RUN cartographer/scripts/install_debs_cmake.sh && rm -rf /var/lib/apt/lists/*
COPY scripts/install_ceres.sh cartographer/scripts/
RUN cartographer/scripts/install_ceres.sh && rm -rf ceres-solver
COPY scripts/install_proto3.sh cartographer/scripts/
RUN cartographer/scripts/install_proto3.sh && rm -rf protobuf
COPY . cartographer
RUN cartographer/scripts/install_cartographer_cmake.sh && rm -rf cartographer
