import os
from prettytable import from_csv
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

with open("project.csv") as fp:
    project = from_csv(fp)

print("""This is a project manager.
You can add, delete, edit, and sort project.""")
sleep(1)
while True:
    try:
        print(project)
        print("""
1. Add project
2. Delete project
3. Edit project
4. Sort project
5. Exit
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Edit project")
            print(project)
            edit_project = int(input("Project number you want to edit: "))
            editproject = edit_project - 1
            project_name = input("Project name: ")
            status = input("Status: ")
            language = input("Language: ")
            about = input("About: ")
            project.del_row(editproject)
            project.del_column("No.")
            project.add_row([project_name, status, language, about])
            project.add_autoindex("No.")
            print("Editing project...")
            sleep(0.5)
            print("Project edited")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sort project")
            print(project)
            project.add_autoindex("No.")
            print("""
1. Sort by project name
2. Sort by status
3. Sort by language
4. Sort by about
""")
            project.del_column("No.")
            sort_project = input("Sort by: ")
            if sort_project == "1":
                project.sortby = "Project Name"
                print("Sorting project...")
                sleep(0.5)
                print("Project sorted")
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif sort_project == "2":
                project.sortby = "Status"
                print("Sorting project...")
                sleep(0.5)
                print("Project sorted")
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif sort_project == "3":
                project.sortby = "Language"
                print("Sorting project...")
                sleep(0.5)
                print("Project sorted")
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif sort_project == "4":
                project.sortby = "About"
                print("Sorting project...")
                sleep(0.5)
                print("Project sorted")
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Wrong choice")
                os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == 5:
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
