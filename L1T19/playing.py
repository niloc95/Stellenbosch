
# =====importing libraries===========
from datetime import date  # To get the current time

# ====Login Section====
# Open and read from user.txt file
# Save the text in list format and close the document
user_file = open('user.txt', 'r')
login_details_list = user_file.read().split()
user_file.close()

# Create empty lists that will hold the usernames and passwords info from user.txt file
usernames_list = []
passwords_list = []

# Looping through the indices of each element in the list containing the usernames and passwords
# If the index is an even number, this means it is a username, if it is odd it means it is a password
# Append the elements at these indices to one of the list according to the categories mentioned above
for i in range(len(login_details_list)):
    if i % 2 == 0:
        usernames_list.append(login_details_list[i].rstrip(','))
    else:
        passwords_list.append(login_details_list[i])

# Print a user message in a user-friendly manner
print(f'''  
    ===========================================================================
    | Welcome to the login page. Please type in your credentials to continue. |
    |      * Please note that your credentials are case sensitive *           |
    ===========================================================================
''')
# Ask user to input a username and a password
username_input = input("     Username: ")
password_input = input("     Password: ")

# While the username cannot be found in the usernames list (it is not a registered user) or the corresponding password
# saved for that username is not introduced, print an error message
while (username_input not in usernames_list) or \
        (password_input != passwords_list[usernames_list.index(username_input)]):
    print('''
    ===================================================
    | Invalid username or password, please try again! |
    ===================================================''')
    # While the conditions above take place, instruct the user to try again and get input for username and password
    username_input = input("     Username: ")
    password_input = input("     Password: ")
# Else (if credentials introduced match the data we have), print a success message for logging in
else:
    print('''
    ====================================
    | You have successfully logged in! |
    ====================================''')

# ====Menu Section====

