
import subprocess
import requests

def check_git_remotes():
    try:
        remotes_output = subprocess.check_output(['git', 'remote', '-v'], encoding='utf-8')
        remotes = [line.split() for line in remotes_output.strip().split('\n')]
        remotes = [(name, url) for name, url, _ in remotes if '(fetch)' in _]  # Only fetch URLs

        for name, url in remotes:
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code == 200:
                    print(f"Remote '{name}' is accessible at {url}.")
                else:
                    print(f"Remote '{name}' is not accessible. Status code: {response.status_code} at {url}.")
            except requests.RequestException as e:
                print(f"Failed to access remote '{name}' at {url}. Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to list Git remotes. Error: {e}")

check_git_remotes()




# import requests
# import concurrent.futures
# import time
# from urllib.parse import urlparse

# # Function to handle HTTPS URLs with personal access tokens
# def check_https_remote(remote, retries=3, delay=2):
#     # Extract hostname and path for token header
#     parsed_url = urlparse(remote)
#     hostname = parsed_url.hostname
#     token = get_personal_access_token(hostname)
    
#     headers = {'Authorization': f'token {token}'} if token else {}
#     for attempt in range(1, retries + 1):
#         try:
#             response = requests.get(remote, headers=headers)
#             if response.status_code == 200:
#                 print(f"HTTPS remote URL {remote} is reachable with provided token.")
#                 return
#             else:
#                 print(f"Attempt {attempt}: HTTPS remote URL returned status code {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"Attempt {attempt}: Error checking HTTPS remote URL: {e}")
        
#         if attempt < retries:
#             wait_time = delay * (2 ** (attempt - 1))
#             print(f"Retrying in {wait_time} seconds...")
#             time.sleep(wait_time)
#     print(f"HTTPS remote URL {remote} is not reachable after {retries} attempts.")

# # Placeholder function for getting personal access tokens
# def get_personal_access_token(hostname):
#     # Replace with actual logic to retrieve the personal access token for the given hostname
#     return 'your_personal_access_token'

# # Function to handle SSH URLs
# def check_ssh_remote(remote, retries=3, delay=2):
#     # Check if the SSH key is available
#     ssh_key_path = get_ssh_key_path(remote)
    
#     if not ssh_key_path:
#         print(f"Missing SSH key for remote URL {remote}. Unable to verify.")
#         return
    
#     for attempt in range(1, retries + 1):
#         try:
#             # Use subprocess to attempt to run a git ls-remote command using the SSH key
#             cmd = ['git', 'ls-remote', remote, '-h', 'HEAD']
#             subprocess.run(cmd, env={'GIT_SSH_COMMAND': f'ssh -i {ssh_key_path}'}, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
#             print(f"SSH remote URL {remote} is reachable with provided SSH key.")
#             return
#         except subprocess.CalledProcessError as e:
#             print(f"Attempt {attempt}: Error checking SSH remote URL: {e}")
        
#         if attempt < retries:
#             wait_time = delay * (2 ** (attempt - 1))
#             print(f"Retrying in {wait_time} seconds...")
#             time.sleep(wait_time)
#     print(f"SSH remote URL {remote} is not reachable after {retries} attempts.")

# # Placeholder function for getting the SSH key path
# def get_ssh_key_path(remote):
#     # Replace with actual logic to retrieve the SSH key path for the given remote
#     return '/path/to/your/ssh/key'

# def check_git_remotes():
#     remotes_output = subprocess.check_output(['git', 'remote', '-v']).decode('utf-8')
#     remotes = set(line.split()[1] for line in remotes_output.strip().split('\n') if line)
    
#     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#         future_to_remote = {}
#         for remote in remotes:
#             parsed_url = urlparse(remote)
#             if parsed_url.scheme == 'https':
#                 future_to_remote[executor.submit(check_https_remote, remote)] = remote
#             elif parsed_url.scheme == 'ssh':
#                 future_to_remote[executor.submit(check_ssh_remote, remote)] = remote
#         for future in concurrent.futures.as_completed(future_to_remote):
#             remote = future_to_remote[future]
#             try:
#                 future.result()
#             except Exception as exc:
#                 print(f"{remote} generated an exception: {exc}")

# # Make sure to install the requests library if you haven't already
# # pip install requests

# check_git_remotes()

