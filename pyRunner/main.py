import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--task')
args = parser.parse_args()

if args.task == "DefaultTask":
    print("Running Default Task")
elif args.task == "Task1":
    print("Running Task1")
elif args.task == "Task2":
    print("Running Task2")
elif args.task == "Task3":
    print("Running Task3")
else:
    print("No task running")
