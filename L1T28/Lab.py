class Email:
    """
    constructor to initialize variables
    """

    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

    '''
    function to mark email as read 
    '''

    def mark_as_read(self):
        self.has_been_read = True

    '''
    function to mark email as spam 
    '''

    def mark_as_spam(self):
        self.is_spam = True


inbox = []

'''
function to add email with message 
'''


def add_email(contents, email_address):
    email = Email(contents, email_address)
    inbox.append(email)


'''
method provides the count of emails within inbox
'''


def get_count():
    return len(inbox)


'''
method provides the email present the specified index
'''


def get_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        email.mark_as_read()
        print(email)
        return email
    else:
        print('Invalid index, email does not exist')


'''
method provides all unread emails
'''


def get_unread_emails():
    unread_list = []
    for i in inbox:
        if not i.has_been_read:
            unread_list.append(i)
    return unread_list


'''
method provides all spam mails
'''


def get_spam_emails():
    spam_list = []
    for i in inbox:
        if i.is_spam:
            spam_list.append(i)
            print(f"spam: {i.email_contents}")
    return spam_list


'''
method add the specified index email as spam
'''


def add_spam(index):
    messages = inbox[index]
    messages.mark_as_spam()
    print("Email added to spam")


'''
method deletes the email from inbox
'''


def delete():
    if len(inbox) > 0:
        return inbox.pop()
    else:
        print('Error, could not delete email')


# prepopulated emails with message
init_emails = [
    'Hello how are you,xyzatyahoo.in',
    'Hey! lets meet this weekend,timberleyatgmail.com'
]

for i in init_emails:
    message, email = i.split(',')
    add_email(message, email)

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":  # read email
        print("List of unread email\n")
        for i, mail in enumerate(init_emails):
            print(f'{i + 1}. {mail}')
        num = int(input("\nEnter number of email you want to read: "))
        get_email(num - 1)

    elif user_choice == "mark spam":  # spam mail marking option
        print("List of emails\n")
        for i, mail in enumerate(init_emails):
            print(f'{i}. {mail}')
        num = int(input("\nEnter number of email you want to spam :"))
        add_spam(num - 1)
        get_spam_emails()

    elif user_choice == "send":  # mail sending option
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address)
        print("Email sent successfully!")

    elif user_choice == "quit":  # quit option
        print("Goodbye")
    else:
        print("Oops - incorrect input")