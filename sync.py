import subprocess
import sys

def run_cmd(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def main():
    # 1. Check for changes
    status = run_cmd("git status -s")
    if not status:
        print("✨ No changes detected. Everything is already up to date!")
        sys.exit(0)

    added = []
    updated = []
    deleted = []

    # 2. Categorize files based on their 2-character Git status code
    for line in status.split('\n'):
        if not line:
            continue
        code = line[:2]
        filename = line[3:]

        if '?' in code or 'A' in code:
            added.append(filename)
        elif 'M' in code:
            updated.append(filename)
        elif 'D' in code:
            deleted.append(filename)

    # Print nicely to the terminal
    print("👀 Changes detected:")
    if added: print(f"  🟢 Added: {', '.join(added)}")
    if updated: print(f"  🟡 Updated: {', '.join(updated)}")
    if deleted: print(f"  🔴 Deleted: {', '.join(deleted)}")

    print("\n📦 Staging files...")
    run_cmd("git add .")

    print("📝 Committing...")
    # Build a clean, multiline commit message
    commit_msg = "docs: auto-sync updates\n\n"
    if added: commit_msg += f"Added: {', '.join(added)}\n"
    if updated: commit_msg += f"Updated: {', '.join(updated)}\n"
    if deleted: commit_msg += f"Deleted: {', '.join(deleted)}\n"
    
    # Run commit using a list to safely pass the multiline string
    subprocess.run(["git", "commit", "-m", commit_msg])

    print("🚀 Pushing to remote...")
    subprocess.run(["git", "push"])
    
    print("✅ Successfully synced to remote!")

if __name__ == "__main__":
    main()