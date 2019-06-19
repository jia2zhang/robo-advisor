# robo-advisor
# Link: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/projects/robo-advisor/README.md 

## Create & Activate a new anaconda virtual environment
```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

## Install the required packages specified in the "requirements.txt" file
```sh
pip install -r requirements.txt
pip install pytest # (this may be skipped if test scripts were not created)
pip install python-dotenv
pip install requests
```

## Once ready to run the program, run the following from the command-line
```sh
python robo_advisor.py
```