# Create an infinite loop that will loop through the following condition
while True:

    # If user is logged in as an administrator, present a specific menu (includes statistics which are not an option
    # for non-admin users.
    # Ensure that the admin user input is converted to lower cases.
    if username_input == "admin" and password_input == passwords_list[usernames_list.index(username_input)]:
        menu = input('''
    ================================================
    |  Select one of the following Options below:  |
     R   =>   Registering a user
     S   =>   Statistics display
     A   =>   Adding a task
     VA  =>   View all tasks
     VM  =>   View my task
     E   =>   Exit
     =====>   ''').casefold()

    # Else (if user logged in is not an admin), present a menu that does not include statistics display option.
    # Ensure that the user input is converted to lower cases.
    else:
        menu = input('''
    ================================================
    |  Select one of the following Options below:  |
    
     R   =>   Registering a user
     A   =>   Adding a task
     VA  =>   View all tasks
     VM  =>   View my task
     E   =>   Exit
     =====>   ''').casefold()

    # If user(admin only as non-admin user cannot see this option) is choosing option "s"
    if menu == "s":
        # Open 'tasks.txt' file in reading mode
        # Use .readlines() function to store all the data (tasks) as a list of elements
        # Find the length of the list (number of elements in it) to find out how many tasks are currently registered
        with open('tasks.txt', 'r') as tasks_file:
            num_of_tasks = len(tasks_file.readlines())

        # Open 'user.txt' file in reading mode
        # Use .readlines() function to store all the data (username and passwords) as a list of pair elements
        # Find the length of the list (number of elements in it) to find out how many users are currently registered
        with open('user.txt', 'r') as users_file:
            num_of_users = len(users_file.readlines())

        # Print menu option title and the statistics info in a user-friendly format
        print('''
    ================
    |  Statistics  |
            ''')
        print(f'''
     Current number of tasks:     {num_of_tasks}
     Total number of users:       {num_of_users}
''')

    # Else if the user (either admin and non-admin) chose menu option 'r'
    elif menu == 'r':
        # If the user logged in is an admin, print menu option title as well as all the inputs required to register a
        # new user (username, password, password confirmation)
        if username_input == "admin" and password_input == passwords_list[usernames_list.index(username_input)]:
            print('''
    =========================
    |  Register a new user  |
    ''')
            new_username_input = input("     New username: ")
            new_password_input = input("     New user password: ")
            confirm_new_password_input = input("     Confirm new user password: ")

            # If the input for password confirmation matched the input for new user password
            # Open 'user.txt' file in append+ (read and write) format and append the new user credentials into the doc
            # Print a new user registration success message
            if new_password_input == confirm_new_password_input:
                with open('user.txt', 'a+') as users_file:
                    users_file.write(f"\n{new_username_input}, {new_password_input}")
                print('''
    ===============================================
    | You have successfully registered a new user |
    ===============================================''')
            # Else (if the two passwords introduced do not match), print an error message
            else:
                print('''
    =================================================
    | The passwords didn't match, please try again! |
    =================================================''')

        # Else (if the user logged in is not admin) print an error message informing the user that they do not have
        # access to this menu option (it is only for administrator) and continue the loop (this will display the user
        # menu again)
        else:
            print('''
    =========================================================================================
    | You do not have permission to perform this action, please contact your administrator! |
    =========================================================================================''')
            continue

    # Else if the user (either admin and non-admin) chose menu option 'a'
    # Print a menu option title
    elif menu == 'a':
        print('''
    ===================
    |  Adding a task  |
    ''')
        # Get user input for who the task will be assigned to
        # If the person that the task will be assigned to is not a user (does not have login details stored in the
        # file), print an error message and get user to input the name again
        task_username_input = input("     This task is for: ")
        while task_username_input not in usernames_list:
            print('''
    =====================================
    | User not found, please try again! |
    =====================================
    ''')
            task_username_input = input("     This task is for: ")

        # After the first step was successful (user to assign task to was found in the list), proceed to take input
        # for task title, task description and due date.
        # Set current time using the imported library (datetime) and format it in the desired way
        # Set completion status to 'No'
        task_title_input = input("     Task title: ")
        task_description_input = input("     Task description: ")
        task_due_date_input = input("     Task due (e.g. 01 Jan 2000): ")
        current_date_input = date.today().strftime("%d %b %Y")
        task_completion_status = "No"

        # If no information for username, task title, task description or due date was
        # introduced, print an error message
        if not len(task_username_input) or not len(task_title_input) or not len(task_description_input) \
                or not len(task_due_date_input):
            print('''
        ================================================================
        | All details are required for adding a task. Please try again!|
        ================================================================''')
        # Else (if all the necessary data above has been introduced)
        # Open 'tasks.txt' file in append mode and append all data into the document
        # Print a new task success message
        else:
            tasks_file = open('tasks.txt', 'a+')
            tasks_file.write(f"\n{task_username_input}, {task_title_input}, {task_description_input}, "
                             f"{task_due_date_input}, {current_date_input}, {task_completion_status}\n")
            tasks_file.close()
            print('''
    ==========================================
    | You have successfully added a new task |
    ===========================================''')

    # Else if the user (either admin and non-admin) chose menu option 'va' (or 'v a')
    # Print menu option title
    elif menu == 'va' or menu == 'v a':
        print('''
    ====================
    |  View all tasks  |''')
        # Open 'tasks.txt' file in read mode
        # For each line in the file, split the line to save the information in a list format
        # Assign the information need for display into variables using list indices
        with open('tasks.txt', 'r') as tasks_file:
            for line in tasks_file:
                line = line.split(', ')
                assigned_to = line[0]
                task = line[1]
                task_description = line[2]
                due_date = line[3]
                date_assigned = line[4]
                task_complete = line[5]

                # Print the tasks information in a friendly format - on each iteration of the for loop
                print(f'''
    ---------------------------------------------------------------------------------------------------------------
     Task:                      {task}
     Assigned to:               {assigned_to}
     Date assigned:             {date_assigned}
     Due date:                  {due_date}
     Task complete?             {task_complete}
     Task description:          {task_description}     
    ----------------------------------------------------------------------------------------------------------------''')

    # Else if the user (either admin and non-admin) chose menu option 'vm' (or 'v m')
    # Print menu option title
    elif menu == 'vm' or menu == 'v m':
        print('''
    ===================
    |  View my tasks  |''')

        # Open 'tasks.txt' file in read mode
        # For each line in the file, split the line to save the information in list format
        # If the name of the user logged in is found at the beginning of the task list (elem with index 0)
        # Save the information in this list line into variables - info that is needed to display the task details
        with open('tasks.txt', 'r') as tasks_file:
            for line in tasks_file:
                line = line.split(', ')
                if username_input == line[0]:
                    my_tasks = line
                    task = line[1]
                    task_description = line[2]
                    due_date = line[3]
                    date_assigned = line[4]
                    task_complete = line[5]
                    # Print the task details in a user friendly format on each iteration of the for loop
                    print(f'''
    ---------------------------------------------------------------------------------------------------------------
     Task:                      {task}
     Date assigned:             {date_assigned}
     Due date:                  {due_date}
     Task complete?             {task_complete}
     Task description:          {task_description}     
    ----------------------------------------------------------------------------------------------------------------''')
            # If no tasks with the username of the logged person is found, print a message
            else:
                print('''
    ====================================
    | There are no tasks in your list! |
    ====================================''')

    # Else if the user (either admin and non-admin) chose menu option 'e', print a goodbye message and exit the program
    elif menu == 'e':
        print('''
    ====================================
    | You have now logged off. Goodbye! |
    ====================================''')
        exit()

    # Else (for any other option entered) print an error message
    else:
        print('''
    ===================================================
    | Your selection does not exist. Please try again! |
    ===================================================''')


"""
NOTES:
We could also include the 'Register an user' option only in admins' menu, therefore the code could would be more logical 
and short, but I am trying to follow the instructions and my understanding is that it should be presented this way.
DOCUMENTATION: 
1. https://www.programiz.com/python-programming/datetime/current-datetime
Used to get information on how to get current date and format it to show desired output
2. HyperionDev L1T21 PDF file - structured format of the output for view my tasks and view all tasks options.
"""
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Task-Manager---HyperionDev-Bootcamp/task_manager.py at main · RamonaGherasim/Task-Manager---HyperionDev-Bootcamp