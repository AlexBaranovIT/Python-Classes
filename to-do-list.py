class TodoList:
 
 def __init__(self):
  self.tasks = []
  
 def add_task(self, task):
  self.tasks.append(task)
  
 def remove_task(self, task_to_remove):
  if task_to_remove in self.tasks:
   self.tasks.remove(task_to_remove)
   print("Task", task_to_remove, "has been deleted")
  else:
   print(f"Task {task_to_remove}not found in list")
   
 def show_tasks(self):
  print("Tasks that you have:" ,self.tasks)
  
 def clear_tasks(self):
  self.tasks = []
  print("Now there are no tasks")
  
 def get_task_count(self):
  print("Tasks count:", len(self.tasks))
 
  
user1 = TodoList()

user1.add_task("check email")

user1.add_task("clean the room")

user1.remove_task("check email")

user1.show_tasks()

user1.get_task_count()
