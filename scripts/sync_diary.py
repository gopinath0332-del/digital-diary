import sys
import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = "/home/pi/digital-diary"
DIARY_DIR = os.path.join(REPO_PATH, "diary")

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing: {cmd}")
        print(f"Stderr: {result.stderr}")
        return None
    return result.stdout

def sync_diary(content):
    # 1. Change to repo directory and pull
    print(f"Pulling latest changes from {REPO_PATH}...")
    run_command(f"git -C {REPO_PATH} pull")

    # 2. Determine today's file
    today_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M")
    file_path = os.path.join(DIARY_DIR, f"{today_date}.md")

    # 3. Handle file content
    existing_content = ""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            existing_content = f.read()

    # If file doesn't exist, start with the Date Header
    if not existing_content:
        header = f"# {today_date}\n\n"
    else:
        header = ""

    # Format new entry as **[HH:MM]** content
    new_entry = f"**[{current_time}]** {content}"
    
    separator = "\n\n" if existing_content else ""
    final_content = header + existing_content + separator + new_entry

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    # 4. Commit and Push
    print("Pushing to GitHub...")
    run_command(f"git -C {REPO_PATH} add .")
    run_command(f"git -C {REPO_PATH} commit -m 'Update diary: {today_date}'")
    push_res = run_command(f"git -C {REPO_PATH} push")
    
    if push_res is not None:
        print("Successfully synced to repository!")
    else:
        print("Failed to push changes.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_diary.py \"Entry text here\"")
        sys.exit(1)
    
    entry_text = sys.argv[1]
    sync_diary(entry_text)
