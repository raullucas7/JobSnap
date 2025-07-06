import random
import sqlite3


print("Welcome to JobSnap, the easy to-use job tracker for applications!")

# connection to database -----------------------------------------------------
connect = sqlite3.connect("data/jobs.db")
cursor = connect.cursor()

# table -----------------------------------------------------
table = """
CREATE TABLE IF NOT EXISTS APPINFO (
    first_name TEXT,
    last_name TEXT,
    app_title TEXT,
    status BOOLEAN,
    company TEXT,
    email TEXT
)
"""

cursor.execute(table)
connect.commit()


# Menu Display -----------------------------------------------------
userinput = input(
""" 
What would you like to do?
              
Options: 
    1. Add Job
    2. View Job
    3. Edit Job
    4. Delete Job
    5. Exit

Enter your value here: 
""")


# Choice Handling -----------------------------------------------------

# ADD JOB
if (userinput == '1'):
    print("You are now adding a j*b")
    
    addfnameinput = input("Enter your first name: ")
    addlnameinput = input("Enter your last name: ")
    applicationtitle = input("Enter application name: ")
    statusinput = input("Have you applied or not (yes/no): ")
    if (statusinput.lower() == 'yes'):
        status_value = 1
    else:
        status_value = 2
    companyinput = input("Enter company applied to: ")
    emailinput = input("Enter your email: ")
    
    # INSERT VALUES INTO DATABASE
    queryinsert = "INSERT INTO APPINFO (first_name, last_name, app_title, status, company, email) VALUES (?,?,?,?,?,?)"
    cursor.execute(queryinsert, (addfnameinput, addlnameinput, applicationtitle, status_value, companyinput, emailinput))
    connect.commit()
    
    print("Job entry success!")



elif (userinput == '2'):
    
    print("You are now viewing a j*b")
    cursor.execute("SELECT * FROM APPINFO")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


elif (userinput == '3'):
    print("You are now editing a j*b")
    
    
    queryedit = "UPDATE APPINFO (first_name, last_name, app_title, status, company, email) VALUES (?,?,?,?,?,?)"
    
"""
elif (userinput == '4'):
    print("You are now deleting a j*b")
    
else:
    print("Exiting")
    exit()

"""
