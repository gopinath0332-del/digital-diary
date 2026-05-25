     1|# Digital Diary
     2|
     3|My personal digital chronicle.
     4|
     5|
     6|## 🛠 Automation & Syncing
     7|
     8|This repository is managed by an AI agent (Hermes). To ensure consistency and avoid conflicts, please use the provided synchronization script for adding new entries.
     9|
    10|### Using `sync_diary.py`
    11|The script `scripts/sync_diary.py` automates the following workflow:
    12|1. **Pull**: Performs a `git pull` to ensure the local copy is up-to-date.
    13|2. **Format**: Automatically adds the date header (`# YYYY-MM-DD`) and the entry timestamp (`**[HH:MM]**`).
    14|3. **Append**: Appends the new entry to the end of the day's file to preserve history.
    15|4. **Push**: Commits and pushes the changes back to GitHub.
    16|
    17|**Usage:**
    18|```bash
    19|python3 scripts/sync_diary.py "Your diary entry text here"
    20|```
    21|
    22|### Formatting Guidelines
    23|- **Entries**: Must follow the `**[HH:MM]** text` format.
    24|- **Images**: All images should be stored in the `diary/images/` directory and compressed to save space on the hosting device (Raspberry Pi).
    25|


### 🖼 Image Management
To prevent storage bloat on the Raspberry Pi, all images must be compressed before being added to the repository.

**Compression Tool:**
Use the script located at `~/.hermes/profiles/diary-profile/scripts/compress_image.py`. 

**Workflow:**
1. Compress the image.
2. Move the compressed version to `diary/images/`.
3. Reference it in the markdown file using: `![alt text](./images/filename.jpg)`.
4. Delete the original high-resolution file from the local cache.
