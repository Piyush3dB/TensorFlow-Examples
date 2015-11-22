import tensorflow as tf
__author__  = "@Piyush3dB"


def example_0():
    '''
    Basic Operations example using TensorFlow library.
    '''

    NUM_CORES = 2  # Choose how many cores to use.
    cfg = tf.ConfigProto(inter_op_parallelism_threads=NUM_CORES,
                         intra_op_parallelism_threads=NUM_CORES)

    sess = tf.Session()


    print "\n\n============== Running example 0 ..."
    # Basic constant operations
    # The value returned by the constructor represents the output
    # of the Constant op.
    a = tf.constant(2)
    b = tf.constant(3)

    # Launch the default graph.
    print "a=2, b=3"
    print "Addition with constants: %i" % sess.run(a+b)
    print "Multiplication with constants: %i" % sess.run(a*b)


    a = tf.placeholder(tf.types.int16)
    b = tf.placeholder(tf.types.int16)

    # Define some operations
    add = tf.add(a, b)
    mul = tf.mul(a, b)

    # Launch the default graph.
    
    # Run every operation with variable input
    print "Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3})
    print "Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3})

    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.],[2.]])

    product = tf.matmul(matrix1, matrix2)

    result = sess.run(product)

    print result
        # ==> [[ 12.]]


if __name__ == "__main__":
    example_0()
