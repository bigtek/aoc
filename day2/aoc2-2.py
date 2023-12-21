import pandas as pd

# opening the file in read mode 
my_file = open("input.txt", "r") 

# reading the file 
data = my_file.read() 

# replacing end splitting the text 
# when newline ('\n') is seen. 
data_into_list = data.split("\n") 
#print(data_into_list[0]) 

df = pd.DataFrame(columns=["game", "red", "green", "blue"])
gamesToRemove = []
for i in range(len(data_into_list)):
    #print ("i is " + str(i)) 
    gameData = data_into_list[i].split(":")
    #if gameData[1] exists
    if (len(gameData) > 1):
        tries = gameData[1].split(";")
        finalBlue = 0
        finalRed = 0
        finalGreen = 0

        for j in range(len(tries)):
            cubes = tries[j].split(",")
            
            blue = 0
            red = 0
            green = 0

            for k in range(len(cubes)):
                color = cubes[k].split(" ")
                #print("what is this cube? "+ color[2] + " and the val is " + color[1])
                if color[2] == "blue":
                    blue = int(color[1])
                    if blue > finalBlue:
                        finalBlue = blue
                elif color[2] == "red":
                    red = int(color[1])
                    if red > finalRed:
                        finalRed = red
                elif color[2] == "green":
                    green = int(color[1])
                    if green > finalGreen:
                        finalGreen = green

               
        myGame = int(gameData[0].replace("Game ",""))
        row = { "game": myGame,
            "red": finalRed,
            "green": finalGreen,
            "blue": finalBlue }

        df.loc[len(df.index)] = row
    

my_file.close() 
df.to_csv("output2.csv", index=False, sep="\t")

df['total'] = df['blue'] * df['red'] * df["green"]

# Sum of all the rows in the 'total' column
total_sum = df['total'].sum()

print("grand total is " + str(total_sum))


