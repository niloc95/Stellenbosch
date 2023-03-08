#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T24 Compulsory Task2 'Task_manager.py' \n")

# =====Importing libraries===========
import datetime
from datetime import date  # To get the current date
from collections import Counter  # To find the number of tasks for each user
import os  # To check if text files are empty


# # ====Functions====

# Defining the function that will register a new user
def reg_user():
    """
    This function check if the user logged in is an admin. If the user is an admin, 
    the function prints the menu option title as well as the input for a new username. 
    If that username already exists, the function prints an error message and asks the user for a username input again. 
    When a correct new username is inputted, the function asks for password and password confirmation.
    """
    if username_input == "admin" and password_input == passwords_list[usernames_list.index(username_input)]:
        print('''
    =========================
    |  Register a new user  |
    ''')
        new_username_input = input("     New username: ")

        while new_username_input in usernames_list:
            print('''
    ====================================================
    |  This username already exists, please try again  |
    ====================================================
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


# Defining the function that will add a task
def add_task():
    # Print a menu option title
    print('''
    ===================
    |  Adding a task  |
    ''')
    # Get user input for whom the task will be assigned to
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

    # If no information for username, task title, task description or due date was introduced, print an error message
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
                         f"{current_date_input}, {task_due_date_input}, {task_completion_status}")
        tasks_file.close()
        print('''
    ==========================================
    | You have successfully added a new task |
    ===========================================''')


# Defining the function that will show all the tasks
def view_all_tasks():
    # Print menu option title
    print('''
    ====================
    |  View all tasks  |''')
    # Open 'tasks.txt' file in read mode
    # For each line in the file, split the line to save the information in a list format
    # Assign the information need for display into variables using list indices
    content = open('tasks.txt', 'r')
    contents = content.readlines()
    content.close()
    for line in contents:
        assigned_to, task, task_description, date_assigned, due_date, task_complete = line.split(", ")
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


# Defining the function that will show user's tasks
def view_my_tasks():
    # Print menu option title
    print('''
    ===================
    |  View my tasks  |''')

    # Open 'tasks.txt' file in read mode
    # For each line in the file, split the line to save the information in list format
    # Keep the task number (count) in a list of tasks numbers
    # If the name of the user logged in is found at the beginning of the task list (elem with index 0)
    # Save the task number in the list
    with open('tasks.txt', 'r+') as tasks_file_content:
        tasks_file = tasks_file_content.readlines()
        my_tasks_num = []
        for count, line in enumerate(tasks_file):
            line = line.strip("\n").split(', ')
            # If the user that is logged in is the same as the user the task has been assigned to (element at index 0 in
            # the line)
            # Save the information in this list line into variables - info that is needed to display the task details
            if username_input == line[0]:
                my_tasks_num.append(count)
                assigned_to = line[0]
                task_title = line[1]
                task_description = line[2]
                due_date = line[4]
                date_assigned = line[3]
                task_complete = line[5].strip("\n")
                # Print the task details in a user friendly format on each iteration of the for loop
                print(f'''
    ---------------------------------------------------------------------------------------------------------------
     Task number {count}
     Task:                      {task_title}
     Assigned to:               {assigned_to}
     Date assigned:             {date_assigned}
     Due date:                  {due_date}
     Task complete?             {task_complete}
     Task description:          {task_description}
    ----------------------------------------------------------------------------------------------------------------''')

            # Continue displaying all tasks until the end of iteration
            if count != len(tasks_file)-1:
                continue

            # Else if there are no tasks assigned to the user that is logged in, print a message and break the loop
            elif not len(my_tasks_num):
                print('''
    ====================================
    | There are no tasks in your list! |
    ====================================''')
                break

            # Otherwise get user to input a number to selecct one of his tasks or type -1 to return to the main menu
            else:
                task_num_input = int(input('''
    =====================================================================================
    |  Enter a task number to select a specific task or -1 to return to the main menu:  |
    ==> '''))

                # If user inputs -1, return to the main menu
                if task_num_input == -1:
                    return

                # Else if the user inputs a number that represents one of his tasks
                # Ask the user to select if they would like to mark or edit the task
                elif task_num_input in my_tasks_num:
                    line = tasks_file[task_num_input].strip("\n").split(", ")
                    mark_or_edit = input(f'''
    ================================================
    |  Please select one of the following options  |
     C   =>   Mark the task number as complete
     E   =>   Edit task
     =====>   ''').casefold()

                    # If user chooses to mark the task as complete, the element at index 5 in the line will become "Yes"
                    # thus marking the task as complete. Print a success message
                    if mark_or_edit == 'c':
                        line[5] = "Yes"
                        print(f'''
    ===================================================
    | Task has been successfully marked as completed! |
    ===================================================
''')

                    # Else if the uses chooses to edit the task, and the task is not complete
                    # Display the editing options the user has
                    elif mark_or_edit == 'e' and line[5] != "Yes":
                        edit_user_or_due_date = input(f'''
    ================================================
    |  Please select one of the following options  |
     UE   =>   Assign this task to another user
     DDE  =>   Edit this task's due date
     ======>   ''').casefold()

                        # If user chooses to assign task to another user
                        # Get user to input who to assign this to
                        # If the assigned user is an existing user, the user name in the task will become the ones that
                        # has been inputted
                        # If the input user does not exist, print an error message
                        if edit_user_or_due_date == "ue":
                            assign_task_to_new_user = input(f'''
    Assign this task to: ''')
                            if assign_task_to_new_user in usernames_list:
                                line[0] = assign_task_to_new_user
                                print(f'''
    ========================================================
    | Task has been successfully assigned to another user! |
    ========================================================
''')
                            else:
                                print(f'''
    ===============================================
    | This is not a valid user. Please try again. |
    ===============================================
''')

                        # Else if user chooses to change the due date of the task
                        # Get user to input the new due date
                        # Due date (element at index 4 in the line) will become the date the user has inputted
                        elif edit_user_or_due_date == "dde":
                            new_due_date = input(f'''
    New task due date (e.g. 01 Jan 2000): ''')
                            line[4] = new_due_date
                            print(f'''
    =======================================
    | Task due date changed successfully! |
    =======================================
                            ''')

                    # Else if user chooses to edit the task but the task has been marked as completed, print an error
                    # message stating that only uncompleted tasks can be edited
                    elif mark_or_edit == "e" and line[5] == "Yes":
                        print(f'''
    ======================================================
    |              This task is complete.                |
    | You can only edit tasks that are not complete yet. |
    ======================================================''')

                    # Otherwise, if user inputs any other option, print an error message
                    else:
                        print(f'''
    =====================================
    | Invalid option, please try again. |
    =====================================''')

                    # Define a variable that will become a line that includes the changes the user has made to the task
                    to_replace = f'{line[0]}, ' \
                                 f'{line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}\n'
                    # Open tasks.txt file in writing mode
                    # For all the lines in the task file, if a line has suffered changed mentioned above, overwrite that
                    # line with the new information
                    # Otherwise, just re-write the line as it was
                    with open("tasks.txt", "w") as file:
                        for i in range(len(tasks_file)):
                            if i == task_num_input:
                                file.write(to_replace)
                            else:
                                file.write(f'{tasks_file[i]}')


# Defining the function that will show the statistics
def show_stats():
    """
    If the user logged in is an admin, this function will display the information from 'task_overview.txt' and
    'user_overview.txt'. Otherwise it will display an error message
    """
    if username_input == "admin" and password_input == passwords_list[usernames_list.index(username_input)]:

        # Check if any of the text files are empty or not
        # If a text file is empty, run the generate_reports() function
        # Open 'task_overview.txt' and "user_overview.txt' files in reading mode
        # Read all the information from each file and display it under the "Statistics" title
        if os.path.getsize("user_overview.txt") == 0 or os.path.getsize("task_overview.txt") == 0:
            generate_reports()
        with open("task_overview.txt", "r") as task_overview_file:
            task_overview = task_overview_file.read()
        with open("user_overview.txt", "r") as user_overview_file:
            user_overview = user_overview_file.read()
        print(f'''
    ================
    |  Statistics  |
     {task_overview}
     
     
     {user_overview}''')

    # Else (if the user logged in is not admin) print an error message informing the user that they do not have
    # access to this menu option (it is only for administrator)
    else:
        print('''
    =========================================================================================
    | You do not have permission to perform this action, please contact your administrator! |
    =========================================================================================''')


# Defining the function that will generate reports
def generate_reports():
    # Open tasks file in reading mode and read all lines in the file
    # Calculate the total tasks recorder as the length of the list of tasks created
    # Define variables for completed tasks, uncompleted tasks and overdue tasks and set these to 0
    # Also create an empty list that will hold all the users that had tasks assigned to them
    with open('tasks.txt', 'r') as tasks_file_content:
        tasks_file = tasks_file_content.readlines()
        num_tasks_recorded = len(tasks_file)
        num_tasks_completed = 0
        num_tasks_uncompleted = 0
        num_tasks_uncompleted_overdue = 0
        user_assigned_list = []

        # For each line in the file, split it by comma space to create a list
        # Append each user name (elem at index 0 in the line) to the empty users list created above
        for line in tasks_file:
            line = line.strip().split(", ")
            user_assigned_list.append(line[0])
            completed = line[5]
            # If the task is complete, increase the value for completed task by 1 on each iteration
            if completed == "Yes":
                num_tasks_completed += 1

            # Otherwise (if the task is not marked as completed)
            # Increase the value for uncompleted tasks by 1 on each iteration
            # Get the current date (today's date) and the task's due date (represented by elem at index 4 in the list)
            # Create a date object from the due date string and store it in the desired format
            else:
                num_tasks_uncompleted += 1
                current_date = datetime.datetime.today()
                due_date_str = line[4]
                due_date_obj = datetime.datetime.strptime(due_date_str, "%d %b %Y")
                # If the current date is bigger than the task's due date object
                # Increase the value for overdue tasks by 1 on each iteration
                if current_date > due_date_obj:
                    num_tasks_uncompleted_overdue += 1

        # Calculate the percentage of uncompleted and the percentage of overdue tasks as uncompleted tasks
        # (overdue respectively) divided by total number of tasks recorder times one hundred
        percentage_tasks_uncompleted = round(num_tasks_uncompleted / num_tasks_recorded * 100, 2)
        percentage_tasks_overdue = round(num_tasks_uncompleted_overdue / num_tasks_recorded * 100, 2)

    # Open the task overview file in writing mode (or create and open if this does not exist yet)
    # Write all the information gathered above
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f'''{"Task Overview:":^50}
    Total number of tasks recorder:                       {num_tasks_recorded}
    Total number of completed tasks:                      {num_tasks_completed}
    Total number of asks that haven't been completed:     {num_tasks_uncompleted}
    Total number of tasks that haven't been completed 
    and are now overdue:                                  {num_tasks_uncompleted_overdue}
    The percentage of tasks that are incomplete:          {percentage_tasks_uncompleted}%
    The percentage of tasks that are overdue:             {percentage_tasks_overdue}%
''')

    # Open the user file in read mode and read all the lines.
    # Get the number of users registered as the length of the list of lines created
    with open('user.txt', 'r') as users_file_content:
        users_file = users_file_content.readlines()
        num_users_registered = len(users_file)

    # Open the task overview file in writing mode (or create and open if this does not exist yet)
    # Write the information about users registered and task recorded in a user-friendly format.
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f'''{"User Overview:":^50}
    Total number of users registered:                     {num_users_registered}
    Total number of tasks recorder:                       {num_tasks_recorded}\n
''')
    # Count how many tasks are assigned to each user with function counter. This will also create a dictionary that
    # will have the usernames as keys and the frequency of that name as the value
    num_tasks_per_user = Counter(user_assigned_list)

    # For each key and value in the dictionary created above
    # Set the username as the key, the num of tasks per user as the value
    # Calculate the percentage of tasks assigned to each user out of the total number of tasks recorded
    # Set the completed tasks and overdue tasks to 0
    for key, value in num_tasks_per_user.items():
        user_name = key
        user_num_tasks = value
        user_task_percentage = round(user_num_tasks / num_tasks_recorded * 100, 2)
        user_num_task_completed = 0
        user_num_tasks_uncompleted_overdue = 0

        # For each line in the task file, create a list by splitting the line at comma space
        for line in tasks_file:
            line = line.split(", ")

            # For each username iteration, find the task that has been assigned to that user
            if line[0].strip("\n") == user_name:
                # If the task is marked as completed (elem at index 5 in the line has the value of 'Yes')
                # Increase the number of completed tasks by 1
                if line[5].strip("\n") == "Yes":
                    user_num_task_completed += 1
                # Otherwise (if the task is not marked as completed)
                # Get the current date (today's date) and the task's due date (represented by elem at index 4 in the
                # list)
                # Create a date object from the due date string and store it in the desired format
                else:
                    current_date = datetime.datetime.today()
                    due_date_str = line[4]
                    due_date_obj = datetime.datetime.strptime(due_date_str, "%d %b %Y")

                    # If the current date is bigger than the task's due date object
                    # Increase the value for overdue tasks by 1 on each iteration
                    if current_date > due_date_obj:
                        user_num_tasks_uncompleted_overdue += 1

        # Caculate the perccentage of tasks the user has completed out of all the tasks assigned to that user
        # Find the percentage of tasks the user has not completed by subtracting the percentage of completed tasks from
        # 100%
        # # Find the percentage of tasks the user has not completed and are overdue
        user_task_percentage_completed = round(user_num_task_completed / user_num_tasks * 100, 2)
        user_task_percentage_uncompleted = 100 - user_task_percentage_completed
        user_task_percentage_overdue = round(user_num_tasks_uncompleted_overdue / user_num_tasks * 100, 2)

        # Open the user overview file in writing mode (or create and open if this does not exist yet)
        # Write all the information gathered above in a user-friendly format
        with open("user_overview.txt", "a") as user_overview:
            user_overview.write(f'''    {user_name.title()}
            {user_name.title()} has been assigned {user_num_tasks} tasks.
            This represents {user_task_percentage}% of all tasks.
            {user_name.title()} has completed {user_task_percentage_completed}% of their tasks.
            {user_name.title()} must still complete {user_task_percentage_uncompleted}% of their tasks.
            {user_task_percentage_overdue}% of {user_name.title()}'s tasks are incomplete and now overdue.
        ''')
            user_overview.write("\n")

    # Print success message
    print(f'''
    =================================================
    | Two reports have been successfully generated! |
    =================================================
    ''')


# ====Login Section====
# Open and read from user.txt file
# Save the contents in list format
# Create empty lists that will hold the usernames and passwords info from user.txt file
# Looping through each line in the file, strip the lines of the escape character \n
# Then split each line by ", " to get the username and password. We know that username is the fist part of the line,
# and the password is the second part.
# Append the usernames and the passwords to the empty lists accordingly
with open('user.txt', 'r') as user_file:
    user_contents = user_file.readlines()
    usernames_list = []
    passwords_list = []
    for line in user_contents:
        username, password = line.strip("\n").split(", ")
        usernames_list.append(username)
        passwords_list.append(password)

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
    # Display menu options and get user to input a choice for an option from the menu
    # Ensure that the admin user input is converted to lower cases.
    menu = input('''
    ================================================
    |  Select one of the following Options below:  |
     R   =>   Registering a user
     DS  =>   Display Statistics
     A   =>   Adding a task
     VA  =>   View all tasks
     VM  =>   View my task
     GR  =>   Generate reports
     E   =>   Exit
     =====>   ''').casefold()

    # If the user (either admin and non-admin) is choosing option 'ds' (or 'd s'), call show_stats function
    if menu == "ds" or menu == "d s":
        show_stats()

    # Else if the user (either admin and non-admin) chose menu option 'r', call reg_user function
    elif menu == 'r':
        reg_user()
        continue

    # Else if the user (either admin and non-admin) chose menu option 'a', call add_task function
    elif menu == 'a':
        add_task()

    # Else if the user (either admin and non-admin) chose menu option 'va' (or 'v a'), call view_all_tasks function
    elif menu == 'va' or menu == 'v a':
        view_all_tasks()

    # Else if the user (either admin and non-admin) chose menu option 'vm' (or 'v m'), call view_my_tasks function
    elif menu == 'vm' or menu == 'v m':
        view_my_tasks()

    # Else if the user (either admin and non-admin) chose menu option 'gr' (or 'g r'), call generate_reports function
    elif menu == "gr" or menu == "g r":
        generate_reports()

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