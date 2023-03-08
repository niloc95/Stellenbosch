#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T28 Compulsory Task1  'email.py' \n")
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
    @staticmethod # Refrenece Sources
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
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read or mark spam or send or quit?")
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
    elif user_choice == "send":
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email contents: ")
        Inbox.add_email(from_address, email_contents)
        print("Email sent!")
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")

#Refrenece Sources
# 1. https://www.geeksforgeeks.org/python-staticmethod/
# 2. https://stackoverflow.com/questions/23508248/why-do-we-use-staticmethod
# 3. https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
