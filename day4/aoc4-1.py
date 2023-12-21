import pandas as pd

file_path = 'input_mini.txt'

def load_games_from_file():
    my_file = open(file_path, "r") 

    # reading the file 
    data = my_file.read() 

    # replacing end splitting the text 
    # when newline ('\n') is seen. 
    data_into_list = data.split("\n") 

    df = pd.DataFrame(columns=['game', 'winning_nums', 'played_nums'])

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

        row = {'game': gameData[0],
               'winning_nums': winning_list,
               'played_nums': played_list}
        df.loc[len(df.index)] = row
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
            print(f"Index is {index} and number of matches is {match_num} and the sum so far is {total_sum}")
    return total_sum

game_matrix = load_games_from_file()
# Create a new column 'merged_list' by applying the function to each row
# Create a new column with common elements
game_matrix['common_elements'] = game_matrix.apply(lambda row: find_common_elements(row['winning_nums'], row['played_nums']), axis=1)

total = calculate_total(game_matrix)
print(f"hi there the total is {total}")
print('hi game data is ' + str(game_matrix))

