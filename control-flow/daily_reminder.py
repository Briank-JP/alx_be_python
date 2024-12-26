task = input("enter the task description: ")
task_priority = input("what is the task priority? high/medium/low: ")
time_bound = input("is the task time bound (yes/no): ")
# use a match case
match task_priority:
    case "high":
        print()
    
    case "medium":
        print("this task can be considered")
    
    case "low":
        print()
    
    case _:
        print("invalid priority level")

if time_bound == "yes":
    print(f"Finish '{task}' is a high priority task that requires immediate attention today.!")
else:
    print(f"{task} is a low priority task, consider finishing it when you have free time.")