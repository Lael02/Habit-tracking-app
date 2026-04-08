# Habit-tracking-app
## Overview

This application is a command-line habit tracking application built in Python. Here, users to create, manage, and analyse habits over time.

## Features

* Create daily and weekly habits
* Mark habits as completed
* Delete habits
* View all habits
* Calculate streaks
* Show the longest streak across all habits

## How It Works

Habit data is stored in a JSON file (`data.json`). Each habit has completion timestamps, which are used to calculate streaks.

The streak calculation respects the habit’s frequency:

* Daily habits → 1 day between completions
* Weekly habits → 7 days between completions

## Project Structure

* `application.py` → user interface (menu)
* `management.py` → handles creating, updating, and deleting habits (Create, Read, Update, Delete)
* `analytics.py` → calculates streaks
* `storage.py` → loads and saves data
* `habits.py` → defines the Habit class

## How to Run

Run the app with:
(cd habit_tracker)
python application.py

## Run Tests
python -m unittest

## Data
The project includes 4 weeks of predefined habit data to test streak calculations.
## Author
Lael Lukoki


