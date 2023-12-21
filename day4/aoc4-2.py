import pandas as pd

file_path = 'input.txt'
df2 = pd.DataFrame(columns=['game', 'instances'])

def load_games_from_file():
    my_file = open(file_path, "r") 

    # reading the file 
    data = my_file.read() 

    # replacing end splitting the text 
    # when newline ('\n') is seen. 
    data_into_list = data.split("\n") 

    df = pd.DataFrame(columns=['game', 'winning_nums', 'played_nums', 'num_of_instances'])

    for i in range(len(data_into_list)):
        gameData = data_into_list[i].split(":")

        nums = gameData[1].split('|')
        winning_num = nums[0]
        played_nums = nums[1]
        #print('hi game data is ' + str(played_nums))

        split_values = winning_num.split(' ')
        winning_list = [int(value) for value in split_values if value]
        
        split_values = played_nums.split(' ')
        played_list = [int(value) for value in split_values if value]

        row = {'game': gameData[0].replace('Card ', ''),
               'winning_nums': winning_list,
               'played_nums': played_list,
               'num_of_instances': 1}
        df.loc[len(df.index)] = row

        row = {'game': gameData[0].replace('Card ', ''),
               'instances': 1}
        df2.loc[len(df2.index)] = row

    return df

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def calculate_total(game_matrix):
    total_sum = 0
    for index, row in game_matrix.iterrows():
        #print(f"Index: {index}, Game: {row['game']}, Merged: {row['common_elements']}")
        match_num = -1
        for num in row['common_elements']:
            match_num = match_num+1
            #print(f"num is {num} and match num is {match_num}")
        if match_num > -1:
            total_sum = total_sum + 2**match_num
            #print(f"Index is {index} and number of matches is {match_num} and the sum so far is {total_sum}")
            #change the number of instances
            df2.loc[index+1 : index+len(row['common_elements']), 'instances'] += df2.loc[index, 'instances']
            #df2.loc[index+1 : index+len(row['common_elements']), 'instances'] + (df2.loc[index : index+len(row['common_elements'])-1, 'instances'] + len(row['common_elements']))
            print(f"the instance of this row is {df2.loc[index, 'instances']}")
            print(f"DF2 is {str(df2)}")
    return df2['instances'].sum()

game_matrix = load_games_from_file()
# Create a new column 'merged_list' by applying the function to each row
# Create a new column with common elements
game_matrix['common_elements'] = game_matrix.apply(lambda row: find_common_elements(row['winning_nums'], row['played_nums']), axis=1)

total = calculate_total(game_matrix)
print(f"hi there the total is {total}")
#print('hi game data is ' + str(df2))

