# pyweek35

Team submission for pyweek35, repo will be renamed once we have a name for the game

# Setup Guide

On windows, run `setup` and then `python run_game.py`
Not tested on linux and mac yet.

# What goes here?

Include a README file in all your packages. This is the perfect place to explain:

- What dependencies your game requires to run
- How to build and run your game
- The controls
- What there is to see in the game
- Copyright attributions (eg. CC-BY resources you have used)

# Guidelines

- Work in the `dev` branch before merging into the `main`
- Rebase your work before pushing, try to keep the git history clean
- Don't push directly to any branch, do a PR

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
