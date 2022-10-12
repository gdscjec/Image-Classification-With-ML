# The following lines adjust the granularity of reporting. 
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

# Improves format of Numpy arrays
np.set_printoptions(linewidth = 200)

# Loading DataSet
#as MNIST is present as a library it is easy to load the data otherwise we have to provide a link to load 
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

# better output format
np.set_printoptions(linewidth = 200)

