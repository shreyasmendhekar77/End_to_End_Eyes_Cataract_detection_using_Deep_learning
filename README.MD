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


Docker ...


CICD pipeline ...



AWS Deployment ...