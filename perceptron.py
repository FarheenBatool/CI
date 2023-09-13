xInput = [1,2,3]
xWeigth = [0.1,0.2,0.4]

threshold = 0.5

def step(weightedSum):
    if(weightedSum) > threshold:
        return 1
    else:
        return 0


def perceptron():
    weightedSum=0
    for x,w in zip(xInput,xWeigth):
        weightedSum += x*w
    return step(weightedSum)
     
output = perceptron()

print(output)