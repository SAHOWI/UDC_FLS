import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.compat.v1.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant).decode()
    print(output)
