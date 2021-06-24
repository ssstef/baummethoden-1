# Baummethoden

## 4 Tickets

- Task 1: Daten herunterladen
- Task 2: Modell trainieren und mit train.py im Terminal ausführen
- Task 3: Modell speichern (als pickle File)
- Task 4: Modell im predict.py file laden und im Terminal ausführen

## Setup

### Linux Users

- create new python environment: `python3 -m venv .venv`
- activate python environment: `source .venv/bin/activate`
- install dependencies: `pip install -r requirements.txt`

### Windows Users

- create new python environment: `python -m venv .venv`
- activate python environment: `.\.venv\Scripts\Activate.ps1`
- install dependencies: `pip install -r requirements.txt`

## Development

- activate python environment: `source .venv/bin/activate`
- run python script: `python <filename.py> `, e.g. `python train.py`
- install new dependency: `pip install sklearn`
- save current installed dependencies back to requirements.txt: `pip freeze > requirements.txt`
- start python api with `python wsgi.py`

## Set Up API Hosting

- Create a heroku account
- Create a new app and save the name
- Go to your Account Settings and save the API Key
- Go to the secrets in the settings of your GitHub repository
- Add the API Key as `HEROKU_API_KEY`
- Add the app name as `HEROKU_APP_NAME`
- Add your email address (the one you used for creating the heroku account) as `HEROKU_EMAIL`
- The github actions scripts assumes that a `heroku` branch exists. If it doesn't, create the branch
- After the first successful github actions deployment, you should be able to access the api via `https://<your-app-name>.herokuapp.com`

## GitHub Actions within this repository

### pull-request

- action that is run on every pull request `open` and `synchronize` event

```
on:
  pull_request:
    types: [opened, synchronize]
```

- the action will run `train.py` and upload the model as an artifact inside the action

### production-release

- action that is run on every `push`in the `main` branch (that also includes merges from any other branch to `main` branch)

```
on:
  push:
    branches:
      - main
```

- the action will run `train.py` and upload the model as an artifact inside the action
- the action will create or checkout a branch called `heroku` and merge `main` to `heroku`
- the action will deploy the code to heroku hosting and run the API, see the [action documentation](https://github.com/AkhileshNS/heroku-deploy) for more information

## Useful commands

- init new git repository: `git init`
- add https://github.com/example/repo.git as remote repository:
  `git remote add origin https://github.com/example/repo.git`
- check configured remote: `git remote -v`
- stage file/directory for commit: `git add <file or directory>`
- commit with message: `git commit - m "message"`
- show git history of current branch: `git log`
- create new branch with history from current branch: `git branch <branchname>`
- check out branch: `git checkout <branchname>`
- pull changes from remote branch into current branch: `git pull`
- push and set remote branchname, always set the same name as local branch name:
  `git push --set-upstream origin <branchname>`
- push changes to existing remote branch: `git push`
- create new python environment: `python3 -m venv .venv`
- activate python environment: `source .venv/bin/activate`
- show installed python dependencies: `pip freeze`
- show installed python dependencies & save to requirements.txt file:
  `pip freeze > requirements.txt`
- install dependencies from file: `pip install -r requirements.txt`
- install single pandas dependency `pip install pandas`
- checkout git branch (if exists) or create a new one (if it does not exist): `git checkout foo 2>/dev/null || git checkout -b foo`, see https://stackoverflow.com/questions/26961371/switch-on-another-branch-create-if-not-exists-without-checking-if-already-exi

- Actions aktivieren