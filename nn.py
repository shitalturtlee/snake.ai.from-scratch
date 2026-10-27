import numpy as np

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# intialize weights

np.random.seed(42)

input_size = 2
hidden_size = 4
output_size = 1

w1 = np.random.randn(input_size,hidden_size)*0.5
b1 = np.zeros((1,hidden_size))

w2 = np.random.randn(hidden_size,output_size)*0.5
b2 = np.zeros((1,output_size))

def sigmoid(z):
    return 1/(1+ np.exp(-z))

def forward(x,w1,b1,w2,b2):
    z1 = np.dot(x,w1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1,w2) + b2
    a2 = sigmoid(z2)
    return z1,a1,z2,a2

z1,a1,z2,a2 = forward(x,w1,b1,w2,b2)
print(a2)

def mse(y_true,y_pred):
    return np.mean((y_true - y_pred)**2)

loss = mse(y,a2)
print(loss)
 
def sigmoid_derivative(a):
    return a*(1-a)

def backward(x,y,z1,a1,z2,a2,w1,w2):
    m = x.shape[0]
    # output layer
    dLoss_da2 = (a2 - y) * (2/m)
    da2_dz2 = sigmoid_derivative(a2)
    dz2 = dLoss_da2 * da2_dz2
    dw2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0, keepdims=True)

    # hidden  layer
    da1 = dz2 @ w2.T
    dLoss_da1 = dz2 @ w2.T
    dz1 = da1 * sigmoid_derivative(a1)
    dw1 = x.T @ dz1
    db1 = np.sum(dz1, axis = 0, keepdims = True)

    return dw1,db1,dw2,db2

dw1,db1,dw2,db2 = backward(x,y,z1,a1,z2,a2,w1,w2)
print("dw1:\n",dw1)
print("dw2:\n",dw2)
