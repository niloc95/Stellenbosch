#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T19 Compulsory Task1+2 'Task_manager.py' \n")
# =====importing libraries===========
# To record current date and time
from datetime import date 

# ====Login Section====
# Open and read the user.txt
user_read_file = open ('user.txt', 'r')
login_data = user_read_file.read().split()
user_read_file.close()

# List to store the usernames and passwords

username_list = []
password_list = []

for i in range(len(login_data)):
    if i % 2 == 0:
        username_list.append(login_data[i].rstrip(','))
    else:
        password_list.append(login_data[i])

print(f'''\033[1m
    =======================================================
    ===== Capstone Projects | Task Management Console =====\033[0m
    =====          Please Sign in below               ===== 
    =====          Sign is case senitive              =====
    =======================================================
    ''')

# Prompt user for sign details
username = input('Please enter your username: ')
password = input('Please enter your password: ')

# While username or password cannot be found in file, printed retry message. 
while (username not in username_list) or \
        (password != password_list[username_list.index(username)]):
        print('''
    ===================================================
    \033[1m    Oh no incorrect details, please try again!\033[0m
    ===================================================''')
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
else: 
    print('''
    ====================================
             Login successfully 
    ====================================''')
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.

# Menu Section
while True: 

    if username == "admin" and password == password_list[username_list.index(username)]:
        menu = input('''
    ==========================================
    Select one of the following Options below:
    ==========================================
        r - Registering a user
        s - Statistics
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
     =====>: ''').lower()
    
    else: 
        menu = input('''
    ================================================
        Select one of the following Options below:
    ================================================
     r - Registering a user
     a - Adding a task
     va - View all tasks
     vm - view my task
     e - Exit
     =====>: ''').lower()
     
    if menu == 's':
        with open ('tasks.txt', 'r') as tasks_file:
            list_num_task = len(tasks_file.readlines())
        
        with open ('user.txt', 'r') as users_file:
            list_num_users = len(users_file.readlines())
        print('''
        -----------------------------
                    Statistics
        -----------------------------
        ''')
        print(f'''
         Current number of task:  {list_num_task}
         Curent number of users:  {list_num_users}
        ''')
    elif menu == 'r':
               
        if username == "admin" and password == password_list[username_list.index(username)]:
            print('''
            ===========================================
                       Lets Register a new user
            ===========================================
            ''') 
            new_username = input('Please enter a new name: ')
            new_password = input('Please enter a new password: ')
            confirm_new_password = input ('Please confirm the password: ')
            if new_password == confirm_new_password:
                with open('user.txt', 'a+') as users_file:
                    users_file.write(f"\n{new_username}, {new_password}")
                print('''
    ===============================================
           New user successfully registered 
    ===============================================''')
            # Else (if the two passwords introduced do not match), print an error message
            else:
                print('''
    =================================================
    | The passwords didn't match, please try again! |
    =================================================''')
        else: 
            print('''
        =========================================================================
             Sorry! administrator privileges are required to perform this task
        =========================================================================''')
            continue

    elif menu == 'a':
        print(''' 
            =======================
                Lets add a task
            =======================''')
        task_username = input('Task for, who must do the task ==>: ')
        while task_username not in username_list:
            print('''
            =================================================
                  Let's try again user not found!
            =================================================''')
            task_username = input('Task for: ')

        task_name = input(' Task name: ')
        task_desc = input(' Task description: ')
        task_due = input(' Task due date: ')
        current_date = date.today().strftime("%d %b %Y")
        task_completion = "No"

        if not len(task_username) or not len(task_name) or not len(task_desc) \
                    or not len(task_due):
            print('''
        ======================================================
            Please enter all the task items, Lets try again! 
        ======================================================''')
        else: 
            tasks_file = open('tasks.txt', 'a+')
            tasks_file.write(f'\n{task_username}, {task_name}, {task_desc}, {task_due}, {current_date}, {task_completion}')
            tasks_file.close()
            print('''
                *****************************************************
                            New task successfully added
                *****************************************************''')
    
    elif menu == 'va':
       print(''' 
        *********************************************
                    Lets view all tasks
        *********************************************''')
       with open ('tasks.txt', 'r') as tasks_file:
            for line in tasks_file:
                line = line.split(', ')
                assignee = line[0]
                task = line[1]
                task_descsription = line[2]
                date_due = line[3]
                assigned = line[4]
                complete_task = line[5]

                print(f'''
                -------------------------------------------------------------------------------------------------------------------------------------                                                                                     
                -   Task Item:              {task}                                                                                                  
                -   Task Assignee:          {assignee}                                                                                              
                -   Date Assigned:          {assigned}                                                                                              
                -   Due Date:               {date_due}                                                                                              
                -   Task Complete Status:   {complete_task}                                                                                         
                -   Task Description:       {task_descsription}
                -------------------------------------------------------------------------------------------------------------------------------------''')

    elif menu == 'vm':
        print(''' 
    *********************************************
                View all tasks
    *********************************************''')
        
        with open ('tasks.txt', 'r') as tasks_file:
            for line in tasks_file:
                line = line.split(', ')
                if username == line[0]:
                    my_tasks = line
                    task = line[1]
                    task_descsription = line[2]
                    date_due = line[3]
                    assigned = line[4]
                    complete_task = line[5]

                print(f'''
                -------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                 
                -   Task Item:              {task}                                                                                                                                                                                          
                -   Date Assigned:          {assigned}                                                                                              
                -   Due Date:               {date_due}                                                                                              
                -   Task Complete Status:   {complete_task}                                                                                         
                -   Task Description:       {task_descsription}
                -------------------------------------------------------------------------------------------------------------------------------------''')
            else: 
                print('''
            ====================================  
              No more tasks available for you
            ====================================''')        

    elif menu == 'e':
        print('Goodbye!!!😀')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")