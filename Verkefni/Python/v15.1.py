length_chores = int(input())
chores = set()
chore_list = []

for i in range(0, length_chores):
    chore = input()

    if chore not in chores:
        print(chore)
    chores.add(chore)
