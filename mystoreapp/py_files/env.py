import os

os.environ['SERVER_HOST'] = '127.0.0.1' 
os.environ['SERVER_PORT'] = '5000'
os.environ['SERVER_DEBUG'] = False

# SERVER_HOST = os.getenv('SERVER_HOST')
# SERVER_PORT = int(os.getenv('SERVER_PORT'))
# SERVER_DEBUG = os.getenv('SERVER_DEBUG')

os.environ['SECRET_KEY'] = 'mcloset-test'

os.environ['STRIPE_SECRET_KEY'] = "sk_test_51NHybZFtRmC6GWxQgYOB7FLa8jkUbyIUyRXHe9X0l21AbJVBJINr1WWg0kbIbZ9H0Ma2p5gpzHKH4MZACXXZLODQ00lRVLOHRB"
os.environ['STRIPE_PUBLISH_KEY'] = "pk_test_51NHybZFtRmC6GWxQE7E8vVeO32laNHkrJsgLp0tcFAlalhBZYfnRkfIVD2zXulfUpviMJvRHGCHMYk84W1ZJQOaV00x9RAxmnV"
