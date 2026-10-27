#!/usr/bin/env python3

def init():

    from pathlib import Path
    if Path("doto.txt").exists():
        print("󰗖 doto.txt already exist.")
    else:
        Path("doto.txt").touch()
        print(" doto.txt have succesfully been created!")

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

    print("󰝖 Tasks from", Path.cwd().name, ":\n")
    print("╭" + "─" * (width + 8) + "╮")

    for done, desc in tasks:
        task_numbr = task_numbr+1
        stat = " " if done else "󰝦 "
        print(f"│ {task_numbr}. {stat} {desc.ljust(width)} │")

    print("╰" + "─" * (width + 8) + "╯")

def tick():

    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines()
    task_numbr = int(sys.argv[2])
    task = doto[task_numbr - 1]

    if task.startswith("x"):
        print("󰗖 The task is already marked as done.")
    else:
        doto[task_numbr - 1] = "x" + task
        Path("doto.txt").write_text("\n".join(doto) + "\n")
        print(" The task has been succesfully marked as done.")

def clean():

    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines()
    task_numbr = int(sys.argv[2])
    task = doto[task_numbr - 1]

    if task.startswith("x"):
        doto[task_numbr - 1] = task[1:]
        Path("doto.txt").write_text("\n".join(doto) + "\n", encoding="utf-8")
        print(" The task has been succesfully cleaned.")
    else:
        print("󰗖 The task isn't done yet.")

def add():
    from pathlib import Path

    with Path("doto.txt").open("a") as f:
        f.write('"'+sys.argv[2]+'"\n')
    print(" The task has been succesfully added to", Path.cwd().name)

def erase():
    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines(keepends=True)
    task_numbr = int(sys.argv[2])
    del doto[task_numbr - 1]
    Path("doto.txt").write_text("".join(doto))
    print(" The task has been succesfully erased off the list.")

def help():
    print("""
󰝖 Doto - simple per-folder todo list

 Commands:
- init             Create doto.txt in the current folder
- peek             Show the tasks
- add   <title>    Add a task
- tick  <number>   Mark a task as done
- clean <number>   Unmark a done task
- erase <number>   Delete a task

 Examples:
$ doto init
$ doto add "Bake some cookies!"
$ doto tick 1
""")

import sys

if len(sys.argv) == 1:
    help()
    sys.exit()

if sys.argv[1] == "init":
    init()
    sys.exit()

if sys.argv[1] == "peek":
    peek()
    sys.exit()

if sys.argv[1] == "tick":
    if len(sys.argv) == 3:
        tick()
        sys.exit()
    else:
        print(" Targeted task's number requiered.")
        sys.exit()

if sys.argv[1] == "clean":
    if len(sys.argv) == 3:
        clean()
        sys.exit()
    else:
        print(" Targeted task's number requiered.")
        sys.exit()

if sys.argv[1] == "add":
    if len(sys.argv) == 3:
        add()
        sys.exit()
    else:
        print(" A descritpion of the task is requiered.")
        sys.exit()

if sys.argv[1] == "erase":
    if len(sys.argv) == 3:
        erase()
        sys.exit()
    else:
        print(" Targeted task's number requiered.")
        sys.exit()
