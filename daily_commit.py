import subprocess
from datetime import date
from pathlib import Path

PROGRESS_FILE = Path("daily-progress.txt")


def run_git(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        print("\n❌ Git command failed:")
        print(" ".join(command))
        if error.stderr:
            print(error.stderr.strip())
        return None


def main():
    if not Path(".git").exists():
        print("❌ This script must be run inside your Git repository.")
        input("\nPress Enter to exit...")
        return

    today = date.today().isoformat()

    print("=" * 40)
    print("       DAILY GITHUB PROGRESS")
    print("=" * 40)
    print(f"\n📅 Date: {today}")
    print("What did you work on today?")
    progress = input("> ").strip()

    if not progress:
        print("\n⚠️ Nothing entered. No commit was made.")
        input("\nPress Enter to exit...")
        return

    with PROGRESS_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{today} - {progress}\n")

    print("\n✅ Progress saved.")

    if run_git(["git", "add", str(PROGRESS_FILE)]) is None:
        input("\nPress Enter to exit...")
        return

    commit_message = f"Daily progress - {today}"

    if run_git(["git", "commit", "-m", commit_message]) is None:
        input("\nPress Enter to exit...")
        return

    print("✅ Commit created.")

    print("\n🚀 Pushing to GitHub...")
    if run_git(["git", "push"]) is None:
        print("\n❌ Push failed.")
        print("The commit exists locally, but was not pushed to GitHub.")
    else:
        print("\n🎉 Successfully pushed to GitHub!")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
