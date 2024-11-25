import subprocess
from git import Repo

def git_quickfix(repo_path, commit_message, remote_name):
    # Initialize the Git repository
    repo = Repo(repo_path)
    repo.git.add(all=True)  # Stage all changes

    # Commit the changes with the specified message
    repo.index.commit(commit_message)

    # Push the changes to the remote repository
    origin = repo.remote(name=remote_name)
    origin.push()
    
if __name__ == "__main__":
    repo_path = "."
    commit_message = "quick fix"
    remote_name = "origin"

    git_quickfix(repo_path, commit_message, remote_name)