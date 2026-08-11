# Dev Daily Tracker

A simple Python application for tracking your daily programming and learning progress.

## Features

* Add multiple tasks every day
* Record hours worked
* Choose a development category
* Prevent accidental duplicate daily entries
* View today's progress
* View recent progress
* Track your current streak
* Count active days
* Track total hours
* See hours spent in each category
* Generate a weekly summary
* Automatically create Git commits
* Automatically push changes to GitHub
* Store progress in a readable TXT file
* Store structured data in a JSON file

## Files

* `daily_tracker.py` — Main Python application
* `daily-progress.txt` — Human-readable progress history
* `daily-progress.json` — Structured data used by the application
* `run_daily.bat` — Windows launcher
* `README.txt` — Project documentation

## Requirements

You need:

* Python
* Git
* A GitHub repository
* GitHub authentication
* Internet connection

Check your installations:

```bash
python --version
git --version
```

## Setup

Put the project inside your Git repository.

If you are creating a new Git repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Running the Application

You don't need to open PowerShell or type `cd` every day.

Simply double-click:

```text
run_daily.bat
```

You will see a menu:

```text
1. Add/update today's progress
2. View today's progress
3. View recent progress
4. View statistics
5. View weekly summary
6. Push changes to GitHub
7. Add progress and push
8. Exit
```

For normal daily use, choose:

```text
7
```

The program will ask what you worked on.

You can enter multiple tasks:

```text
> Learned JavaScript arrays
> Practiced coding problems
> Worked on my React project
> DONE
```

Then enter your hours and select a category.

The program will save your progress and push the changes to GitHub.

## Moving the Project

If you move the project to another location, edit `run_daily.bat`.

Change:

```bat
cd /d "C:\Users\hassa\Downloads\daily_github_progress"
```

to the new location.

## Important

This project is designed to document real programming and learning activity.

It should not be used to create fake GitHub activity.
