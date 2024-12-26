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
    print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
else:
    print("'Read a book' is a low priority task. Consider completing it when you have free time.")