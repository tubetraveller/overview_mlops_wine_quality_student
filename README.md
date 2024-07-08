Setting up a project on wine-quality step by step 🚀

Welcome to the setup guide! Here, we'll outline the steps needed to configure and implement the various first stages of the MLOps pipeline. Follow along and fill in the details as you proceed through each step in the workflow_steps.ipynb notebook.

You can start by getting familiar with the architecture of the project: 

```bash
+---.dvc
|  
+---.github
|   \---workflows
+---data
|           
+---logs
|       
+---metrics
+---notebooks
|       workflow_steps.ipynb
|       
+---src
|   |   common_utils.py
|   |   config.py
|   |   config.yaml
|   |   config_manager.py
|   |   entity.py
|   |   __init__.py
|   |   
|   +---app
|   |       app.py
|   |       
|   +---data_module_def
|   |   |   data_ingestion.py
|   |   |   data_transformation.py
|   |   |   data_validation.py
|   |   |   schema.yaml
|   |   |   __init__.p
|   |           
|   +---models_module_def
|   |       model_evaluation.py
|   |       model_trainer.py
|   |       params.yaml
|   |       __init__.py
|   |       
|   +---pipeline_steps
|   |       prediction.py
|   |       stage01_data_ingestion.py
|   |       stage02_data_validation.py
|   |       stage03_data_transformation.py
|   |       stage04_model_trainer.py
|   |       stage05_model_evaluation.py
|   |       __init__.py
|           
+---templates
|       index.html
|       login.html
|       register.html
|       results.html
|       
+---users
|   |   users.json
| 
|   .dvcignore
|   .gitignore
|   custom_logger.py
|   dvc.lock
|   dvc.yaml
|   README.md
|   requirements.txt
|   tree
|   __init__.py
|  
```


Step 1: Update Configuration Files
Update config.yaml 📂

Define directories for each step (data ingestion, validation, transformation, training, evaluation).
Example:
yaml
Copier le code
data_ingestion:
  root_dir: "data_ingestion"
  source_URL: "http://example.com/data.zip"
  local_data_file: "data/raw_data.zip"
  unzip_dir: "data/raw"
Update params.yaml 📊

Set model hyperparameters.
Example:
yaml
Copier le code
ElasticNet:
  alpha: 0.1
  l1_ratio: 0.5
Update schema.yaml 🗃️

Define data types for each column.
Example:
yaml
Copier le code
COLUMNS:
  column_name_1: "float"
  column_name_2: "int"
Step 2: Implement Common Utilities
In src/common_utils.py, add reusable functions:

read_yaml(filepath: str) -> dict
create_directories(paths: List[str])
save_json(path: str, data: dict)
These utilities will streamline the loading of configurations and ensure necessary directories are created.

Step 3: Define Configuration Classes
In src/entity.py, define dataclasses for configuration objects:

DataIngestionConfig
DataValidationConfig
DataTransformationConfig
ModelTrainerConfig
ModelEvaluationConfig
Refer to the corresponding cell in workflow_steps.ipynb for class definitions.

Step 4: Configuration Manager
In src/config_manager.py, create a class to manage configurations:

Read paths from config.yaml
Read hyperparameters from params.yaml
Create necessary folders
Example:

python
Copier le code
class ConfigurationManager:
    def __init__(self, config_filepath, params_filepath, schema_filepath):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        # additional initializations
Refer to the notebook for full implementation details.

Step 5: Data Ingestion
In src/data_module_def/data_ingestion.py, create the Data Ingestion class:

Download the dataset
Unzip the dataset
Example methods:

python
Copier le code
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        # download logic here
    
    def extract_zip_file(self):
        # unzip logic here
Step 6: Data Validation
In src/data_module_def/data_validation.py, create the Data Validation class:

Validate columns against the schema
Example method:

python
Copier le code
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        # validation logic here
Step 7: Data Transformation
In src/data_module_def/data_transformation.py, create the Data Transformation class:

Split the data into training and test sets
Example method:

python
Copier le code
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        # splitting logic here
Step 8: Model Training
In src/models_module_def/model_trainer.py, create the Model Trainer class:

Train the model using specified hyperparameters
Example method:

python
Copier le code
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        # training logic here
Step 9: Model Evaluation
In src/models_module_def/model_evaluation.py, create the Model Evaluation class:

Evaluate the model and log metrics
Example method:

python
Copier le code
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def log_into_mlflow(self):
        # evaluation and logging logic here
Step 10: Pipeline Steps
In src/pipeline_steps, create scripts for each step to instantiate and run the processes:

stage01_data_ingestion.py
stage02_data_validation.py
stage03_data_transformation.py
stage04_model_trainer.py
stage05_model_evaluation.py
Example:

python
Copier le code
# stage01_data_ingestion.py
from config_manager import ConfigurationManager
from data_module_def.data_ingestion import DataIngestion

config = ConfigurationManager().get_data_ingestion_config()
data_ingestion = DataIngestion(config=config)
data_ingestion.download_file()
data_ingestion.extract_zip_file()
Step 11: Link Steps with DVC
Create a dvc.yaml file to link and manage the steps with DVC.

Example:

yaml
Copier le code
stages:
  data_ingestion:
    cmd: python src/pipeline_steps/stage01_data_ingestion.py
    deps:
      - src/data_module_def/data_ingestion.py
      - config.yaml
    outs:
      - data/raw
Congratulations! 🎉 You have now a structured and well-defined MLOps project. Each step is modularized, making it easy to maintain, extend, and scale your machine learning pipeline. Use the workflow_steps.ipynb as a reference to implement each component and happy coding!






