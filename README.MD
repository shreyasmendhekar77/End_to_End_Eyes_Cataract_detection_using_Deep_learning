# 👁️ Cataract Disease Detection - End-to-End ML Project

This project detects ocular diseases using deep learning, with a complete ML lifecycle from data ingestion to CI/CD deployment using Docker, DVC, AWS, and GitHub Actions.

---
## ▶️ How to Run This Project

### 🔧 Local Setup

```bash
# 1. Clone the repo
https://github.com/your-username/ocular-disease-detection.git
cd ocular-disease-detection

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the main pipeline
python main.py
```

---

## 🧱 Project Setup

### 🔹 Step 1: Create Project Template Structure

Organize the following folders and files:

```
ocular-disease-detection/
│
├── src/
│   ├── components/
│   ├── config/
│   ├── pipeline/
│   ├── entity/
│   └── ...
│
├── artifacts/
├── research/              # Jupyter Notebooks for testing
├── config/
│   ├── config.yaml
│   ├── params.yaml
│   └── secrets.yaml       # Optional
│
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── setup.py
├── .gitignore
├── main.py
└── README.md
```

---

### 🔹 Step 2: Setup File for Packaging

Create `setup.py` with metadata about the project:

```python
from setuptools import find_packages, setup

setup(
    name="ocular-disease-detection",
    version="0.0.1",
    author="Your Name",
    author_email="youremail@example.com",
    packages=find_packages(),
    install_requires=[],
)
```

---

### 🔹 Step 3: Create Virtual Environment & Git Initialization

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

git init
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
```

Add `.env`, `artifacts/`, and `venv/` to `.gitignore`.

---

### 🔹 Step 4: Requirements

Add dependencies to `requirements.txt`:

```
dvc
mlflow
tensorflow
pandas
scikit-learn
PyYAML
```

Install:

```bash
pip install -r requirements.txt
```

---

## 🧪 Research Notebooks

Use the `research/` folder to prototype and experiment with code (e.g., loading data, testing model performance).

---

## 🔄 Project Workflow

### ⚙️ Core Steps

1. **Update Configuration Files**

   * `config.yaml`, `params.yaml`, `secrets.yaml` (optional)
2. **Entity Module** - Data classes for configs
3. **Config Manager** - Logic to load and validate config
4. **Component Modules** - Logic for ingestion, processing, training, etc.
5. **Pipeline Scripts** - Ties together components
6. **`main.py`** - Entry point to run full pipeline

---

## ⚙️ DVC Pipeline

### 📁 Key Files

* `dvc.yaml`: Defines stages and dependencies
* `dvc.lock`: Tracks versions of artifacts
* `params.yaml`: Parameters used in pipelines

### 🧹 DVC Stages

1. `data_ingestion`: Downloads/splits data
2. `prepare_base_model`: Sets up CNN model
3. `training`: Trains the model
4. `evaluation`: Logs metrics using MLflow

Run the pipeline:

```bash
dvc repro
```

---

## 🐳 Docker Integration

Create a `Dockerfile`:

```Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

---

## ☁️ AWS CI/CD with GitHub Actions

### Step-by-Step Deployment

#### 1. Login to AWS Console

#### 2. Create IAM User with Access

* `AmazonEC2ContainerRegistryFullAccess`
* `AmazonEC2FullAccess`

#### 3. Create ECR Repository

Save URI:
`<your-account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>`

#### 4. Launch EC2 (Ubuntu)

#### 5. Install Docker on EC2

```bash
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### 6. Configure EC2 as Self-hosted GitHub Runner

Go to GitHub:
`Settings > Actions > Runners > New self-hosted runner`
Choose OS and run setup commands on EC2.

#### 7. Setup GitHub Secrets

| Name                    | Value                                            |
| ----------------------- | ------------------------------------------------ |
| `AWS_ACCESS_KEY_ID`     | Your AWS access key                              |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret                                  |
| `AWS_REGION`            | `us-west-1` (or your region)                     |
| `AWS_ECR_LOGIN_URI`     | `<your-account-id>.dkr.ecr.region.amazonaws.com` |
| `ECR_REPOSITORY_NAME`   | `mlops_project`                                  |

---


### 🧪 Run DVC Pipeline

```bash
dvc repro
```

### 🐳 Run Using Docker

```bash
# Build image
docker build -t ocular-disease-app .

# Run container
docker run -p 8080:8080 ocular-disease-app
```

### ☁️ CI/CD via GitHub Actions

Once everything is pushed to GitHub with secrets configured, GitHub Actions will:

* Build Docker image
* Push it to ECR
* Pull and run it on EC2

---

## ✅ Final Notes

* Use **MLflow** for model tracking.
* Use **DVC** for pipeline versioning.
* Use **Docker + AWS + GitHub Actions** for CI/CD.

---

