Occular Disease detection 

Procedure to implement the  END-END project.

------------------- Setup for the Project ( file creation to install dependecies all the content...)--------------------------

Step 1 :- 
Create the template file - it contains the required files to for implementation the template structure is -

Step 2:- 
Steup file for the packaging our code - which contains the necessary info about the latest version of model.

Step 3:- 
Create the Virtual environment and Initiate the git repo for version controlling. 
(Download the python .gitignore file and add the environment name in it and all the files that you don't want to
add in the repo.)

Step 4:-
Requirement.txt file - which contains the necessary libraries/ Dependences for the project.

Step 5:- 
Run the requiremnts.txt file for setup and installing the necessary libraries.

--------------------- Setup for Project is Done ----------------------------------------------------------------------------------------

Implement Data Ingestion to Model Evaluation 

Research Notebook -It is used to implement the commands for testing purpose - 
All files have similar procedure to do the testing research part- 

## Workflow of the Project 
Update config.yaml
Update secrets.yaml [Optional]
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml



--------------------------------
Entity file -  It contains the configuration for the different file paths.

---------------------------------
Config /Configuration file - it contains the necessary function to get the file paths and other parameters 

-----------------------------------
Components - It contains all the operations about the particular task - 
for data ingestion - get the necessary path and variables for config file and download the data , store it etc.

--------------------------------------
Pipeline file - for each operation , it is just joining the differernt modular classes with respective the arguments.

---------------------------------------


1.Data Ingestion -
contains the code to take the data form different sourece and storing it to the Artifacts file.
- Update the  Workflow part ...

2.Data Preprocessing validation - 
Do the necessary preprocessing as per requirement.

3.Model Training .
- Take the model from API  ( transfer learning )/ Create your own model 
- Use the params.yaml for paramters of the model.

4.Model Evaluation and Experiment tracking ...
- Use the Mlflow for experiment tracking
- Upadte the username and other credentials like - 



DVC pipeline ...
DVC (Data Version Control) pipelines are used to track and automate machine learning workflows, ensuring that your data, code, and model artifacts are versioned and reproducible. A DVC pipeline consists of stages, each representing a step (like preprocessing, training, or evaluation), connected by dependencies (data files, scripts, etc.).

🛠️ Basic Components of a DVC Pipeline
dvc.yaml – Defines stages of the pipeline and their dependencies/outputs.

dvc.lock – Records exact versions of inputs/outputs used in the last run.

params.yaml – (Optional) Stores hyperparameters or config variables.



DVC pipeline has 4 stages:

data_ingestion – Splits raw data into train/test sets.

prepare_base_model – Builds a base CNN model using parameters.

training – Trains the model with the prepared data and base model.

evaluation – Evaluates the trained model and logs metrics (scores.json).

Each stage uses specific scripts, configs, parameters, and outputs artifacts for the next stage.


Docker ...






# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 507319107220.dkr.ecr.us-west-1.amazonaws.com/mlops_project

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-west-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = 


