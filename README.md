# Software Design
 * Assignment 2

 # Student Management System

### Overview

This repository contains a Python implementation of a simple student management system designed to manage student records efficiently. It allows users to add, update, delete, and view student information. This README provides instructions on how to run the system and highlights the changes made to the original code.


## Running the System
  
###  Prerequisites:

    Python 3.x installed on your machine.

### Steps to Run

1. Clone the Repository:

       git clone <repository-url>
       cd <repository-directory>
      
2. Run the Application: Open a terminal and execute the following command:

        python student_management_system.py

4. Follow the Menu:

   * Once the application is running, follow the on-screen menu to add, update, delete, or view student records.
    You will see the menu like this:

         Student Management System Menu:
          1. Add Student
          2. Delete Student
          3. Update Student Info
          4. View All Students
          5. Quit

## Code Changes

The code has been updated to improve efficiency, maintainability, and adheres to software design principles. Also, the refactored code provides a more efficient and maintainable implementation of the student management system. It also includes a menu-driven interface for interacting with the system.

### Class Student

* The ```update_student``` method has been replaced with the ```update``` method.
* The ```update``` method now accepts optional parameters for ```name```, ```age```, and ```major```.
* The ```display``` method has been added to display the student's information.


### Class StudentDatabase

* The ```students``` list has been replaced with a dictionary called ```_students```.
* The ```add_student``` method has been replaced with the ```add``` method.
* The ```remove_student``` method has been replaced with the ```remove``` method.
* The ```display_all_students``` method has been replaced with the ```display_all``` method.


### Class StudentManagementSystem

* The ```add_new_student``` method now accepts parameters for ```id```, ```name```, ```age```, and ```major```.
* The ```delete_student``` method now accepts a parameter for ```student_id```.
* The ```update_student_info``` method has been replaced with the ```update_student``` method.
* The ```show_all_students``` method has been replaced with the ```show_all``` method.


