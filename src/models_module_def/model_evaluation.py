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
dagshub.init(repo_owner='your_username', repo_name='your_repo', mlflow=True)
