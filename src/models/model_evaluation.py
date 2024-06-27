import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import dagshub
import joblib
from pathlib import Path
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.entity import ModelEvaluationConfig
from src.common_utils import save_json

# To fill in with your repo information
dagshub.init(repo_owner='', repo_name='', mlflow=True)

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        '''
        To be completed.
        This function will calculate and return the rmse, mae and r2.
        '''

        return rmse, mae, r2
    
    def log_into_mlflow(self):
        '''
        To be completed.
        This function will load the test set and the trained model and use the dagshub mlflow uri
        to track the metrics of our model. For this ze will need to make predictions on the test set 
        and use the previous function (eval_metrics) to evaluate the rmse, mae and r2.
        Additionally, we'll save these metrics as a dictionary on a json file. You can use the function 
        found on src/common_utils, save_json.
        Once again you can use the src/config.yaml file to help you with the attributes.
        To use mlflow you can use the methods mlflow.set_registry_uri, mlflow.log_params, mlflow.log_metric and mlflow.sklearn.log_model.
        '''

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Making predictions

            # Saving metrics as local

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case.

                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")

            else:
                mlflow.sklearn.log_model(model, "model")           