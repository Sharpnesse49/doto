def init():
    from pathlib import Path
    if Path("doto.txt").exists():
        print("doto.txt already exist.")
    else:
        Path("doto.txt").touch()
        print("doto.txt have succesfully been created!")

def peek():
    from pathlib import Path
    with open("doto.txt") as f:
         doto = f.readlines()

    tasks = []
    for task in doto:
        if task.strip() == "":
            continue
        done = task.startswith("x")
        desc = task[task.index('"') + 1 : task.rindex('"')]
        tasks.append((done, desc))

    width = max(len(desc) for done, desc in tasks)
    task_numbr = 0

    print("\n\033[1mTasks from", Path.cwd().name, ":\033[22m")
    print("╭" + "─" * (width + 8) + "╮")

    for done, desc in tasks:
        task_numbr = task_numbr+1
        stat = " " if done else " "
        print(f"│ {task_numbr}. {stat} {desc.ljust(width)} │")

    print("╰" + "─" * (width + 8) + "╯")

# def flip

# def add

# def drop
