import subprocess

def quickfix_commit(message):
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', message], check=True)
    subprocess.run(['git', 'push'], check=True)

quickfix_commit("A Quick fix")