import pandas as pd 
import re

def extract_symbol_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {'Symbol': [], 'X': [], 'Y': []}
    special_characters = "!@#$%^&*()_-+=<>?/\\|{}[]~`';:,"
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

def process_file(file_path):
    sum = 0
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Extract information from the current line
            numbers_info = extract_numbers(line, line_number)
            
            # Print the information for each number in the line
            for info in numbers_info:
                #next calculate each number to see if there is a symbol directly to the left
                if any((symbol_coordinates['Y'] == info['y_coordinate']) & 
                       (symbol_coordinates['X'] == info['start_x'] - 1)):          
                    sum = sum + int(info['number'])
                elif any((symbol_coordinates['Y'] == info['y_coordinate']) & 
                       (symbol_coordinates['X'] == info['end_x'] + 1)):          
                    sum = sum + int(info['number'])
                elif any((symbol_coordinates['Y'] == info['y_coordinate']-1) & 
                       (symbol_coordinates['X'] >= info['start_x'] - 1) &
                       (symbol_coordinates['X'] <= info['end_x'] + 1)):          
                    sum = sum + int(info['number'])
                elif any((symbol_coordinates['Y'] == info['y_coordinate']+1) & 
                       (symbol_coordinates['X'] >= info['start_x'] - 1) &
                       (symbol_coordinates['X'] <= info['end_x'] + 1)):          
                    sum = sum + int(info['number'])
                else:
                    print("no match for " + info['number'] + " (" + str(info['start_x']) + ", " + str(info['y_coordinate']) + ")")
                #print("sum so far is " + str(sum)) 
            #print(numbers_info)            
    return sum               
                


# Example usage:
file_path = 'input.txt'
symbol_coordinates = extract_symbol_coordinates(file_path)

total = process_file(file_path)

print('hi there total is ' + str(total))

symbol_coordinates.to_csv("output.csv", index=False, sep="\t")
