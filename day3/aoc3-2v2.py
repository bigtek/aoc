import re

file_path = 'input.txt'

def extract_numbers(line, line_number):
    # Define a regular expression pattern to match numbers
    pattern = re.compile(r'(\d+)')
    
    # Find all matches in the line
    matches = pattern.finditer(line)
    
    # Extract information about each match
    result = []
    index = 1
    for match in matches:
        start_index, end_index = match.span()
        number = match.group()
        result.append({
            'id': str(line_number) + '-' + str(index),
            'number': number,
            'y_coordinate': line_number,
            'start_x': start_index + 1,  # Adding 1 to make it 1-based index
            'end_x': end_index  # end index is exclusive
        })
        index = index+1
    return result    

def process_file():
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

def find_coordinates():
    coordinates = []

    with open(file_path, 'r') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line):
                if char == '*':
                    coordinates.append((x+1, y+1))
                    # see if there a number to the left
                    #result = next(item['number'] for item in numbers if int(item['start_x']) == int(x) and int(item['y_coordinate']) == int(y)+1)
                    
    return coordinates  

def check_adjacent(grid, starMap):
    #iterate thru the starts
    total = 0
    for star in starMap:
        match_list = []

        #check to see if theres a number directly to the left
        same_line = grid[star[1]-1]
        above_line = grid[star[1]-2]
        below_line = grid[star[1]]

        for num in same_line:
            if num.get('end_x') == star[0] - 1: 
                #there's a number to the left
                match_list.append(num)
            if num.get('start_x') == star[0] + 1: 
                #there's a number to the right
                print('added to the right ' + num.get('number'))
                match_list.append(num)   
    
        for num in below_line:
            if star[1]+1 == num.get('y_coordinate') and star[0]-1 <= num.get('end_x') and star[0]+1 >= num.get('start_x'):
                match_list.append(num)
                if star[1]+1 == num.get('y_coordinate') and star[0]+1 == num.get('start_x'):
                    if len(match_list) > 0:
                        id_to_check = num['id']
                        id_exists = any(item['id'] == id_to_check for item in match_list)

                    # If 'id' doesn't exist, append the new item
                        if not id_exists:
                            match_list.append(num)

        for num in above_line:
            if star[1]-1 == num.get('y_coordinate') and star[0]-1 <= num.get('end_x') and star[0]+1 >= num.get('start_x'):
                match_list.append(num)
                if star[1]-1 == num.get('y_coordinate') and star[0]+1 == num.get('start_x'):
                    if len(match_list) > 0:
                        id_to_check = num['id']
                        id_exists = any(item['id'] == id_to_check for item in match_list)

                        # If 'id' doesn't exist, append the new item
                        if not id_exists:
                            match_list.append(num)

        
        if len(match_list) == 2:
            print("matchy! " + str(match_list))
            sum = 1
            for match in match_list:
                sum = sum * int(match['number'])
            total = total + sum   
           
    return total

grid = process_file()
#print(str(grid))
starMap = find_coordinates()
print('stars ' + str(starMap))

print(' final total! ' + str(check_adjacent(grid, starMap)))