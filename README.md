[![CircleCI](https://circleci.com/gh/Sarchbold/air-quality-poc/tree/main.svg?style=svg&circle-token=fa313ea772a617091e96a53e4de85a2a36c6a02e)](https://circleci.com/gh/Sarchbold/air-quality-poc/tree/main)
[![codecov](https://codecov.io/gh/Sarchbold/air-quality-poc/branch/main/graph/badge.svg?token=WTA3WTCDOV)](https://codecov.io/gh/Sarchbold/air-quality-poc)

[![GitHub release](https://img.shields.io/github/v/release/sarchbold/air-quality-poc?sort=semver)](https://github.com/Sarchbold/air-quality-poc/releases)

  # air-quality-poc

Prototype repo for analyzing air quality data against covid restriction timelines in Boston

To install dependencies, run pip install -r requirements.txt

To update the requirements.txt, install pip-tools, edit requirements.in, and run pip-compile ./requirements.in

To generate a docker image build with the requirements installed run 

    ./docker-build.sh 

To start the container run:

    Docker run -d -t -p 8000:8000 <image>:<tag> (fast-api:v5)

To scan your container for security vulnerabilities run:

    Docker scan <image>:<tag> (fast-api:v5)
