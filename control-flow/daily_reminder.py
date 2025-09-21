task = input("Input your task here: ")
priority = input("'high', 'medium', 'low')")
time_bound = input("Is your task time-bound? (yes/no): ")

match (priority, time_bound):
    case ("high", "yes"):
        print(f" {task} is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f" {task} is a low priority task. Consider completing it when you have free time.")
    case ("medium", "yes"):
        print(f" {task} is a medium priority task that should be addressed soon.")
    case ("medium", "no"):
        print(f" {task} is a low priority task. Consider completing it when you have free time.")
    case ("low", "yes"):
        print(f" {task} is a low priority task, but it needs to be done today.")
    case ("low", "no"):
        print(f" {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input. Please enter 'high', 'medium', or 'low' for priority and 'yes' or 'no' for time-bound.")

