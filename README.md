# Baummethoden

## 4 Tickets

- Task 1: Daten herunterladen
- Task 2: Modell trainieren und mit train.py im Terminal ausführen
- Task 3: Modell speichern (als pickle File)
- Task 4: Modell im predict.py file laden und im Terminal ausführen

## Setup

- create new python environment: `python3 -m venv .venv`
- activate python environment: `source .venv/bin/activate`
- install dependencies: `pip install -r requirements.txt`

## Development

- activate python environment: `source .venv/bin/activate`
- run python script: `python <filename.py> `, e.g. `python train.py`
- install new dependency: `pip install sklearn`
- save current installed dependencies back to requirements.txt: `pip freeze > requirements.txt`

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
