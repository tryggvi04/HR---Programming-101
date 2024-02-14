def is_file(file_name: str):
    ''' Boolean function to tests whether or not the string given is a file that can be opened '''
    try:
        file_test = open(file_name)
        return True
    except:
        return False


def inflation(data_list: list):
    ''' Calculates the inflation of a given list '''

# Inflation rate = ((B - A)/A)*100 where A = starting cost and B = ending cost

    inflation_int = (data_list[len(data_list)-1] - data_list[0])/data_list[0]
    inflation_int *= 100

    return round(inflation_int, 2)


def collecting_info(file_name):
    ''' Opens a file and collects the information needed in a list of tuples '''

    data_file = open(file_name)
    data_list = []
    data_tuple = ()

    for line in data_file:
        line = line.strip()
        line = line.split()

        data_tuple = (line[0], float(line[1]))
        print(data_tuple)
        data_list.append(data_tuple)
        
    return data_list

def Calculate_data(data_file: list):
    ''' We find the year(s) of the data and print the first and the last indexes and print's the inflation '''
    year_list = []
    year_data = []
    month_list = []
    year_tuple = ()


    for data in data_file:

        # The year is always after M in the given data format
        year = data[0].split("M")

        if year[0] not in year_list:
            year_list.append(year[0])
        
    
    for i in range(0, len(year_list)):
        for data in data_file:
            
            # Collect all the numbers needed for calculation for the year we are looping through
            if year_list[i] in data[0]:
                month_list.append(float(data[1]))

            
        # Format the data to the required format, printing the tuple when it's done    
        max_month = len(month_list) - 1
        year_data.append(month_list)
        year_tuple = (int(year_list[i]), month_list[0], month_list[max_month])
        print(year_tuple)
        month_list = []
    
    for i in range(0, len(year_list)):
        year_tuple = (int(year_list[i]), inflation(year_data[i]))
        print(year_tuple)
    
    
    
    
    



file_name = str(input())

if is_file(file_name):
    data_list = collecting_info(file_name)
    
    Calculate_data(data_list)
    