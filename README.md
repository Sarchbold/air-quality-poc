    # air-quality-poc
Prototype repo for analyzing air quality data against covid restriction timelines in Boston

To install dependencies, run pip install -r requirements.txt

To update the requirements.txt, install pip-tools, edit requirements.in, and run pip-compile ./requirements.in

To generate a docker image build with the requirements installed run 

    ./docker-build.sh 