# bbocebot
Battlebit OCE Server Discord Bot

# Getting Started
## Installation
Install python 3 (3.11.5)

Install venv if not already installed:
```$ python3 -m pip install venv```

Initialize a python virtual environment with:
```$ python3 -m venv .venv```

Then activate the virtual environment with:
```$ ./venv/Scripts/activate```

Install pip packages:
```$  pip3 install -r requirements.txt```

Set the discord api token in the .env file.

## Running the discord bot:

You need to create a `.env` file in the working directory. You then need to add the `DISCORD_API_TOKEN` key and value. You'll have to ask David for a test token or use your own.

After the `.env` is setup, run the discord bot with the following:
```$ ./venv/Scripts/python.exe main.py```

Stop the bot from running by hitting: `CTRL + C` in the console.