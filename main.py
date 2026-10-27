#!/usr/bin/env python3

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
    task_numbr = int(sys.argv[2])
    task = doto[task_numbr - 1]

    if task.startswith("x"):
        print("The task is already marked as done.")
    else:
        doto[0] = "x" + task
        Path("doto.txt").write_text("\n".join(doto) + "\n")
        print("The task has been succesfully marked as done.")

def clean():

    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines()
    task_numbr = int(sys.argv[2])
    task = doto[task_numbr - 1]

    if task.startswith("x"):
        doto[0] = task[1:]
        Path("doto.txt").write_text("\n".join(doto) + "\n", encoding="utf-8")
        print("The task has been succesfully cleaned.")
    else:
        print("The task isn't done yet.")

def add():
    from pathlib import Path

    with Path("doto.txt").open("a") as f:
        f.write('\n"'+sys.argv[2]+'"')
    print("The task has been succesfully added to", Path.cwd().name)

def erase():
    from pathlib import Path

    doto = Path("doto.txt").read_text().splitlines(keepends=True)
    task_numbr = int(sys.argv[2])
    doto[task_numbr - 1] = ""
    Path("doto.txt").write_text("".join(doto))
    print("The task has been succesfully earased off the list.")

def help():
    print("""
\033[1mdoto\033[22m - simple per-folder todo list

\033[1mUsage:\033[22m
  doto <command> [arguments]

\033[1mCommands:\033[22m
  init              Create doto.txt in the current folder
  peek, ls          Show the tasks
  add, a <title>    Add a task
  tick, t <number>  Mark a task as done
  clean, c <number> Unmark a done task
  erase, rm <number> Delete a task
  help              Show this page

\033[1mExamples:\033[22m
  doto init
  doto add "Buy bread"
  doto tick 1
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
        print("Targeted task's number requiered.")
        sys.exit()

if sys.argv[1] == "clean":
    if len(sys.argv) == 3:
        clean()
        sys.exit()
    else:
        print("Targeted task's number requiered.")
        sys.exit()

if sys.argv[1] == "add":
    if len(sys.argv) == 3:
        add()
        sys.exit()
    else:
        print("A descritpion of the task is requiered.")
        sys.exit()

if sys.argv[1] == "erase":
    if len(sys.argv) == 3:
        erase()
        sys.exit()
    else:
        print("Targeted task's number requiered.")
        sys.exit()
