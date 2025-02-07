FROM python:3.10.1-buster

## DO NOT EDIT these 3 lines.
RUN mkdir /challenge
COPY ./ /challenge
WORKDIR /challenge
RUN mkdir /challenge/model
RUN mkdir /challenge/test_outputs

## Install your dependencies here using apt install, etc.

# Copy your scripts 
#COPY 1_team_code_train.py ./
#COPY 2_team_code_run.py ./
#COPY helper_code.py ./


## Include the following line if you have a requirements.txt file.
RUN pip install -r requirements.txt

CMD ["bash", "run_all.sh"]



