import random
import math

xWeight1 = [random.uniform(-1, 1), random.uniform(-1, 1)]
xWeight2 = [random.uniform(-1, 1), random.uniform(-1, 1)]
xWeight3 = [random.uniform(-1, 1), random.uniform(-1, 1)]

sigmoid_threshold = 0.5

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def apply_threshold(output, threshold):
    if output >= threshold:
        return 1
    else:
        return 0

def perceptron(xInput, xWeight):
    weightedSum = 0
    for x, w in zip(xInput, xWeight):
        weightedSum += x * w
    return sigmoid(weightedSum)


def calculate_error(target, output):
    return target - output

def backpropagation(xInput, xWeight, error, learning_rate):
    for i in range(len(xWeight)):
        xWeight[i] += learning_rate * error * xInput[i]

def generate_xor_target(input1, input2):
    return int(input1) ^ int(input2)

learning_rate = 0.1


input1 = input("Enter the value for input1 (0 or 1): ")
input2 = input("Enter the value for input2 (0 or 1): ")

input1 = int(input1)
input2 = int(input2)

target_output = generate_xor_target(input1, input2)


for epoch in range(1000):  
    output1 = perceptron([input1, input2], xWeight1)
    output2 = perceptron([input1, input2], xWeight2)
    Input3 = [output1, output2]
    output = perceptron(Input3, xWeight3)

    error = calculate_error(target_output, output)

    
    backpropagation(Input3, xWeight3, error, learning_rate)
    backpropagation([input1, input2], xWeight1, error * xWeight3[0], learning_rate)
    backpropagation([input1, input2], xWeight2, error * xWeight3[1], learning_rate)

    print(f"Epoch {epoch + 1}:")
    print("xWeight1:", xWeight1)
    print("xWeight2:", xWeight2)
    print("xWeight3:", xWeight3)

output1 = perceptron([input1, input2], xWeight1)
output2 = perceptron([input1, input2], xWeight2)
Input3 = [output1, output2]
output = perceptron(Input3, xWeight3)
binary_output = apply_threshold(output, sigmoid_threshold)


print(f"Final output for inputs ({input1}, {input2}):")
print(output)
print(binary_output)
