#!/usr/bin/env python3
"""
Setup script for MLflow + DVC + GCP integration
"""
import os
import subprocess
import sys

def setup_gcp_integration():
    """Setup MLflow and DVC with GCP Cloud Storage"""
    
    print("Setting up MLflow + DVC + GCP integration...")
    
    # Verify GCP credentials
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", 
                          os.path.expanduser("~/.config/gcloud/application_default_credentials.json"))
    if not os.path.exists(creds_path):
        print("❌ GCP credentials not found. Run: gcloud auth application-default login")
        return False
    
    # Set environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path
    
    # Test DVC remote connection
    try:
        result = subprocess.run(["dvc", "remote", "list"], capture_output=True, text=True)
        if "gcp-storage" in result.stdout:
            print("✅ DVC GCP remote configured")
        else:
            print("❌ DVC GCP remote not found")
            return False
    except Exception as e:
        print(f"❌ DVC check failed: {e}")
        return False
    
    # Test MLflow tracking URI
    try:
        import mlflow
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "gs://your-bucket/mlflow-tracking"))
        print("✅ MLflow GCP tracking configured")
    except Exception as e:
        print(f"❌ MLflow setup failed: {e}")
        return False
    
    print("🎉 Setup complete! MLflow and DVC are now integrated with GCP.")
    return True

if __name__ == "__main__":
    setup_gcp_integration()