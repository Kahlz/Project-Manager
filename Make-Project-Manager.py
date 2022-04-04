import os
from prettytable import PrettyTable
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

project = PrettyTable()
project.field_names = ["Project Name", "Status", "Language", "About"]
project.add_autoindex("No.")

print("""This is a project manager.
You can add and delete project.""")
sleep(1)
while True:
    try:
        print(project)
        print("""
1. Add project
2. Delete project
3. Exit
""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Add project")
            print(project)
            project_name = input("Project name: ")
            status = input("Status: ")
            language = input("Language: ")
            about = input("About: ")
            project.del_column("No.")
            project.add_row([project_name, status, language, about])
            project.add_autoindex("No.")
            print("Adding project...")
            sleep(0.5)
            print("Project added")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Delete project")
            print(project)
            delete_project = int(input("Project number you want to delete: "))
            delproject = delete_project - 1
            project.del_row(delproject)
            print("Deleting project")
            sleep(0.5)
            print("Project deleted")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == 3:
            print("Exit")
            raw = project.get_string()
            data = [tuple(filter(None, map(str.strip, splitline)))
                    for line in raw.splitlines()
                    for splitline in [line.split('|')] if len(splitline) > 1]
            if project.title is not None:
                data = data[1:]
            with open('project.csv', 'w') as f:
                for d in data:
                    f.write('{}\n'.format(','.join(d)))
            break
        else:
            print("Wrong choice")
            os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError:
        print("Wrong choice")
        os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print("Exit")
        raw = project.get_string()
        data = [tuple(filter(None, map(str.strip, splitline)))
                for line in raw.splitlines()
                for splitline in [line.split('|')] if len(splitline) > 1]
        if project.title is not None:
            data = data[1:]
        with open('project.csv', 'w') as f:
            for d in data:
                f.write('{}\n'.format(','.join(d)))
        break
