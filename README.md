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

## Setting up an environment variable named "ALPHAVANTAGE_API_KEY" so that secret credentials are not tracked in version control
Add the following to the ".gitignore" file
```sh
# .gitignore

# ignore secret environment variable values in the ".env" file:
.env
```

Create a new "data directory.
Create another ".gitgnore" file under the "data" directory and paste in the following content:

```sh
# data/.gitignore

# h/t: https://stackoverflow.com/a/5581995/670433

# ignore all files in this directory:
*

# except this gitignore file:
!.gitignore
```

## AlphaVantage API Key
Request your own AlphaVantage API key from https://www.alphavantage.co/
Create a ".env" file and place your secret API Key value in the format of:
```sh
ALPHAVANTAGE_API_KEY="abc123"
```


## Finally once ready to run the program, run the following from the command-line
```sh
python robo_advisor.py
```
