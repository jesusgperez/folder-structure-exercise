# Folder Structure Application

This is a command line application for the folder structure interview problem


## How to use it
In the command console type the following command:
  * python3 main.py

And this will start the application, you are going to have 5 options:
    * CREATE <path>: Creates a new folder
    * LIST: Lists the current folder structure
    * MOVE <path_from> <path_to>: Moves a given folder to another place
    * DELETE <path>: Deletes a given folder
    * EXIT: exit the application

The program will guide you through the process and will tell you whether a path is valid or not in the application

## Structure
It uses a validators objects to validate the input data from the command line

There is an implementation of Builder design pattern for the Folder Structure object to create the object step by step

As well to preserve the Single Responsibility principle I created a different object to persist the data in a file that's called: tree.txt

In data there are some variables that server as setting variables and an object to model the command options
