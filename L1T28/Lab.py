class Email:
    def __init__(self, from_address, email_contents):
        self.has_been_read = False
        self.is_spam = False
        self.email_contents = email_contents
        self.from_address = from_address

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

inbox = []

class EmailStore:
    @staticmethod
    def add_email(from_address, email_contents):
        email = Email(from_address, email_contents)
        inbox.append(email)

    @staticmethod
    def get_count():
        return len(inbox)

    @staticmethod
    def get_email(i):
        email = inbox[i]
        email.mark_as_read()
        return email.email_contents

    @staticmethod
    def get_unread_emails():
        return [email for email in inbox if not email.has_been_read]

    @staticmethod
    def get_spam_emails():
        return [email for email in inbox if email.is_spam]

    @staticmethod
    def delete(i):
        del inbox[i]

while True:
    user_input = input("What would you like to do - send/read/quit? ")
    if user_input == "send":
        from_address = input("Enter sender's email address: ")
        email_contents = input("Enter email contents: ")
        EmailStore.add_email(from_address, email_contents)
        print("Email sent!")
    elif user_input == "read":
        if EmailStore.get_count() == 0:
            print("You have no emails!")
        else:
            for i in range(EmailStore.get_count()):
                email_contents = EmailStore.get_email(i)
                print(f"From: {inbox[i].from_address}\n{email_contents}\n")
    elif user_input == "quit":
        break
    else:
        print("Invalid input. Please enter 'send', 'read', or 'quit'.")



# class Email:
#     # constructor to initialise variables
#     def __init__(self, from_address, email_contents):
#         self.has_been_read = False
#         self.email_contents = email_contents
#         self.is_spam = False
#         self.from_address = from_address

#     # method to mark email as read
#     def mark_as_read(self):
#         self.has_been_read = True

#     # method to mark email as spam
#     def mark_as_spam(self):
#         self.is_spam = True

# inbox = []

# class Inbox:
#     # method to add email to inbox
#     def add_email(self, from_address, email_contents):
#         email = Email(from_address, email_contents)
#         inbox.append(email)

#     # method to get number of messages in inbox
#     def get_count(self):
#         return len(inbox)

#     # method to get email contents at a given index
#     # mark the email as read
#     def get_email(self, i):
#         email = inbox[i]
#         email.mark_as_read()
#         return email.email_contents

#     # method to get list of unread emails
#     def get_unread_emails(self):
#         unread_emails = []
#         for email in inbox:
#             if not email.has_been_read:
#                 unread_emails.append(email)
#         return unread_emails

#     # method to get list of spam emails
#     def get_spam_emails(self):
#         spam_emails = []
#         for email in inbox:
#             if email.is_spam:
#                 spam_emails.append(email)
#         return spam_emails

#     # method to delete email at a given index
#     def delete(self, i):
#         del inbox[i]

# # create instance of Inbox class
# my_inbox = Inbox()

# # sample usage
# my_inbox.add_email("example@domain.com", "Hello World!")
# my_inbox.add_email("spam@domain.com", "Get rich quick!")
# my_inbox.get_count()  # returns 2
# my_inbox.get_email(0)  # returns "Hello World!"
# my_inbox.get_unread_emails()  # returns [Email("spam@domain.com")]
# my_inbox.get_spam_emails()  # returns [Email("spam@domain.com")]
# my_inbox.delete(0)