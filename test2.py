import subprocess

def git_quickfix_commit(message):
    try:
        # Add changes to the index
        subprocess.run(['git', 'add', '--all'], check=True)

        # Commit changes with the specified message
        subprocess.run(['git', 'commit', '-m', message], check=True)

        # Push changes to the remote repository
        subprocess.run(['git', 'push'], check=True)

        print(f"Git quickfix commit successful with message: '{message}'")
    except subprocess.CalledProcessError as e:
        print(f"Git quickfix commit failed: {e}")

git_quickfix_commit("Quick fix for issue #123")