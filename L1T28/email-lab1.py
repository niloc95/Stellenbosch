class Email:
    # constructor to initialise variables
    def __init__(self, from_address, email_contents):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
    # method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True
    # method to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True

inbox = []
# method to add email to inbox
def add_email(from_address, email_contents):
    inbox.append(Email(from_address, email_contents))
# method to get number of messages in inbox
def get_count():
    return len(inbox)
# method to get email contents at a given index
# mark the email as read
def get_email(i):
    email = inbox[i]
    email.mark_as_read()
    return email.email_contents
# method to get list of unread emails
def get_unread_emails():
    return [email for email in inbox if not email.has_been_read]
# method to get list of spam emails
def get_spam_emails():
    return [email for email in inbox if email.is_spam]
# method to delete email at a given index
def delete(i):
    del inbox[i]

while True:
    action = input("Do you want to send an email (s), read your emails (r), or quit (q)? ")

    if action == "s":
        from_address = input("Enter sender email address: ")
        email_contents = input("Enter email contents: ")
        add_email(from_address, email_contents)
        print("Email sent!")

    elif action == "r":
        if len(inbox) == 0:
            print("You have no messages.")
        else:
            for i in range(len(inbox)):
                email = inbox[i]
                print(f"From: {email.from_address}\nContents: {email.email_contents}")
                email.mark_as_read()
                print()
            print(f"You have {len(get_unread_emails())} unread messages and {len(get_spam_emails())} spam messages.")
            delete_choice = input("Do you want to delete any messages (y/n)? ")
            if delete_choice == "y":
                delete_indices = input("Enter the indices of the messages you want to delete, separated by commas: ")
                delete_indices = [int(i) for i in delete_indices.split(",")]
                delete_indices.sort(reverse=True)
                for i in delete_indices:
                    delete(i)

    elif action == "q":
        break

    else:
        print("Invalid input. Try again.")