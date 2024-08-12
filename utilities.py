import subprocess
import os

def init():
    if not os.path.exists('.git'):
        print("Initializing new git repository")
        run_command('git init')

    folderpath = input("Enter the folder path to create the dummy repository: ")
    while not os.path.exists(folderpath):
        print("The folder path does not exist.")
        folderpath = input("Enter the folder path to create the dummy repository: ")

    os.chdir(folderpath)
    clean_repo()

    start_date = input("Enter the starting date (YYYY-MM-DD): ")
    end_date = input("Enter the ending date (YYYY-MM-DD): ")

    return start_date, end_date, folderpath

def push_to_remote():
    push_to_remote = input("Do you want to push the repository to a remote? (y/n): ")
    if push_to_remote.lower() != 'y':
        print("Exiting the script.")
        exit()
    else:
        remote_url = input("Enter the URL of the remote repository: ")
        run_command(f'git remote add origin {remote_url}')
        run_command('git push -u origin master')

def clean_repo():
    run_command('git rm -r --cached .')
    run_command('git reset --hard')
    print("All commits have been deleted.")

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')