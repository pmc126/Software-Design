# Software Design principles - Assignment 2

## Student Management System

### Overview

This repository contains a Python implementation of a simple student management system designed to manage student records efficiently. It allows users to add, update, delete, and view student information. This README provides instructions on how to run the system and highlights the changes made to the original code.


## Running the System
  
###  Prerequisites:

    Python 3.x installed on your machine.
  Ensure Python is installed on your PC. You can download it from the [official Python website](https://www.python.org/downloads/)

### Steps to Run

- Clone the Repository:

       git clone https://github.com/pmc126/Software-Design.git
       cd <repository-directory>
      
2. Run the Application: Open a terminal navigate to the directory where the script is located and execute the following command:

        python student_Management_System.py

4. Follow the Menu:
  - Once the application is running, follow the on-screen menu to add, update, delete, or view student records. You will see the menu like this:

         Student Management System Menu:
          1. Add Student
          2. Delete Student
          3. Update Student Info
          4. View All Students
          5. Quit
 - Enter the number corresponding to your choice and follow the prompts.

## Code Changes

The Student Management System has been updated to improve its efficiency, maintainability, and adherence to software design principles. The refactored code provides a more efficient and maintainable implementation of the student management system and includes a menu-driven interface for interacting with the system.

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

### menu method
  * The ```menu``` was added for users to interact with the system.

