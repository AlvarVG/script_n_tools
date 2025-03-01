# Scripts and Tools Repository

This repository contains a collection of scripts and tools that I have used in past projects and will continue to use in the future. Each tool is dockerized to make it easy to run and deploy in different environments (you also wont need to download all the dependencies).

## Contents

This repository includes scripts for various tasks such as data analysis, process automation, API integration, etc. All scripts are dockerized and prepared to run in an isolated and reproducible manner. As now, this are the tools:

- [intensifier](./intensifier/README.md): gets an avatar image and modifies it to make it look more intense.
- [wifi qr generator](./wifi_qr_generator/README.md): creates a qr to share your wifi password.

## Repository Structure

In each folder you will find a script or tool ready to be used. That folder should have: Makefile (building and pushing the docker image), Dockerfile (in order to generate the image), README.md (explaining as much as possible for that folder) and all the needed files in order to make ir work (inside files folder).

In the root of this repo you will also find a Makefile.common; this file will make all the different folder Makefile and Dockerfile to behave in the same way.

## Requirements

Before running the tools in this repository, make sure you have the following installed and configured. Later on, each tools will need each own requirements:

- **Docker**: The tools are dockerized, so you need to have Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).
- **containerd** (or a compatible builder): You need to have containerd activated or a builder that can manage and store multi-architecture images. [More info](https://docs.docker.com/desktop/features/containerd/)

## Contributing

If you would like to contribute to this repository, please follow these steps:

1. Fork the repository.
2. Create a branch for your changes (git checkout -b feature/new-tool).
3. Make your changes and ensure everything is working correctly.
4. Open a pull request explaining the changes you have made.
