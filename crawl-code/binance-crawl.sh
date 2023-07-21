#!/bin/bash

# Check if venv folder exists
if [ ! -d "venv" ]; then
    echo "venv folder not found. Creating a virtual environment..."
    python -m venv venv
    echo "Virtual environment created."
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the Python script
python binance-crawl.py

