# CMSE 492 Tooling Check

This repository contains a simple Python script used to verify that a Python virtual environment (venv) is set up correctly for CMSE 492.

## Structure

- src/simple_analysis.py: creates a small pandas DataFrame, computes a summary statistic, and generates a simple matplotlib plot
- README.md: setup and usage instructions
- requirements.txt: list of required Python packages

## Setup and Usage (Windows PowerShell)

All commands below should be run from the project root directory (the folder containing README.md) using PowerShell.

Create the virtual environment:
python -m venv .venv

Activate the virtual environment:
.\.venv\Scripts\Activate

Install required packages:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Run the analysis script:
python src/simple_analysis.py

Deactivate the virtual environment when finished:
deactivate

## Analysis

The analysis for this project is implemented in a Python script that demonstrates a basic data workflow. The script creates a small pandas DataFrame with sample data, computes a simple summary statistic (the mean of one column), and generates a basic visualization using matplotlib.

The analysis script is located at:
src/simple_analysis.py

To run the analysis, make sure the virtual environment is activated and then run:
python src/simple_analysis.py
