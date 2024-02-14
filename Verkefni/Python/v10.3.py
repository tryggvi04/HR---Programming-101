k, bennis_bag_inp = input().split()
bag_placements = input()
bag_placements = bag_placements.split()
bennis_bag = bag_placements.index(bennis_bag_inp)+1
if bennis_bag == 1:
    print("fyrst")
elif bennis_bag == 2:
    print("naestfyrst")
else:
    print(f"{bennis_bag} fyrst")