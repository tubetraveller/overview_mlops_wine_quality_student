import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        '''
        To be completed.
        Read the train set, define an elastic net model and fir it on the train set.
        Once the model has been trained, save it as a .joblib file on the folder created for this purpose. 
        You can have a look on the src/config.yaml file to help you.
        '''
        X_train = pd.read_csv(self.config.train_X_path)
        y_train = pd.read_csv(self.config.train_y_path)

        lr = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))