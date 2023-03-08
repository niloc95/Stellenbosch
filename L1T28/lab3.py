class Email:
    # constructor to initialise variables
    def __init__(self, from_address, email_contents):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False
    # method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True
     # method to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True
    
inbox = []
# method to add email to inbox
class Inbox:
    @staticmethod 
    def add_email(from_address, email_contents):
        inbox.append(Email(from_address, email_contents))
    # method to get number of messages in inbox
    @staticmethod
    def get_count():
        return len(inbox)
    # method to get email contents at a given index
    # mark the email as read
    @staticmethod
    def get_email(index):
        email = inbox[index]
        email.mark_as_read()
        return email.email_contents
    # method to get list of unread emails
    @staticmethod
    def get_unread_emails():
        return [email for email in inbox if not email.has_been_read]
    # method to get list of spam emails
    @staticmethod
    def get_spam_emails():
        return [email for email in inbox if email.is_spam]
    # method to delete email at a given index
    @staticmethod
    def delete(index):
        del inbox[index]

# Program main 
# This code initializes a variable user_choice to an empty string and enters a while loop that runs until user_choice is equal to the string "quit".
# In each iteration of the loop, the user is prompted to enter a choice from a list of options.
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read, mark spam, delete, get count, get spam emails, send or quit?")
    if user_choice == "read":
        unread_emails = Inbox.get_unread_emails()
        if not unread_emails:
            print("No unread emails")
        else:
            for i, email in enumerate(unread_emails):
                print(f"{i}: From {email.from_address} - {email.email_contents}")
            index = int(input("Enter index of email to read: "))
            print(Inbox.get_email(index))
    elif user_choice == "mark spam":
        for i, email in enumerate(inbox):
            print(f"{i}: From {email.from_address} - {email.email_contents}")
        index = int(input("Enter index of email to mark as spam: "))
        inbox[index].mark_as_spam()
        print("Email marked as spam.")
    elif user_choice == "delete":
        for i, email in enumerate(inbox):
            print(f"{i}: From {email.from_address} - {email.email_contents}")
        index = int(input("Enter index of email to delete: "))
        Inbox.delete(index)
        print("Email deleted.")
    elif user_choice == "get count":
        print(f"There are {Inbox.get_count()} emails in the inbox.")
    elif user_choice == "get spam emails":
        spam_emails = Inbox.get_spam_emails()
        if not spam_emails:
            print("No spam emails")
        else:
            for i, email in enumerate(spam_emails):
                print(f"{i}: From {email.from_address} - {email.email_contents}")
    elif user_choice == "send":
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email contents: ")
        Inbox.add_email(from_address, email_contents)
        print("Email sent!")
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")