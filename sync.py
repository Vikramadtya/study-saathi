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

    # 2. Parse changed files for the commit message
    changed_files = [line.split()[-1] for line in status.split('\n') if line]
    files_str = ", ".join(changed_files)
    
    print(f"👀 Changes detected in: {files_str}")
    
    print("📦 Staging files...")
    run_cmd("git add .")
    
    print("📝 Committing...")
    # Escape quotes for the commit message
    commit_msg = f'docs: update {files_str}'
    run_cmd(f'git commit -m "{commit_msg}"')
    
    print("🚀 Pushing to remote...")
    push_result = subprocess.run("git push", shell=True)
    
    if push_result.returncode == 0:
        print("✅ Successfully synced to remote!")
    else:
        print("❌ Failed to push to remote.")

if __name__ == "__main__":
    main()