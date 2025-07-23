#neuron with 3 inputs
inputs = [1,2,3,2.5]
weights = [0.1,0.8,-0.5,1]
bias = 2.0
outputs = [inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3]+bias]
print(outputs)
#layer of neurons
inputs = [1,2,3,2.5]

weights = [[0.2,0.8,-0.5,1],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
weights0 = weights[0] # weights for 1st neuron
weights1 = weights[1] # weights for 2nd neuron
weights2 = weights[2] # weights for 3rd neuron
#weights3 = weights[3] # weights for 4th neuron
biases = [2,3,0.5]
bias1 = 2
bias2 = 3
bias3 = 0.5
outputs = [
    #neuron1
    inputs[0]*weights0[0]+inputs[1]*weights0[1]+inputs[2]*weights0[2]+inputs[3]*weights0[3]+bias1,
#neuron2
           inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias2,
#neuron3
           inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+bias3,
#neuron4
 #          inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+bias3
              ]
print(outputs)
#we can do same thing in loop
neuron_outputs = []
for weight, bias in zip(weights, biases):
    neuron_output_temp = 0
    for neuron_output, neuron_input in zip(weight, inputs):
        neuron_output_temp += neuron_output*neuron_input
    #neuron_output_temp += neuron_output_temp+bias
    neuron_outputs.append(neuron_output_temp+bias)
    print(neuron_output_temp)
print(neuron_outputs)
