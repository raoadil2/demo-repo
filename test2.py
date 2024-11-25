import subprocess
import os

def git_quickfix_commit(repo_dir, commit_message="quick fix", target_branch=None):
    """
    Automates the process of staging, committing, and pushing changes to a Git repository.
    It also handles empty commit messages, branch checks, and ensures no duplicate commits.
    
    :param repo_dir: Path to the local Git repository.
    :param commit_message: Commit message for the quick fix.
    :param target_branch: The target branch to commit to (if specified).
    :return: None
    """
    # Change working directory to the repository directory
    os.chdir(repo_dir)

    try:
        # Step 1: Check if git is initialized in the directory
        subprocess.check_call(['git', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Step 2: Handle empty commit message
        if not commit_message.strip():
            raise ValueError("Commit message cannot be empty. Please provide a valid message.")

        # Step 3: Check for unsaved changes
        status = subprocess.check_output(['git', 'status', '--porcelain']).decode('utf-8')
        if not status.strip():
            print("No changes detected. Skipping commit.")
            return  # No changes, skip commit

        # Step 4: Ensure we're on the correct branch
        if target_branch:
            current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()
            if current_branch != target_branch:
                print(f"Warning: You're on branch '{current_branch}', but the target branch is '{target_branch}'.")
                # Optionally, switch to the correct branch
                # subprocess.check_call(['git', 'checkout', target_branch])
                return  # You can uncomment the above line if you want to switch branches automatically

        # Step 5: Add all changes (can be modified to add specific files)
        print("Adding changes to git...")
        subprocess.check_call(['git', 'add', '.'])

        # Step 6: Commit changes with a quick fix message
        print(f"Committing changes with message: '{commit_message}'...")
        subprocess.check_call(['git', 'commit', '-m', commit_message])

        # Step 7: Push the changes to the remote repository
        print("Pushing changes to remote repository...")
        subprocess.check_call(['git', 'push'])

        print("Quick fix commit pushed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Git command: {e}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
repo_path = '.'  # Change this to your repo path
git_quickfix_commit(repo_path, commit_message="quick fix", target_branch="main")
      
        
# import subprocess
# import os


# def git_quickfix_commit(repo_dir, commit_message="quick fix"):
#     """
#     Automates the process of staging, committing, and pushing changes to a Git repository.

#     :param repo_dir: Path to the local Git repository.
#     :param commit_message: Commit message for the quick fix.
#     :return: None
#     """
#     # Change working directory to the repository directory
#     os.chdir(repo_dir)

#     try:
#         # Step 1: Check if git is initialized in the directory
#         subprocess.check_call(
#             ['git', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         # Step 2: Add all changes (can be modified to add specific files)
#         print("Adding changes to git...")
#         subprocess.check_call(['git', 'add', '.'])

#         # Step 3: Commit changes with a quick fix message
#         print(f"Committing changes with message: '{commit_message}'...")
#         subprocess.check_call(['git', 'commit', '-m', commit_message])

#         # Step 4: Push the changes to the remote repository
#         print("Pushing changes to remote repository...")
#         subprocess.check_call(['git', 'push'])

#         print("Quick fix commit pushed successfully!")

#     except subprocess.CalledProcessError as e:
#         print(f"Error occurred while running Git command: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# # Example usage
# repo_path = '.'  # Change this to your repo path
# git_quickfix_commit(repo_path)
