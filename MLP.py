xInput = []
Input3 = []
xWeigth1 = [0.6,0.6]
xWeigth2 = [1.1,1.1]
xWeigth3 = [-2,1.1]



threshold = 1
def step(weightedSum):
    if(weightedSum) > threshold:
        return 1
    else:
        return 0


def perceptron1():
    weightedSum1=0
    for x,w in zip(xInput,xWeigth1):
        weightedSum1 += x*w
    return step(weightedSum1)

def perceptron2():
    weightedSum2=0
    for x,w in zip(xInput,xWeigth2):
        weightedSum2 += x*w
    return step(weightedSum2)   

def perceptron3():
    weightedSum3=0
    for x,w in zip(Input3,xWeigth3):
        weightedSum3 += x*w
    return step(weightedSum3)  

for i in range(2):
    user_input = input(f"Enter the value for xInput[{i}]: ")
    try:
        xInput.append(int(user_input))
    except ValueError:
        print("Invalid input. Please enter an integer.")

output1 = perceptron1()
output2 = perceptron2()
Input3 = [output1,output2]
output = perceptron3()

print(output)