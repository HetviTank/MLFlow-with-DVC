import os

# Secure configuration using environment variables
GCP_CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "~/.config/gcloud/application_default_credentials.json")
GCP_BUCKET = os.getenv("GCP_BUCKET", "your-bucket-name")
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", f"gs://{GCP_BUCKET}/mlflow-tracking")
DVC_REMOTE_URL = os.getenv("DVC_REMOTE_URL", f"gs://{GCP_BUCKET}/dvc-storage")