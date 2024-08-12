import os
import random
from utilities import run_command, clean_repo, push_to_remote, init
from datetime import datetime, timedelta


def commit_suppressor():
    commit_suppressor = input("Do you want to suppress commits? (y/n): ")

    if commit_suppressor.lower() != 'y':
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
    while True:
        choice = input("Select an option:\n1. Commit Suppressor\n2. Commit Generator\n3. Push to Remote\nq. Quit\n")

        if choice == '1':
            commit_suppressor()
        elif choice == '2':
            commit_generator()
        elif choice == '3':
            push_to_remote()
        elif choice == 'q':
            exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()