import mlflow 
print('printing tracking url schema blew')

print(mlflow.get_tracking_uri())
print('/n')

mlflow.set_tracking_uri('http://127.0.0.1:5000')
print('printing new tracking url schema blew')

print(mlflow.get_tracking_uri())
print('/n')