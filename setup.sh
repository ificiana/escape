if ! command -v poetry &> /dev/null
then
    echo "poetry could not be found"
    python3 utils/install_poetry.py
    export PATH="$HOME/.local/bin:$PATH"

    # install dependencies
    poetry install
    poetry shell
    exit
fi

