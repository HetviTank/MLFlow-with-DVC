# MLflow with DVC Integration

A machine learning project demonstrating the integration of MLflow for experiment tracking and DVC (Data Version Control) for data management, with Google Cloud Platform (GCP) as the backend storage.

## 🚀 Features

- **MLflow**: Experiment tracking, model versioning, and deployment
- **DVC**: Data version control and pipeline management
- **GCP Integration**: Cloud storage for artifacts and data
- **Secure Configuration**: Environment-based credential management

## 📋 Prerequisites

- Python 3.8+
- Git
- Google Cloud SDK (`gcloud`)
- GCP project with Cloud Storage enabled

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd mlflow_with_dvc
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup GCP Authentication
```bash
# Login to GCP
gcloud auth login

# Set up application default credentials
gcloud auth application-default login

# (Optional) If using service account impersonation:
gcloud auth application-default login --impersonate-service-account=your-service-account@project.iam.gserviceaccount.com
```

## ⚙️ Configuration

### 1. Environment Setup
Copy the environment template and configure your settings:
```bash
cp .env.template .env
```

Edit `.env` file with your values:
```bash
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
GCP_BUCKET=your-bucket-name
MLFLOW_TRACKING_URI=gs://your-bucket-name/mlflow-tracking
DVC_REMOTE_URL=gs://your-bucket-name/dvc-storage
```

### 2. Load Environment Variables
```bash
source .env  # or use python-dotenv in your scripts
```

## 🔧 Setup Commands

### Initialize DVC and MLflow
```bash
# Make setup script executable
chmod +x setup_secure.sh

# Run secure setup (requires GCP_BUCKET environment variable)
export GCP_BUCKET=your-bucket-name
./setup_secure.sh
```

### Manual Setup (Alternative)
```bash
# Initialize DVC
dvc init

# Add GCP remote storage
dvc remote add -d gcp-storage gs://your-bucket-name/dvc-storage

# Add data to DVC
dvc add data/wine-quality.csv

# Commit changes
git add data/wine-quality.csv.dvc .dvc/config .dvcignore
git commit -m "Add data with DVC"
```

## 🚀 Usage

### Start MLflow Server
```bash
./start_mlflow.sh
```
MLflow UI will be available at: http://127.0.0.1:5000

### Run Experiments
```bash
# Run with default parameters
./run_experiment.sh

# Run with custom parameters
./run_experiment.sh --alpha 0.5 --l1_ratio 0.1
```

### DVC Operations
```bash
# Pull latest data
dvc pull

# Push data changes
dvc push

# Check data status
dvc status
```

## 📁 Project Structure

```
mlflow_with_dvc/
├── data/                          # Data directory (DVC tracked)
│   ├── wine-quality.csv          # Dataset
│   └── wine-quality.csv.dvc       # DVC metadata
├── mlruns/                        # MLflow artifacts (local)
├── venv/                          # Virtual environment
├── .dvc/                          # DVC configuration
├── config.py                      # Secure configuration
├── mlflow-with-dvc.py            # Main experiment script
├── params.yaml                    # Experiment parameters
├── dvc.yaml                       # DVC pipeline definition
├── requirements.txt               # Python dependencies
├── .env.template                  # Environment template
├── .gitignore                     # Git ignore rules
├── setup_secure.sh               # Secure setup script
├── start_mlflow.sh               # MLflow server startup
├── run_experiment.sh             # Experiment runner
├── fix_gcp_auth.py               # GCP authentication helper
└── setup_gcp_integration.py      # GCP integration setup
```

## 🔒 Security Best Practices

### ✅ What's Secure
- Environment variables for credentials
- `.gitignore` prevents credential commits
- No hardcoded secrets in code
- Service account impersonation support

### ❌ Never Commit
- `.env` files
- `*.json` credential files
- `*.key` files
- Any files containing secrets

### 🛡️ Security Checklist
- [ ] GCP credentials stored securely
- [ ] Environment variables configured
- [ ] `.env` file in `.gitignore`
- [ ] No hardcoded secrets in code
- [ ] Service account has minimal permissions

## 🧪 Testing Authentication

Run the authentication test script:
```bash
python fix_gcp_auth.py
```

This will verify:
- GCP credentials configuration
- DVC remote access
- MLflow GCP integration

## 📊 Monitoring and Tracking

### MLflow Features
- Experiment tracking
- Parameter logging
- Metric visualization
- Model versioning
- Artifact storage

### DVC Features
- Data versioning
- Pipeline reproducibility
- Remote storage sync
- Data lineage tracking

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Errors**
   ```bash
   # Re-authenticate
   gcloud auth application-default login
   ```

2. **DVC Remote Issues**
   ```bash
   # Check remote configuration
   dvc remote list
   
   # Test connection
   dvc status
   ```

3. **MLflow Connection Issues**
   ```bash
   # Verify tracking URI
   python -c "import mlflow; print(mlflow.get_tracking_uri())"
   ```

### Getting Help
- Check the authentication script: `python fix_gcp_auth.py`
- Verify environment variables are set
- Ensure GCP bucket exists and is accessible
- Check service account permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure no credentials are committed
5. Submit a pull request

## 📄 License

[Add your license information here]

## 🔗 Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [Google Cloud Storage](https://cloud.google.com/storage/docs)
- [GCP Authentication](https://cloud.google.com/docs/authentication)