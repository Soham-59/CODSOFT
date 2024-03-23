
tasks=[]
def addtask():
     
    task=input("Enter A New Task:")
    tasks.append(task)
    print("Task Added Successfully !")

def showtask():
     if len(tasks)==0:
        print("No Tasks.")
     else:
          print("\nTask List=")
          for i,task in enumerate(tasks):
               print(f'{i+1}.{task}')

def delete_task():
    
    if len(tasks)==0:
        print("No Tasks !")
    else:
         print("\nTasks\n")
         for i,task in enumerate(tasks):
             print(f'{i+1}.{tasks[i]}')
         choice_num=int(input("Enter a (task number-1) to delete :"))
         if choice_num>=0 & choice_num<=(len(tasks)-1):
             del tasks[choice_num]
             print("Task successfully Deleted.")
         else:
              print("Invalid Task Number.")
              
             

while True:
     print("--------- To DO LIST APPLICATION------------")
     print("1.Add Task")
     print("2.Show Task List")
     print("3.Delete Task")

     choice=int(input("Enter a number for Operation:"))
     if choice==1:
          addtask()
     elif choice==2:
          showtask()
     elif choice==3:
          delete_task()
     else:
          print("Invalid Choice")
          break 