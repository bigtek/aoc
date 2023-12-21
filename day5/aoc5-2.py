import pandas as pd
from enum import Enum

file_path = 'input_mini.txt'

class MapType(Enum):
    HUMIDITY_TO_LOCATION = (1, "humidity-to-location")
    TEMPERATURE_TO_HUMIDITY = (2, "temperature-to-humidity")
    LIGHT_TO_TEMPERATURE = (3, "light-to-temperature")
    WATER_TO_LIGHT = (4, "water-to-light")
    FERTILIZER_TO_WATER = (5, "fertilizer-to-water")
    SOIL_TO_FERTILIZER = (6, "soil-to-fertilizer")
    SEED_TO_SOIL = (7, "seed-to-soil")

map_list = pd.DataFrame(columns=['type', 'destination_start', 'source_start', 'range'])
seedy = pd.DataFrame(columns=['start', 'range'])

def set_seed_list(seeds):
    tmp = seeds.split(":") 
    
    seed_value = tmp[1].split(' ')
    seed_list = [int(value) for value in seed_value if value]

    for i in range(len(seed_list)):
        if (i % 2 != 1):
            row = {'start': seed_list[i],
                   'range': seed_list[i+1]}
            seedy.loc[len(seedy.index)] = row

def map_things(line):    
    tmp = line.split(":") 
    lines = tmp[1].split("\n")
    
    for line in lines:
        map_value = line.split(' ')
        m_list = [int(value) for value in map_value if value]
        #print(f"the map of {tmp[0]} -  are {m_list}")
        if len(m_list) == 3:
            type_name = tmp[0].replace(" map", "")
            row = {'type': type_name,
                   'destination_start': m_list[0],
                   'source_start': m_list[1],      
                   'range': m_list[2]}
            map_list.loc[len(map_list.index)] = row
    
def get_min_range(next_workflow, min_value, max_value):
<<<<<<< Updated upstream
    #find the row that fits the range
=======
>>>>>>> Stashed changes
    filtered_rows = map_list[map_list['type'] == next_workflow.value[1]]  
    min_index = filtered_rows['destination_start'].idxmin()

    # Select the row with the minimum value
    min_row = filtered_rows.loc[min_index]
    min_row = min_row.reset_index(drop=True)
    print(f"the min row selected is {str(min_row)} and the min destination value is {min_row[1]}")
    #row[2] is the source
    #row[1] is the destination

    if min_row[1] >= max_value:
        #it's the start
        new_min_value = min_value
        new_max_value = min_row[1] - 1
        # Get the minimum value
    elif min_row[1] < max_value:
        #new min and max values
        #find teh corresponding source values to send out
        new_min_value = min_row[2]
        diff = max_value - min_value

        if diff > min_row[3]:
            diff = min_row[3]
        new_max_value = min_row[2] + diff
    '''    
    else:
        new_min_value = min_row[1] 
        val = min_row[1] + min_row[3]
        #print(f"^^^^^^^^^ the min row 1 is {min_row[2]} and the range is {min_row[3]}")
        if val < max_value:
            new_max_value = val
    '''        
    return new_min_value,new_max_value             


def parse_file():
    my_file = open(file_path, "r") 
    seeds_list = []

    # reading the file 
    data = my_file.read() 

    # replacing end splitting the text 
    # when newline ('\n') is seen. 
    data_into_list = data.split("\n\n") 
    #print('helro? ' + str(data_into_list))
    for i in range(len(data_into_list)):
        if i == 0:
            set_seed_list(data_into_list[i])
        else:
            map_things(data_into_list[i])

    #print(f"the matrix is {str(map_list)}")
    min_value = 0
    max_value = 0
    for workflow in MapType:
        min_value, max_value = get_min_range(workflow, min_value, max_value)
        print(f"the workflow is {workflow.value} : the min is - {min_value} and the max is {max_value}")
 
    '''
    target_list = []
    for seed in seeds_list:
        target = seed
        for workflow in MapType:
            index, value = workflow.value
            #target = calculate_destination(seed, workflow)
            #print(f"TARGET {seed} - {workflow.value}")
            target = calculate_destination(target, workflow)
        print(f"**********new seed***********")    
        target_list.append(target)

    print(f"$$$$$$$$ the lowest value is {min(target_list)}")
'''

parse_file()
#print(f"the seed list looks like {str(seedy)}")
#print(f"here's teh matrix {str(map_list)}")
#calculate_destination(seed_list[0], MapType.FERTILIZER_TO_WATER)