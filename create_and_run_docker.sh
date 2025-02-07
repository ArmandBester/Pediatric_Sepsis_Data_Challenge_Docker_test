#!/bin/bash

# Usage:
#  This script will remove and recreate the model and test_outputs directories
#     in the current (executing) directory, so no stale data exists between runs.
#
#  No modifications to this script should be required,
#    besides optionally renaming the docker_image_name
#
#  This script will remove and recreate the docker images,
#    to prevent the buildup of multiple images between builds
#
#  The models and the test_outputs directories are mounted into the container
#    and any output written to those directories will be persistent
#  NOTE:
#    Each time this script is executed, all data in the model and test_outputs is lost
 

# You may specify the name of your docker image here (it must be lowercase)

docker_image_name=pedriatric_challenge_2024


###############################################################################
#               No further modifications should be required                   #
###############################################################################

# If the model and test_outputs directories exist, they will be removed now

[ -e model ] && /bin/rm -rf model
[ -e test_outputs ] && /bin/rm -rf test_outputs

# Create the expected model and test_outputs directories
mkdir model test_outputs

# Check if a docker container with the specified name exists; if one exists, forcefully remove it
docker image ls $docker_image_name && docker image rm $docker_image_name --force

# Create a docker container with the name as specified in the variable
docker build --tag "$docker_image_name" .

# Run the container and mount the model and test_outputs directories in the correct paths within the container
docker run --mount type=bind,source=./model,target=/challenge/model --mount type=bind,source=./test_outputs,target=/challenge/test_outputs "$docker_image_name"
