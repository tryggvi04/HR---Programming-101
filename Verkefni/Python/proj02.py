grades = []
credits = []
weighted_average = 0
grade = 3

# söfnum saman einkunum og einingar
while grade >= 0:
    grade = float(input())
    if (grade >= 0):
        credit = int(input())
        credits.append(credit)
        grades.append(grade)

# endum forritið ef engar einkunnir voru settar inn
if not grades:
    exit()

# förum í gegnum allar einkunnir til að reikna meðaltal
if sum(credits) > 0:
    for grade, credit in zip(grades, credits):
        weighted_average += grade*credit
    weighted_average /= sum(credits)
    print("Weighted average grade:", round(weighted_average, 2))

# reiknum hæsta einkunina
maximum_grade = max(grades)
print("Highest grade:", maximum_grade)