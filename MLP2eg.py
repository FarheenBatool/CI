import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

#def initialize_weights(input_size):
 #   return [random.uniform(-1, 1) for _ in range(input_size)]


def weighted_sum(inputs, weights):
    return sum(x * w for x, w in zip(inputs, weights))

def predict(inputs, weights):
    return sigmoid(weighted_sum(inputs, weights))

def backpropagate(inputs, weights, error, learning_rate):
    for i in range(len(weights)):
        weights[i] += learning_rate * error * inputs[i]


def generate_student_data():
    study_time = random.uniform(0, 10)
    attendance = random.uniform(0, 1)
    previous_test_scores = random.uniform(0, 100)
    return [study_time, attendance, previous_test_scores]


def calculate_exam_score(features):
    return predict(features, weights)

learning_rate = 0.1
epochs = 1000
weights = [0.2, 0.3, 0.1]  


for epoch in range(epochs):
    features = generate_student_data()
    target_exam_score = features[0] * 0.3 + features[1] * 0.2 + features[2] * 0.1  
    predicted_exam_score = calculate_exam_score(features)
    error = target_exam_score - predicted_exam_score
    backpropagate(features, weights, error, learning_rate)

    if epoch % 100 == 0:
        print(f"Epoch {epoch + 1}: Error = {error}")

test_features = [5.0, 0.8, 100.0]  
predicted_score = calculate_exam_score(test_features)
print(f"Predicted Exam Score: {predicted_score:.2f}")
