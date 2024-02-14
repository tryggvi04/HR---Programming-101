def collecting_grades():
    continue_str = "y"
    gradebook_dict = {}

    while continue_str == "y":
        key_input = input()
        value_input = int(input())
        continue_str = input().lower()
        
        if key_input in gradebook_dict:
            gradebook_dict[key_input].append(value_input)
        else:
            gradebook_dict[key_input] = [value_input]

    return gradebook_dict

def sort_dict(a_dict: dict):
    ''' Takes in a dictinary and sorts the keys in alphabetical order '''

    sorted_list = sorted(a_dict)
    sorted_dict = {}

    for key in sorted_list:
        sorted_dict[key] = a_dict[key]
        
    return sorted_dict



def average_grade(item):
    sum_grades = sum(item[1])
    count_grades = len(item[1])
    ave_grade = sum_grades/count_grades
    
    return (item[0], round(ave_grade, 2))


gradebook = collecting_grades()

sorted_gradebook = sort_dict(gradebook)

for item in sorted_gradebook.items():
    student, ave_grade = average_grade(item)
    print(f"{student}: {ave_grade}")
