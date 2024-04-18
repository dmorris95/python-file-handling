#Task 1

import re
def extract_emails(name_file):
    try:
        with open(name_file, 'r') as file:
            email_list = set()
            for line in file:
                if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{3,}", line):
                    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", line)
                    email_str = email[0]
                    email_list.add(email_str)
            for e in email_list:
                print(e)
    except:
        print("An error has occured, please try again.")

extract_emails("contacts.txt")