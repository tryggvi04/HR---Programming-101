length_stars = int(input())
views_dict = {}
for i in range(0, length_stars):
    input_data = input()
    input_data = input_data.split()
    
    name = input_data[0]
    view = int(input_data[1])
    if name in views_dict:
        views_dict[name] += view
    else:
        views_dict[name] = view
highest_views = name
for key in views_dict.keys():
    if views_dict[key] > views_dict[highest_views]:
        highest_views = key

print(highest_views)