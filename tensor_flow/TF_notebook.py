#### notepad for tensorflow

# initialize global variables
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)


# initializing weights with normalized random numbers

n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))

# initialize bias with 0 (ZERO)
n_labels = 5
bias = tf.Variable(tf.zeros(n_labels))




### QUIZ 

Instructions
Open quiz.py.
Implement get_weights to return a tf.Variable of weights
Implement get_biases to return a tf.Variable of biases
Implement xW + b in the linear function
Open sandbox.py
Initialize all weights
Since xW in xW + b is matrix multiplication, you have to use the tf.matmul() function instead of tf.multiply().
 Don't forget that order matters in matrix multiplication, so tf.matmul(a,b) is not the same as tf.matmul(b,a).




 ### MULTIPLE INPUTS BASICS
 We can take advantage of an operation called broadcasting used in TensorFlow and Numpy. 
 This operation allows arrays of different dimension to be added or multiplied with each other. For example:

 import numpy as np
t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
u = np.array([1, 2, 3])
print(t + u)



# SOFTMAX w logits
# logits is a one-dimensional array with 3 elements
logits = [1.0, 2.0, 3.0]
# softmax will return a one-dimensional array with 3 elements
print softmax(logits)

#### QUIZ

# Solution is available in the other "solution.ipynb" 
import tensorflow as tf


def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)
    
    # TODO: Calculate the softmax of the logits
    # softmax =  
    softmax = tf.nn.softmax(logit_data)
    
    with tf.Session() as sess:
        #pass
        # TODO: Feed in the logit data
        # output = sess.run(softmax,    )
        output = sess.run(softmax,  feed_dict={logits: logit_data} )

    return output



### DON'T MODIFY ANYTHING BELOW ###
### Be sure to run all cells above before running this cell ###
import grader

try:
    grader.run_grader(run)
except Exception as err:
    print(str(err))

### create batches

import math

def batches(batch_size, features, labels):
    #
    # Create batches of features and labels
    # :param batch_size: The batch size
    # :param features: List of features
    # :param labels: List of labels
    # :return: Batches of (Features, Labels)

    assert len(features) == len(labels)
    # TODO: Implement batching
    out_bat = []
    
    sample_size = len(features)
    
    for i in range(0, sample_size, batch_size):
        j = i + batch_size
        batch = [features[i:j], labels[i:j]]
        out_bat.append(batch)
        
    return out_bat