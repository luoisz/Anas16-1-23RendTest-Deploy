from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info
from os import path as ospath, environ
from subprocess import run as srun
from requests import get as rget
from dotenv import load_dotenv
from pymongo import MongoClient
import time
import urllib.request
while True:
  URL = "https://drivetalkanasrender.onrender.com"
  Wait_Time = 10
  print("Pinging...")
  time.sleep(Wait_Time)
  ping = urllib.request.urlopen(URL)
  status = str(ping.status)
  print(f"Cron-Job is working with status ({status})")

if ospath.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[FileHandler('log.txt'), StreamHandler()],
                    level=INFO)

CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = rget(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('config.env', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        log_error(f"CONFIG_FILE_URL: {e}")
except:
    pass

load_dotenv('config.env', override=True)

UPSTREAM_REPO = "https://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@github.com/luoisz/Anas16-1-23RendTest-Host"
UPSTREAM_BRANCH = 'master'

# UPSTREAM_REPO = environ.get('UPSTREAM_REPO', '')
# if len(UPSTREAM_REPO) == 0:
   # UPSTREAM_REPO = "https://github.com/anasty17/mirror-leech-telegram-bot"

# UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH', '')
# if len(UPSTREAM_BRANCH) == 0:
    # UPSTREAM_BRANCH = 'master'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update = srun([f"git init -q \
                     && git config --global user.email e.anastayyar@gmail.com \
                     && git config --global user.name mltb \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        log_info('Successfully updated with latest commit from https://github.com/anasty17/mirror-leech-telegram-bot')
    else:
        log_error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
