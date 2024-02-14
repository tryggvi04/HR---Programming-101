
def is_file(a_str):
    try:
        file_test = open(a_str)
        return True
    except:
        return False
def parse(file_name):
    num_list = []
    file_open = open(file_name)
    for line in file_open:
            line = line.split()
            for item in line:
                if item.isdecimal():
                    num_list.append(int(item))
    num_list = sorted(num_list)
    return num_list

while True:
     file_to_open = input()

     if is_file(file_to_open):
          print(parse(file_to_open))
          break
     else:
          print(file_to_open, "not found! Please try again.")
    
