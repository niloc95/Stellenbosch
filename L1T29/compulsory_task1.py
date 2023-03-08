#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T29 Compulsory Task1 \n")
# Adding new method to Course class
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("Head Office Location: Woodstock, Cape Town")

# Creating a subclass of the Course class named OOPCourse
# Creating a constructor that initialises the 
# following attributes and assigns these values:
class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print("Course Description:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        print("ID Number: #12345")

#  is a method to show inherited
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
