tasks_list = []

def add_task(tasks)
  print("What task would you like to add?")
  task = input()
  tasks.append(task)
  input("Task added! Press enter to continue..")

def show_tasks(tasks):
  print("All tasks:")
  print("\n".join(tasks))

def remove_task(tasks):
  try:
    for i in range(len(tasks)):
      print(f"{i+1}. {tasks[i]}")
    print("Enter task number to remove that task.")
    task_to_remove = input()
    removed_task = tasks.pop(tasks_to_remove-1)
    input(f"Task =={removed_task}== removed successfully!")
  except:
    input(f"You must enter a number between 1 and {len(tasks+1)!}")
  
def manage_tasks():
  user_choice = -1
menu_message = """===Task List Menu===
1. Add task
2. View all tasks
3. Remove task
4. Back to main menu
"""
  while (user_choice != 4)
    try:
      
      print(menu_message)
      user_choice = int(input("Enter menu choice between 1 and 4: "))
      if (user_choice <1 or user_choice > 4):
        print("Input must be between 1 and 4!")
      else:
        if (user_choice == 1):
          add_task(tasks_list)
        if (user_choice == 2):
          show_tasks(tasks_list)
        if (user_choice == 3):
          remove_task(tasks_list)
          
    except:
      input("Input must be a number! Press enter to try again..")

  input("Returning to main menu. Press enter to continue..")
