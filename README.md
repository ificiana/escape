# pyweek35

Team submission for pyweek35, repo will be renamed once we have a name for the game

# Setup Guide

First install poetry following : https://python-poetry.org/docs/

### For Windows run:
  #### Make sure to run in Command Prompt (NOT in powershell)

  `curl -sSL https://install.python-poetry.org | python -`

  `set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\pypoetry\venv\Scripts`

### For Mac or Linux:

  `curl -sSL https://install.python-poetry.org | python3 -`

  `export PATH="$HOME/.local/bin:$PATH"`

### Install the dependencies:

  `poetry install -n`

### Next to run the game:

  `poetry run game`


# Dev Guidelines

- Work in the `dev` branch before merging into the `main`
- Rebase your work before pushing, try to keep the git history clean
- Don't push directly to any branch, do a PR

# Appendix

## Using Virtual Environment (venv)

To isolate dependencies and manage packages for this project, we recommend using Python's built-in `venv` module. Follow these steps to create and activate a virtual environment:

### On Windows

1. Open a command prompt and navigate to the project directory.

2. Create a virtual environment using the following command:

`python -m venv venv`

This will create a virtual environment named `venv` inside the project directory.

3. Activate the virtual environment by running:

`.\venv\Scripts\activate`

Your command prompt should now show the virtual environment's name, e.g., `(venv)`.

### On macOS and Linux

1. Open a terminal and navigate to the project directory.

2. Create a virtual environment using the following command:

`python3 -m venv venv`

This will create a virtual environment named `venv` inside the project directory.

3. Activate the virtual environment by running:

`source venv/bin/activate`

Your terminal prompt should now show the virtual environment's name, e.g., `(venv)`.

### Installing Dependencies

With the virtual environment activated, install the required packages using:

`pip install -r requirements.txt`

### Deactivating the Virtual Environment

When you are done working with the project, you can deactivate the virtual environment by running:

`deactivate`

This will return your terminal or command prompt to its normal state.

### Setting up pre-commit

We use pre-commit to run some checks before committing. To set it up, run:

`pre-commit install`

This will install the pre-commit hook into your local git repository. Now, whenever you commit, the pre-commit hook will run and check for any errors. If there are any errors, the commit will fail and you will have to fix them before committing again.

## License

All code is licensed under the [MIT License](https://github.com/ificiana/pyweek35/blob/dev/LICENSE).

The licenses for the `/assets/sounds` are as follows:

- [Glacier](https://freemusicarchive.org/music/SalmonLikeTheFish/Music_for_the_Sleepy_Traveler/03_-_Glacier/) by [SalmonLikeTheFish](https://freemusicarchive.org/music/SalmonLikeTheFish/) is under the licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- [Insomnia](https://freemusicarchive.org/music/David_Hilowitz/Paralytic_Insomnia) by [David Hilowitz](https://freemusicarchive.org/music/David_Hilowitz/) is under the licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
- [Japan](https://freemusicarchive.org/music/Yakov_Golman/Piano_album_1/Yakov_Golman_-_Japan/) by [Yakov Golman](https://freemusicarchive.org/music/Yakov_Golman/) is under the licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- All other sound effects in `/assets/sounds` are under the [Mixkit Sound Effects Free License]](https://mixkit.co/license/)
