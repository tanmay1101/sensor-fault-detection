# sensor-fault-detection

# Folder and Files Structure
1. venv- It is virtual environment that is required to run project
2. requirement.txt- This file contains all the required liberaries and dependencies that we need to install. Please install this file before starting project.
3. setup.py- This file will help us to install any custom codes or liberaries and other dependencies
4. Sensor- This is a package that will be master folder for this project sensor-fault-detection. We will write each code inside this folder only. This folder contains many sub folders for specific task.
  1. Pipeline- In this folder we will write training and testing pipeline codes.
  2. ml- Any custom algorithms, graphs, accuracy metrices will be written and decided in this folder.
  3. entity- To define structure of input and output components.
  4. data_access- To access the data from databases.
  5. constant- 
  6. configuration- To maintain all connection related configuration e.g- kafka or S3 related configurations will be written in this folder, so that we can connect to them.
  components- We will write ML related components here.
  7. Cloud_storage- to upload and download files from S3 or other cloud storage.
5. logger.py/acception.py- to capture all the bugs and mistakes so that we can track them