# Daily GitHub Progress

This folder contains a Python script that records your daily progress and commits it to GitHub.

## How to use

1. Copy `daily_commit.py` into the root of your existing GitHub repository.
2. Open PowerShell/Terminal in that repository.
3. Run:

    python daily_commit.py

4. Enter what you worked on today.
5. The script adds the entry to `daily-progress.txt`, commits it, and pushes it to GitHub.

## Important

Your repository must already be initialized with Git and have a GitHub remote configured.

Check with:

    git remote -v

Test that pushing works manually before using the script:

    git push