############# Ideal Response 4
    # import subprocess
    # import requests
    # import concurrent.futures
    # import time
    # from urllib.parse import urlparse

    # # Define paths to keys and tokens
    # SSH_KEY_PATH = ".your_ssh_key_path"  # Update this with the path to your SSH key
    # HTTPS_TOKEN = "your_personal_access_token"  # Replace with your token or logic to fetch it
    # LOG_FILE = "remote_check.log"

    # # Helper function to log messages to a file
    # def log_message(message):
    #     with open(LOG_FILE, "a") as log_file:
    #         log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

    # # Function to check SSH remotes
    # def check_ssh_remote(remote, retries=3, delay=2):
    #     hostname = remote.split('@')[1].split(':')[0]  # Extract hostname
    #     for attempt in range(1, retries + 1):
    #         try:
    #             cmd = ["ssh", "-i", SSH_KEY_PATH, "-o", "BatchMode=yes", hostname, "exit"]
    #             response = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             if response.returncode == 0:
    #                 print(f"SSH remote URL {remote} is reachable.")
    #                 return
    #             else:
    #                 error_message = response.stderr.decode('utf-8').strip()
    #                 print(f"Attempt {attempt}: Error checking SSH remote URL: {error_message}")
    #                 log_message(f"SSH remote error for {remote}: {error_message}")
    #         except subprocess.CalledProcessError as e:
    #             print(f"Attempt {attempt}: SSH error for {remote}: {e}")
    #             log_message(f"SSH error for {remote}: {e}")
            
    #         if attempt < retries:
    #             wait_time = delay * (2 ** (attempt - 1))
    #             print(f"Retrying in {wait_time} seconds...")
    #             time.sleep(wait_time)
    #     print(f"SSH remote URL {remote} is not reachable after {retries} attempts.")
    #     log_message(f"SSH remote {remote} is not reachable.")

    # # Function to check HTTPS remotes
    # def check_https_remote(remote, retries=3, delay=2):
    #     headers = {"Authorization": f"token {HTTPS_TOKEN}"} if HTTPS_TOKEN else {}
    #     for attempt in range(1, retries + 1):
    #         try:
    #             response = requests.get(remote, headers=headers)
    #             if response.status_code == 200:
    #                 print(f"HTTPS remote URL {remote} is reachable.")
    #                 return
    #             else:
    #                 error_message = f"Status code {response.status_code}"
    #                 print(f"Attempt {attempt}: HTTPS error for {remote}: {error_message}")
    #                 log_message(f"HTTPS error for {remote}: {error_message}")
    #         except requests.exceptions.RequestException as e:
    #             print(f"Attempt {attempt}: HTTPS error for {remote}: {e}")
    #             log_message(f"HTTPS error for {remote}: {e}")
            
    #         if attempt < retries:
    #             wait_time = delay * (2 ** (attempt - 1))
    #             print(f"Retrying in {wait_time} seconds...")
    #             time.sleep(wait_time)
    #     print(f"HTTPS remote URL {remote} is not reachable after {retries} attempts.")
    #     log_message(f"HTTPS remote {remote} is not reachable.")

    # # Main function to check all git remotes
    # def check_git_remotes():
    #     remotes_output = subprocess.check_output(["git", "remote", "-v"]).decode("utf-8")
    #     remotes = set(line.split()[1] for line in remotes_output.strip().split("\n") if line)
        
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #         future_to_remote = {}
    #         for remote in remotes:
    #             parsed_url = urlparse(remote)
    #             if remote.startswith("git@"):  # SSH remotes
    #                 future_to_remote[executor.submit(check_ssh_remote, remote)] = remote
    #             elif parsed_url.scheme in ("http", "https"):  # HTTPS remotes
    #                 future_to_remote[executor.submit(check_https_remote, remote)] = remote
    #             else:
    #                 print(f"Unknown remote type: {remote}")
    #                 log_message(f"Unknown remote type: {remote}")
            
    #         for future in concurrent.futures.as_completed(future_to_remote):
    #             remote = future_to_remote[future]
    #             try:
    #                 future.result()
    #             except Exception as exc:
    #                 print(f"{remote} generated an exception: {exc}")
    #                 log_message(f"{remote} generated an exception: {exc}")

    # # Ensure the `requests` library is installed
    # # pip install requests

    # if __name__ == "__main__":
    #     check_git_remotes()
