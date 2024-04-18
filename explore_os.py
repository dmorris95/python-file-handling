#Task 1
#take user input of a directory and display contents

import os

def list_directory_contents(use_path):
    try:
        if os.path.exists(use_path):
            print(os.listdir(use_path))
        else:
            print("Sorry this path does not exist.")
    except PermissionError:
        print("Sorry you don't have permission to view this.")
    except:
        print("An error occurred please try again.")
    

#take users input of the path they want to view the directory of

#user_path = input("Please type the directory you would like to view: ")
#list_directory_contents(user_path)


#Task 2

def show_file_sizes(direct):
    try:
        if os.path.isdir(direct):
            for fname in os.listdir(direct):
                f = os.path.join(direct, fname)
                if os.path.isfile(f):
                    print(f"{f} with size of {os.path.getsize(f)} bytes")
        else:
            print("The text you input is not an existing directory.")
    except PermissionError:
        print("Sorry you don't have access to this.")
    except:
        print("An error has occured.")

#user_direct = input("Please enter the directory you would like to learn more about: ")
#show_file_sizes(user_direct)


#Task 3
#i choose 4 common extensions but also added functionality to return the occurences of the other file extensions
import re
def count_extensions(direct):
    extensions = []
    pd_count = 0
    tx_count = 0
    py_count = 0
    ex_count =0 
    misc_count = 0
    try:
        if os.path.isdir(direct):
            for f_name in os.listdir(direct):
                f = os.path.join(direct, f_name)
                if os.path.isfile(f):
                    if re.search(r"\.[.a-zA-Z]{2,}\b", f):
                        ex = (re.findall(r"\.[.a-zA-Z]{2,}\b", f,))
                        extensions.append(ex[0])
            for t in extensions:
                if t.lower() == ".pdf":
                    pd_count += 1
                elif t.lower() == ".txt":
                    tx_count += 1
                elif t.lower() == ".py":
                    py_count += 1
                elif t.lower() == ".exe":
                    ex_count += 1
                else:
                    misc_count += 1
            print(f"'.pdf' = {str(pd_count)} occurences\n'.txt' = {str(tx_count)} occurences\n'.py' = {str(py_count)} occurences\n'.exe' = {str(ex_count)} occurences\nMisc. extensions = {str(misc_count)}")
        else:
            print("That directory does not exist, please try again.")

    except PermissionError:
        print("Sorry you don't have permission to access this.")
    #except:
        #print("An error occured, please try again.")


user_dir = input("Please enter the path of the directory you would like to gather the extension counts for: ")

count_extensions(user_dir)
