import pandas as pd 
import re
from enum import Enum

class Adjacent(Enum):
    LEFT = 1
    RIGHT = 2
    ABOVE = 3
    BELOW = 4
    ABOVESPECIAL = 5
    BELOWSPECIAL = 6

#for this problem. i need to iterate over the symbol *.  evaluate each *
# and see if there are at least two adjacent numbers.


def extract_symbol_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {'Symbol': [], 'X': [], 'Y': []}
    special_characters = "!*"
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            #if char in {'$', '!', '@', '#', '%', '^', '&', '*', '\\', '/', '(', ')', '-'}:
            if char in special_characters:
                data['Symbol'].append(char)
                data['X'].append(x+1)
                data['Y'].append(y+1)

    df = pd.DataFrame(data)
    return df

def extract_numbers(line, line_number):
    # Define a regular expression pattern to match numbers
    pattern = re.compile(r'(\d+)')
    
    # Find all matches in the line
    matches = pattern.finditer(line)
    
    # Extract information about each match
    result = []
    for match in matches:
        start_index, end_index = match.span()
        number = match.group()
        result.append({
            'number': number,
            'y_coordinate': line_number,
            'start_x': start_index + 1,  # Adding 1 to make it 1-based index
            'end_x': end_index  # end index is exclusive
        })
    
    return result

def extract_number_at_position(line, position):
    # Split the input string into a list of substrings using non-numeric characters as separators
    substrings = ''.join(c if c.isdigit() else ' ' for c in line).split()

    # Check if the specified position is within the range of substrings
    if 1 <= position <= len(substrings):
        return substrings[position - 1]
    else:
        return "NOT A NUMBER"
    




def find_coordinates(input_file, numbers):
    coordinates = []

    with open(input_file, 'r') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line):
                if char == '*':
                    coordinates.append((x+1, y+1))
                    # see if there a number to the left
                    #result = next(item['number'] for item in numbers if int(item['start_x']) == int(x) and int(item['y_coordinate']) == int(y)+1)
                    
    return coordinates        

def process_file(file_path):
    sum = 0
    # first get all the numbers
    number_grid = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Extract information from the current line
            #numbers_info = extract_numbers(line, line_number)
            number_grid.append(extract_numbers(line, line_number))
            #number_grid.append(numbers_info = extract_numbers(line, line_number))
    #next get the *
       
    return number_grid        

def get_number_match(data_list, star, direction):
    for data in data_list:
        if ((data.get('end_x') == star[0] - 1 and direction == Adjacent.LEFT) or
            (data.get('start_x') == star[0] + 1 and direction == Adjacent.RIGHT) or 
            (direction == Adjacent.ABOVE and star[1]-1 == data.get('y_coordinate')) and 
                star[0]-1 <= data.get('end_x') and star[0]+1 >= data.get('start_x') or 
            (direction == Adjacent.BELOW and star[1]+1 == data.get('y_coordinate')) and 
                star[0]-1 <= data.get('end_x') and star[0]+1 >= data.get('start_x') or

            (direction == Adjacent.ABOVESPECIAL and star[1]-1 == data.get('y_coordinate')) and
              star[0]+1 == data.get('start_x') or
            (direction == Adjacent.BELOWSPECIAL and star[1]+1 == data.get('y_coordinate')) and
              star[0]+1 == data.get('start_x')):
            #print("star is " + str(star))
            #print("number is " str(data.get('number'))) + " and the x coords are " + str(data.get('start_x')))
            #print("number is " + str(data.get('number')))
            #print(" the x are " + str(data.get('start_x')))
            #print(" and " + str(data.get('end_x')) + " and the y is " + str(data.get('y_coordinate')))
            return data.get('number')       



def find_adjacent(grid, starMap):
    sum = 0
    star_count = 0

        #for index, line in enumerate(grid):
    #    print("the y value is " + str(index) + ' and ' + str(line))
    
    for item in starMap:
    # Access each element in the tuple
        # find number to directly to the left of the star
        count = 0
        found_number1 = 0
        found_number2 = 0
        found_number3 = 0
        found_number4 = 0
        found_special_case = None
        found_special_case2 = None

        if grid[item[1]] is not None:
            line = grid[item[1]-1]
            found_number1 = get_number_match(line, item, Adjacent.LEFT)
            if found_number1 is not None:
                count = count + 1
                #print("not null left " + found_number1 + " value of count is " + str(count))
                
            found_number2 = get_number_match(line, item, Adjacent.RIGHT)
            if found_number2 is not None:
                count = count + 1
                #print("not null " + found_number2 + " value of count is " + str(count))
            line = grid[item[1]-2]
            found_number3 = get_number_match(line, item, Adjacent.ABOVE)
            if found_number3 is not None:
                count = count + 1
                #print('!!!found from above!!!!!')
                found_special_case2 = get_number_match(line, item, Adjacent.ABOVESPECIAL)
                if found_special_case2 is not None:
                    count = count + 1
                    print('!!!! found a special case above ! ' + str(found_special_case2))

            line = grid[item[1]]
            found_number4 = get_number_match(line, item, Adjacent.BELOW)
            if found_number4 is not None:
                count = count + 1
                print('!!!found from below!!!!!' + str(found_number4))    

                found_special_case = get_number_match(line, item, Adjacent.BELOWSPECIAL)
                if found_special_case is not None:
                    count = count + 1
                    print('!!!! found a special case ! ' + str(found_special_case))

            #print('next please ' + str(count))
            if (count == 2):
                star_count = star_count+1
                print('star count at this point ' + str(star_count))
                found_number1 = 1 if found_number1 is None else found_number1
                found_number2 = 1 if found_number2 is None else found_number2
                found_number3 = 1 if found_number3 is None else found_number3
                found_number4 = 1 if found_number4 is None else found_number4
                found_special_case = 1 if found_special_case is None else found_special_case
                found_special_case2 = 1 if found_special_case2 is None else found_special_case2


                if sum > 0:
                    sum = sum + int(found_number1) * int(found_number2) * int(found_number3) * int(found_number4) * int(found_special_case) * int(found_special_case2)
                    print(' Hit!!! ' + str(found_number1) + " , " + str(found_number2) + " , " + str(found_number3)  + " , " + str(found_number4)  + " , SP = " + str(found_special_case) + " , SP2 = " + str(found_special_case2))
                else:
                    sum = int(found_number1) * int(found_number2) * int(found_number3) * int(found_number4) * int(found_special_case) * int(found_special_case2)
                    print('FIRST ONE!! ' + str(found_number1) + " , " + str(found_number2) + " , " + str(found_number3)  + " , " + str(found_number4) + " , SP = " + str(found_special_case) + " , SP2 = " + str(found_special_case2))
                print('$$$current sum is ' + str(sum))
        print("the amount of stars that matched " + str(star_count))        
    return sum              

file_path = 'mini_input.txt'
#symbol_coordinates = extract_symbol_coordinates(file_path)

grid = process_file(file_path)
starMap = find_coordinates("mini_input.txt", grid)
total = find_adjacent(grid, starMap)

#print('stars are here' + str(starMap))
print('length of star list is ' + str(len(starMap)))
print('hi there total is ' + str(total))

#symbol_coordinates.to_csv("output.csv", index=False, sep="\t")
