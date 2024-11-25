import subprocess
import os

def git_quickfix_commit(repo_dir, commit_message="quick fix"):
    """
    Automates the process of staging, committing, and pushing changes to a Git repository.
    
    :param repo_dir: Path to the local Git repository.
    :param commit_message: Commit message for the quick fix.
    :return: None
    """
    # Change working directory to the repository directory
    os.chdir(repo_dir)

    try:
        # Step 1: Check if git is initialized in the directory
        subprocess.check_call(['git', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Step 2: Add all changes (can be modified to add specific files)
        print("Adding changes to git...")
        subprocess.check_call(['git', 'add', '.'])

        # Step 3: Commit changes with a quick fix message
        print(f"Committing changes with message: '{commit_message}'...")
        subprocess.check_call(['git', 'commit', '-m', commit_message])

        # Step 4: Push the changes to the remote repository
        print("Pushing changes to remote repository...")
        subprocess.check_call(['git', 'push'])

        print("Quick fix commit pushed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
repo_path = '.'  # Change this to your repo path
git_quickfix_commit(repo_path)
