import numpy as np
x = np.array(([2,9],[1,5],[3,6]),dtype = float)
y = np.array(([92],[86],[89]),dtype = float)
x = x/np.amax(x,axis=0)
y = y/100
def sigmoid(x):
  return 1/(1+np.exp(-x))

def derivatives_sigmoid(x):
  return x*(1-x)
epoch = 5
lr = 0.1
np.random.seed(1)
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1

wh = np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh = np.random.uniform(size=(1,hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout = np.random.uniform(size=(1,outputlayer_neurons))
for i in range(epoch):
  #Forward Propagation
  hinp1=np.dot(x,wh)
  hinp=hinp1 + bh 
  hlayer_act = sigmoid(hinp) 
  outinp1=np.dot(hlayer_act,wout)
  outinp= outinp1+bout
  output = sigmoid(outinp)
  #Backpropagation
  EO = y-output
  outgrad = derivatives_sigmoid(output)
  d_output = EO * outgrad 
  EH = d_output.dot(wout.T)
  hiddengrad = derivatives_sigmoid(hlayer_act)
#how much hidden layer wts contributed to error 
d_hiddenlayer = EH * hiddengrad 
wout += hlayer_act.T.dot(d_output)*lr
# dotproduct of nextlayererror and currentlayerop 
wh += x.T.dot(d_hiddenlayer)*lr
print("Input: \n" + str(x))
print("\nActual Output: \n" + str(y))
print("\nPredicted Output: \n" ,output)