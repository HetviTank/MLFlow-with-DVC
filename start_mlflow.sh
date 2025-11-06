#!/bin/bash

# Navigate to the project directory
cd /home/hetvi/Documents/python/mlflow_with_dvc

# Start MLflow server in the background
echo "Starting MLflow server..."
mlflow server --host 127.0.0.1 --port 5000 &

# Wait a moment for the server to start
sleep 5

echo "MLflow server started at http://127.0.0.1:5000"
echo "You can now run your experiment with: python mlflow-with-dvc.py"
echo "To stop the MLflow server, use: pkill -f mlflow"