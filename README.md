# COVID-19 Tracking System

A Python-based COVID-19 tracking system that provides real-time statistics and visualizations of COVID-19 data globally and by country.

## Features

- Get global COVID-19 statistics
- Get country-specific COVID-19 statistics
- Generate visualizations of global COVID-19 data
- Real-time data from disease.sh API

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python covid_tracker.py
```

The program provides a menu-driven interface with the following options:
1. Get Global Statistics - View worldwide COVID-19 statistics
2. Get Country Statistics - View COVID-19 statistics for a specific country
3. Plot Global Statistics - Generate a bar chart of global COVID-19 statistics
4. Exit - Close the program

## Data Source

This project uses the disease.sh API to fetch real-time COVID-19 data. The data is updated regularly and provides accurate statistics about:
- Total cases
- Total deaths
- Total recoveries
- Active cases

## Requirements

- Python 3.7+
- requests
- pandas
- matplotlib
- python-dotenv