

def make_formula(form: str):
    form_list = []
    for letter in form:
        if letter.isupper():
            form_list.append(letter)
        elif(letter.islower()):
            form_list[-1] += letter
    return form_list


formula_set = set()

formula_str = str(input())

formula2_str = input()

formula = make_formula(formula_str)
formula2 = make_formula(formula2_str)


intersection_set = set(formula).intersection(set(formula2))

formula_format = list(intersection_set)
formula_format = sorted(formula_format)

print(", ".join(formula_format))