# Pediatric_Sepsis_Data_Challenge_Docker_test

Python heavily borrowed from here [https://github.com/Kamaleswaran-Lab/The-2024-Pediatric-Sepsis-Challenge](https://github.com/Kamaleswaran-Lab/The-2024-Pediatric-Sepsis-Challenge)

This is an example to completely automate team submissions in terms of training and running models

## How to execute.

**clone the repo**

```
git clone https://github.com/ArmandBester/Pediatric_Sepsis_Data_Challenge_Docker_test.git
```

**move into the repo**

```
cd Pediatric_Sepsis_Data_Challenge_Docker_test/
```

**run the bash script**

```
bash create_and_run_docker.sh
```

Read the comments in this file to know how to edit, but it optionally should only be the docker image name. Teams should edit the `run_all.sh` script to run the team code. This bash script also assumes your model will be written to `model/[your_model_name]` and the output of predictions be written to `test_outputs/outputs.txt`.

## What will happen?

- The `create_and_run_docker.sh` script will build your docker iamge using your `Dockerfile`. You can use your own `FROM` base image import as you require. You can install your own dependancies as required using your operating system's methadology. The rest of the Dockerfile should probably be left as is.





