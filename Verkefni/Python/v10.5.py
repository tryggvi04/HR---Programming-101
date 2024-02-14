def heimavinna(a_str: str):
    homework_count = 0
    homework_list = a_str.split(";")
    for item in homework_list:
        if "-" in item:
            numbers = item.split("-")
            beginning = int(numbers[0])
            end = int(numbers[1])
            for i in range(beginning, end+1):
                homework_count += 1
        else:
            homework_count+=1     
    return homework_count
print(heimavinna(str(input())))
