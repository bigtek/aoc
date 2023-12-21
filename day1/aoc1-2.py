import pandas as pd

data = pd.read_csv("firstlast.csv")

# using List comprehension + isdigit() +split()
# getting numbers from string 
res = pd.DataFrame(columns=['input','first','last', 'computed'])

def digitize(row):
    row = row.lower()
    premapping = { 'oneight':'oneeight', 'threeight':'threeeight', 'fiveight':'fiveeight',
                'sevenine': 'sevennine', 'eightwo': 'eighttwo', 'nineight': 'nineeight', 'twone': 'twoone'}
    for k, v in premapping.items():
        row = row.replace(k, v)

    mapping = { 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for k, v in mapping.items():
        row = row.replace(k, v)
    return row

def calculateSum():
    for i in range(len(data)):
        line = digitize(data["string"][i])
        parsedLine = [int(j) for j in line if j.isdigit()]
        line = {"input": data["string"][i],
                "first": parsedLine[0],
                "last": parsedLine[-1],
                "computed": parsedLine[0] * 10 + parsedLine[-1]}
        res.loc[i] = line

    # print result
    print("The numbers list is :" + str(res))
    return res["computed"].sum()

print("total is : " + str(calculateSum()))

