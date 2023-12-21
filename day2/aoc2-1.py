import pandas as pd

# opening the file in read mode 
my_file = open("input.txt", "r") 

# reading the file 
data = my_file.read() 

# replacing end splitting the text 
# when newline ('\n') is seen. 
data_into_list = data.split("\n") 
#print(data_into_list[0]) 

df = pd.DataFrame(columns=["game","tries", "red", "green", "blue", "isPossible"])
gamesToRemove = []
for i in range(len(data_into_list)):
    #print ("i is " + str(i)) 
    gameData = data_into_list[i].split(":")
    #if gameData[1] exists
    if (len(gameData) > 1):
        tries = gameData[1].split(";")
        for j in range(len(tries)):
            cubes = tries[j].split(",")
            
            blue = 0
            red = 0
            green = 0
            isPossible = True

            for k in range(len(cubes)):
                color = cubes[k].split(" ")
                #print("what is this cube? "+ color[2] + " and the val is " + color[1])
                if color[2] == "blue":
                    blue = int(color[1])
                    if blue > 14:
                        isPossible = False
                elif color[2] == "red":
                    red = int(color[1])
                    if red > 12:
                        isPossible = False
                elif color[2] == "green":
                    green = int(color[1])
                    if green > 13:
                        isPossible = False
                myGame = int(gameData[0].replace("Game ",""))
                row = { "game": myGame,
                    "tries": j+1,
                    "red": red,
                    "green": green,
                    "blue": blue,
                    "isPossible": isPossible}
                if isPossible == False and myGame not in gamesToRemove:
                    gamesToRemove.append(myGame)
                #print("my row is " + str(row))
            df.loc[len(df.index)] = row
    
filtered_df = df[df['isPossible']] 
sum_of_distinct_games = filtered_df['game'].unique().sum()

print("Sum of distinct game numbers where 'isPossible' is True:", sum_of_distinct_games)
print("removing " + str(gamesToRemove))
print("sum to remove is " + str(sum(gamesToRemove)))

finalAnswer = 5050 - sum(gamesToRemove)
print("final answer is " + str(finalAnswer))

my_file.close() 
df.to_csv("output.csv", index=False, sep="\t")

