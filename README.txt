# Daily GitHub Progress

A simple Python script that helps you record what you worked on each day and automatically commit and push the update to GitHub.

## 📁 Files

* `daily_commit.py` — Python script that asks for your daily progress.
* `daily-progress.txt` — Stores your daily progress.
* `run_daily.bat` — Starts the Python script automatically.
* `README.txt` — This file.

## 🚀 Setup

### 1. Clone or download the project

Put the project folder anywhere on your computer.

### 2. Open the folder

Make sure the folder is already a Git repository and connected to your GitHub repository.

If you are starting a new repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

### 3. Check Python

Make sure Python is installed:

```bash
python --version
```

### 4. Run it

You don't need to open PowerShell or type `cd` every day.

Just double-click:

```text
run_daily.bat
```

The program will ask:

```text
What did you work on today?
>
```

Type what you worked on and press **Enter**.

The script will automatically:

1. Add your progress to `daily-progress.txt`
2. Create a Git commit
3. Push the commit to GitHub

## 📝 Example

You enter:

```text
Learned JavaScript arrays and practiced some problems.
```

The file will contain:

```text
2026-08-11 - Learned JavaScript arrays and practiced some problems.
```

## ⚠️ Requirements

You need:

* Python installed
* Git installed
* A GitHub repository
* GitHub authentication configured
* Internet connection

That's it! 🎉
