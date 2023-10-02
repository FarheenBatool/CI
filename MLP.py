import random
import math

xInput = []
Input3 = []
xWeigth1 = [random.uniform(-1, 1), random.uniform(-1, 1)]
xWeigth2 = [random.uniform(-1, 1), random.uniform(-1, 1)]
xWeigth3 = [random.uniform(-1, 1), random.uniform(-1, 1)]


threshold = 1

def step(weightedSum):
    if(weightedSum) > threshold:
        return 1
    else:
        return 0



def generate_xor_target(input1, input2):
    return int(input1) ^ int(input2)


def perceptron(xInput,xWeigth):
    weightedSum=0
    for x,w in zip(xInput,xWeigth):
        weightedSum += int(x)*w
    return step(weightedSum)

def calculate_error(target, output):
    return target - output

input1 = input("Enter the value for input1 (0 or 1): ")
input2 = input("Enter the value for input2 (0 or 1): ")
xInput = [input1,input2]

input1 = int(input1)
input2 = int(input2)

output1 = perceptron(xInput,xWeigth1)
output2 = perceptron(xInput,xWeigth2)
Input3 = [output1,output2]
output = perceptron(Input3,xWeigth3)
target_output = generate_xor_target(input1, input2)
error = calculate_error(target_output, output)

print(output)
print("Error is " + str(error * 100) + "%")
