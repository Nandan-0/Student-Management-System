print("===================================")
print("    STUDENT MANAGEMENT SYSTEM")
print("===================================")
print("WELCOME!")

# " create an empty list to store student records."

students = []

# " keep displaying the menu until the user exits."

while True:
    print("\n1. Add student")
    print("2. View All students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    Choice = input("Enter Your Choice (1-6): ")

# " create a dictionary containing the student information."
    
    if Choice == "1":
        print("\n-----Add student -----")

        roll = input("Enter Roll Number: ")
        Name = input("Enter student Name: ")
        Course = input("Enter course: ")
        Marks = input("Enter Marks: ")

        student = {
            "Roll": roll,
            "Name": Name,
            "Course": Course,
            "Marks": Marks
        }
    
        students.append(student)
        print("student added Succesfully")

 # " check whether any student records exits."
        
    elif Choice == "2":
         print("\n---- All students----" )
         
         if len(students) == 0:
            print("No Student Found: ")

         else:
              for Student in students:
                print("--------------------")
                print("roll Number:",Student["Roll"])
                print("Name:",Student["Name"])
                print("Course:",Student["Course"])
                print("Marks:",Student["Marks"])
                
    # " Ask for the roll number to search."            
                
    elif Choice == "3":
        print("---- Search Student ----")
        roll = input("Enter Roll Number to Search: ")
        found = False
        for student in students:
             if student["Roll"] == roll:
                print("\nstudent found!")
                print("Roll Number: ",student["Roll"])
                print("Name: ",student["Name"])
                print("Course: ",student["Course"])
                print("Marks: ",student["Marks"])
                found = True
                break
        if not found:
            print("Student not Found!")        

    # " Ask which detail the user want to update."
    
    elif Choice == "4":
        print("\n---- Update Student ----")
        roll = input("Enter Roll Number to Update: ")
        found = False
        for student in students:
            if student["Roll"] == roll:
                print("student Found!")
                print("1. Update Name")
                print("2. Update Course")
                print("3. Update Marks")

                option = input("Enter your Choice: ")
                if option == "1":
                    student["Name"] = input("Enter New Name: ")
                    print("Updated Successfully!")

                elif option == "2":
                    student["Course"] = input("Enter New Course: ")
                    print("Updated Successfully!")

                elif option == "3":
                    student["Marks"] = input("Enter New Marks: ")
                    print("Updated Successfully!")

                else:
                    print("Invalid Choice!")

                    found = True
                    break
        if not found:
            
            print("Student not Found!")          

# " find the student to be deleted."

    elif Choice == "5":
        print("\n---- Delete Student ----")
        roll = input("Enter Roll Number to Delete: ")
    
        found = False
        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break
        if not found:
            print("Student not Found!")

# " Display a closing message."
    elif Choice == "6":
        print("Thank You For Using Student Management system!")
        break

    else:
        print("Invalid Choice! Please Enter 1-6.")
     



