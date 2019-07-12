#!/usr/bin/env python
# coding: utf-8
import numpy as np

input_data = np.array([[0,0,1],
                       [1,1,1],
                       [1,0,1],
                       [0,1,1]])
target = np.array([[0],
                   [1],
                   [1],
                   [0]])

weight1 = np.random.uniform(0, 1, (3,3))
weight2 = np.random.uniform(0, 1, (3,1))

print(weight1.shape)
print(weight2.shape)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sig_der(x):
    return x*(1-x)

learning = .01
for i in range(10000):
    data = input_data
    output1 = sigmoid(np.dot(data, weight1))
    output2 = sigmoid(np.dot(output1, weight2))
    
    # Backpropagation
    # Error at 2nd layer
    e2 = sig_der(output2)*(target-output2)
    
    
    # Update the weight
    data = np.dot(output1.T, e2)
    weight2 += learning*np.dot(output1.T, e2)
    
    
    # First layer error
    e1 = sig_der(output2)* np.dot(e2, weight2.T)
    # Update the Weight
    weight1 += learning*np.dot(input_data.T, e1)
    
   
#print(f"Weight 1 {weight1}")
#print(f"Weight 2 {weight2}")
print(f"Output {output2}")
