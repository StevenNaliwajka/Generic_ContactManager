#!/bin/bash

VENV_DIR="venv"
PYTHON_VERSION="3.13"
PYTHON_BINARY="python$PYTHON_VERSION"

# Check if Python 3.13 is installed on the system
if ! command -v $PYTHON_BINARY &> /dev/null
then
    echo "Error: Python $PYTHON_VERSION is not installed on the system."
    echo "Please install Python $PYTHON_VERSION first."
    exit 1
fi

# Check if the virtual environment exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists."

    # Check the Python version inside the virtual environment
    VENV_PYTHON_VERSION=$($VENV_DIR/bin/python --version 2>&1)

    if [[ $VENV_PYTHON_VERSION == *"$PYTHON_VERSION"* ]]; then
        echo "Python $PYTHON_VERSION is already installed in the virtual environment."
        exit 0
    else
        echo "Incorrect Python version found in venv. Reinstalling venv with Python $PYTHON_VERSION..."
        rm -rf $VENV_DIR
    fi
fi

# Create a new virtual environment with Python 3.13
echo "Creating virtual environment with Python $PYTHON_VERSION..."
$PYTHON_BINARY -m venv $VENV_DIR

if [ $? -eq 0 ]; then
    echo "Virtual environment created successfully."
else
    echo "Error: Failed to create virtual environment."
    exit 1
fi

# Activate venv and ensure pip is up-to-date
source $VENV_DIR/bin/activate
pip install --upgrade pip

echo "Setup complete. Use 'source $VENV_DIR/bin/activate' to activate the environment."
exit 0
