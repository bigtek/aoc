import pandas as pd
from enum import Enum

file_path = 'input.txt'

class MapType(Enum):
    SEED_TO_SOIL = (1, "seed-to-soil")
    SOIL_TO_FERTILIZER = (2, "soil-to-fertilizer")
    FERTILIZER_TO_WATER = (3, "fertilizer-to-water")
    WATER_TO_LIGHT = (4, "water-to-light")
    LIGHT_TO_TEMPERATURE = (5, "light-to-temperature")
    TEMPERATURE_TO_HUMIDITY = (6, "temperature-to-humidity")
    HUMIDITY_TO_LOCATION = (7, "humidity-to-location")

map_list = pd.DataFrame(columns=['type', 'destination_start', 'source_start', 'range'])

def get_seed_list(seeds):
    tmp = seeds.split(":") 
    
    seed_value = tmp[1].split(' ')
    return [int(value) for value in seed_value if value]

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

def calculate_destination(source_num, next_workflow):
    #get the rows that correlate to the workflow
    filtered_rows = map_list[map_list['type'] == next_workflow.value[1]]   
    #print(f"how about here? {str(filtered_rows)}")  
    
    filtered_row = filtered_rows[(filtered_rows['source_start'] <= source_num) & 
                    (source_num <= filtered_rows['source_start'] + filtered_rows['range']-1)]
    filtered_row = filtered_row.reset_index(drop=True)

    if len(filtered_row) == 1:
        diff = source_num - filtered_row.loc[0, 'source_start']
        target = filtered_row.loc[0, 'destination_start'] + diff
        print(f"the final target value of the {next_workflow.value[1]} is {target}")
        return target
    elif len(filtered_row) == 0:
        print(f"no map found for {next_workflow.value[1]} returning {source_num}")
        return source_num
    else:
        print("got more than one row!  thsi should not happen")
        return None
    
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
            seeds_list = get_seed_list(data_into_list[i])
        else:
            map_things(data_into_list[i])
    
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

parse_file()
#print(f"here's teh matrix {str(map_list)}")
#calculate_destination(seed_list[0], MapType.FERTILIZER_TO_WATER)