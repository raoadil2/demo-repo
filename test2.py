import subprocess

def git_quickfix():
    subprocess.run(["git", "add", "."])  # Add changes
    subprocess.run(["git", "commit", "-m", "Quick fix"])  # Commit with a "quick fix" message
    subprocess.run(["git", "push"])  # Push changes to the remote repository
    
git_quickfix()