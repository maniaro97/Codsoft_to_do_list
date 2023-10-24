#!/usr/bin/env python
# coding: utf-8

# In[ ]:


to_do_list = []
while True:
    # Display menu options
    print("To-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Quit")
# Get user input
    choice = input("Enter your choice (1/2/3/4): ")
# Add a task
    if choice == '1':
        task = input("Enter a new task: ")
        to_do_list.append(task)
        print("Task added!\n")
# View tasks
    elif choice == '2':
        if len(to_do_list) == 0:
            print("Your to-do list is empty.\n")
        else:
            print("To-Do List:")
            for i, task in enumerate(to_do_list, start=1):
                print(f"{i}. {task}")
            print()
# Mark a task as done
    elif choice == '3':
        if len(to_do_list) == 0:
            print("Your to-do list is empty.\n")
        else:
            print("To-Do List:")
            for i, task in enumerate(to_do_list, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter the number of the task you want to mark as done: "))
            if task_num >= 1 and task_num <= len(to_do_list):
                to_do_list.pop(task_num - 1)
                print("Task marked as done!\n")
            else:
                print("Invalid task number. Please try again.\n")
# Quit the program
    elif choice == '4':
        break
# Handle invalid input
    else:
        print("Invalid choice. Please try again.\n")
print("Goodbye! Your to-do list is saved.")


# In[ ]:




