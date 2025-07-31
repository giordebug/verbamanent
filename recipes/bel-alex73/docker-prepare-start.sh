#!/bin/bash
set -x

cd $( dirname -- "$0"; )

cp ../../requirements*.txt docker-prepare/

docker build -t tts-learn -f docker-prepare/Dockerfile docker-prepare/

mkdir -p ../../../storage
docker run --rm -it \
    -p 2525:2525 \
    --shm-size=256M \
    --name tts-learn-run \
    -v $(pwd)/../../:/a/tts \
    -v $(pwd)/../../../cv-corpus:/a/cv-corpus \
    -v $(pwd)/../../../fanetyka/:/a/fanetyka/ \
    -v $(pwd)/../../../storage:/storage \
    tts-learn
