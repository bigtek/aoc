import pandas as pd

data = pd.read_csv("firstlast.csv")

# using List comprehension + isdigit() +split()
# getting numbers from string 
res = pd.DataFrame(columns=['input','first','last', 'computed'])

def calculateSum(res):
    for i in range(len(data)):
        parsedLine = [int(j) for j in data["string"][i] if j.isdigit()]
        line = {"input": data["string"][i],
                "first": parsedLine[0],
                "last": parsedLine[-1],
                "computed": parsedLine[0] * 10 + parsedLine[-1]}
        res.loc[i] = line


    # print result
    print("The numbers list is :" + str(res))
    return res["computed"].sum()

print("total is : " + str(calculateSum(res)))

