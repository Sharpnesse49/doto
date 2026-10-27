with open("doto.txt") as f:
    doto = f.readlines()

tasks = []
for task in doto:
    if task.strip() == "":
        continue
    done = task.startswith("x")
    desc = task[task.index('"') + 1 : task.rindex('"')]
    tasks.append((done, desc))

largeur = max(len(desc) for done, desc in tasks)
task_numbr = 0

print("\n\033[1mTasks from doto :\033[22m")
print("╭" + "─" * (largeur + 8) + "╮")

for done, desc in tasks:
    task_numbr = task_numbr+1
    stat = " " if done else " "
    print(f"│ {task_numbr}. {stat} {desc.ljust(largeur)} │")

print("╰" + "─" * (largeur + 8) + "╯")
