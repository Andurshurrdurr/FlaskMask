# Statement for enabling the development environment
DEBUG = True
# SERVER_NAME = 'example.com:5000'
SECRET_KEY = 'my_secret_key'

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print "filepath is: " + str(BASE_DIR)

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2
