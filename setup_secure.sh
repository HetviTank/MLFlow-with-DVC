#!/bin/bash
set -e

# Secure DVC Setup Commands
# This script uses environment variables instead of hardcoded values

# Check required environment variables
if [ -z "$GCP_BUCKET" ]; then
    echo "Error: GCP_BUCKET environment variable not set"
    echo "Please set: export GCP_BUCKET=your-bucket-name"
    exit 1
fi

echo "Setting up DVC with bucket: $GCP_BUCKET"

# Initialize git repository (if not already done)
git init

# Initialize DVC
dvc init

# Configure GCP remote storage using environment variable
dvc remote add -d gcp-storage "gs://$GCP_BUCKET/dvc-storage"

# Add data to DVC tracking
dvc add data/wine-quality.csv

# Commit DVC files to git
git add data/wine-quality.csv.dvc .dvc/config .dvcignore
git commit -m "Add data with DVC"

# Create and push git tag
git tag -a 'v1' -m 'Initial data version'

echo "Setup complete. To push data: dvc push"
echo "To push git changes: git push origin main && git push origin v1"