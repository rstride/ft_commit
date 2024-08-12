import os
import subprocess
import random
from datetime import datetime, timedelta

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

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

def clean_repo():
    run_command('git rm -r --cached .')
    run_command('git reset --hard')
    print("All commits have been deleted.")

def push_to_remote():
    push_to_remote = input("Do you want to push the repository to a remote? (y/n): ")
    if push_to_remote.lower() != 'y':
        print("Exiting the script.")
        exit()
    else:
        remote_url = input("Enter the URL of the remote repository: ")
        run_command(f'git remote add origin {remote_url}')
        run_command('git push -u origin master')

def commit_generator():
    commit_generator = input("Do you want to generate commits? (y/n): ")

    if commit_generator.lower() != 'y':
        exit()
    start_date, end_date, folderpath = init()

    #Calculate the number of days between the start and end date
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    rdate = (end_date - start_date).days
    print(f"Generating commits for {rdate} days")

    for day in range(rdate):
        date = start_date + timedelta(days=day)
        commit_nb = random.randint(1, 5)
        print(f"Generating {commit_nb} commits for day {date.strftime('%Y-%m-%d')}")
        for commit_num in range(1, 5):  # 4 commits per day
            commit_time = date + timedelta(hours=commit_num * 6)  # 6-hour interval between commits
            commit_message = f"Commit {commit_num} on {date.strftime('%Y-%m-%d')}"
            
            filename = f"file_{date.strftime('%Y%m%d')}_{commit_num}.txt"
            with open(filename, 'w') as file:
                file.write(f"Dummy content for {commit_message}")
            
            run_command(f'git add {filename}')

            commit_date_str = commit_time.strftime("%a %b %d %H:%M:%S %Y %z")

            env = os.environ.copy()
            env['GIT_COMMITTER_DATE'] = commit_date_str
            command = f'git commit -m "{commit_message}" --date "{commit_date_str}"'
            run_command(command)

            print(f'Committed: {commit_message} at {commit_date_str}')

def main():
    commit_generator()
    push_to_remote()

if __name__ == "__main__":
    main()