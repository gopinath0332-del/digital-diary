# Digital Diary

My personal digital chronicle.

## 🛠 Automation & Syncing

This repository is managed by an AI agent (Hermes). To ensure consistency and avoid conflicts, please use the provided synchronization script for adding new entries.

### Using `sync_diary.py`
The script `scripts/sync_diary.py` automates the following workflow:
1. **Pull**: Performs a `git pull` to ensure the local copy is up-to-date.
2. **Format**: Automatically adds the date header (`# YYYY-MM-DD`) and the entry timestamp (`**[HH:MM]**`).
3. **Append**: Appends the new entry to the end of the day's file to preserve history.
4. **Push**: Commits and pushes the changes back to GitHub.

**Usage:**
```bash
python3 scripts/sync_diary.py "Your diary entry text here"
```

## 🖼 Image Management

To prevent storage bloat on the Raspberry Pi, all images must be compressed before being added to the repository.

### Compression Tool
Use the script located at `scripts/compress_image.py`.

### Workflow
1. **Compress**: Run the compression script on the source image.
2. **Save**: Move the compressed version to `diary/images/`.
3. **Reference**: Use markdown format in the diary entry: `![alt text](./images/filename.jpg)`.
4. **Cleanup**: Delete the original high-resolution file from the local cache to conserve storage.

## 📋 Formatting Guidelines
- **Entries**: Must follow the `**[HH:MM]** text` format.
- **Headers**: Each day starts with a `# YYYY-MM-DD` header.
