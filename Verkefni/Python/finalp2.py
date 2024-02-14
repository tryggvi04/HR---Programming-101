from typing import List

def main():

    file_name = str(input())
    data_file = get_file(file_name)

    if data_file is not None:
        competitor_list = get_competitors(data_file)
        formatted_string = format_list(competitor_list)
        print(formatted_string)

def get_file(file_name: str):
    """Opens the given file, returning its file object if found, otherwise None."""

    try:
        file_object = open(file_name)
        return file_object
    except FileNotFoundError:
        return None
    
def get_competitors(file_object) -> list[list]:
    """Returns a dictionary of all competitors and their scores. The full name of the competitor is the key and their throw distance is the value."""

    competitor_dict = {}
    for line in file_object:
        line = line.split()
        first_name, last_name, distance_thrown = line
        full_name = first_name + " " + last_name

        if full_name in competitor_dict:
            competitor_dict[full_name] += " " + distance_thrown
        else:
            competitor_dict[full_name] = distance_thrown

    return competitor_dict

def format_list(competitor_dict: dict) -> str:
    ''' Takes in the competitor list and returns a string in the correct format to be printed.
    The function also takes in account whether a competitor has thrown more than once and acts accordingly.'''

    formatted_string = ""
    multiple_throw = []
    for competitor, distance_thrown in competitor_dict.items():
        if len(distance_thrown.split()) > 1: # Check if they've thrown it more than once
            multiple_throw.append(competitor)

        if formatted_string == "": 
            formatted_string = "{:<20}Throws: {}".format(competitor.strip(), distance_thrown.strip())
        else:
            formatted_string += "\n{:<20}Throws: {}".format(competitor.strip(), distance_thrown.strip())
    
    if multiple_throw != []: # If someone has thrown it more than once, we calculate the highest average among them.
        highest_average = calculate_average(multiple_throw, competitor_dict)
        formatted_string += "\n" + highest_average

    return formatted_string

def calculate_average(competitor_list: list, competitor_dict: dict):
    ''' Calculates the average of those competitors that threw more than one javelin.'''

    highest_average: float = 0
    highest_competitor: str = ""
    return_str = ""
    for competitor in competitor_list:
        distances_thrown = competitor_dict[competitor].split()
        distances_thrown = [float(distance) for distance in distances_thrown] # Converts the distances into floats
        calculated_average = sum(distances_thrown)/len(distances_thrown) # Sum divided by n

        if highest_average < calculated_average:
            highest_average = calculated_average
            highest_competitor = competitor

    return_str = "{}: {:.2f}".format(highest_competitor.strip(), highest_average)
    return return_str
   
if __name__ == "__main__":
    main()