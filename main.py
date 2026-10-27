def init():
    from pathlib import Path
    if Path("doto.txt").exists():
        print("doto.txt already exist.")
    else:
        Path("doto.txt").touch()
        print("doto.txt have succesfully been created!")

def peek():
    from pathlib import Path
    doto = Path("doto.txt").read_text().splitlines()

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

def tick():
    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines()
    task = doto[0]

    if task.startswith("x"):
        print("The task is already marked as done.")
    else:
        doto[0] = "x" + task
        Path("doto.txt").write_text("\n".join(doto) + "\n", encoding="utf-8")
        print("The task has been succesfully marked as done.")

def clean():
    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines()
    task = doto[0]

    if task.startswith("x"):
        doto[0] = task[1:]
        Path("doto.txt").write_text("\n".join(doto) + "\n", encoding="utf-8")
        print("The task has been succesfully cleaned.")
    else:
        print("The task isn't done yet.")

# def add

# def erase
