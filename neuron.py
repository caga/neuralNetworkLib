from numpy import *
import random

import math
class Neuron:
    def __init__(self, weights:array, bias,inputs:array,neuronid):
        self.id=neuonid
        self.weights = weights
        self.bias = bias
        self.inputs=inputs
        self.output=self.activate(weights)
        self.deltaw=0.000001
        self.diffOutputWeightArray=self.calculate_diff_output_diff_weight()

    def activate(self,weights:array):
        dotproduct=(weights).dot(self.inputs)
        result=1/(1+math.exp(-dotproduct+self.bias))
        return result
    def calculate_diff_output_diff_weight(self):
        diffOutputWeightArray=[]
        for i in range(len(self.weights)):
            weights=self.weights.copy()
            output1=self.activate(weights)
            weights[i]=weights[i]+self.deltaw
            output2=self.activate(weights)
            diffOutputWeight=(output2-output1)/self.deltaw
            diffOutputWeightArray.append(diffOutputWeight)
        #diffOutputWeightArray=array(diffOutputWeightArray)
        return diffOutputWeightArray
class Layer:
    def __init__(self, neuronNumber,inputs:array,layerid):
        self.id=layerid
        self.neurons=[]
        for i in range(neuronNumber-1):
            n=Neuron(

weights=array([0.0999,0.2,0.3,0.4])
bias=1
inputs=array([1,1,2,3])
n=Neuron(weights,bias,inputs)
print(n.output)
print(n.diffOutputWeightArray)
print(0.0001*n.diffOutputWeightArray[0]+n.output)
print(-0.0001*n.diffOutputWeightArray[0]+n.output)









