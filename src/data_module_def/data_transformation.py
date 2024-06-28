import os
import pandas as pd
from sklearn.model_selection import train_test_split
from custom_logger import logger
from src.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        '''
        To be completed. 
        Read the winequality-red.csv file.
        Create the X and y dataframes, the target variable is "quality".
        Split into X_train, X_test, y_train, y_test and save them into the appropriate folder.
        '''

        logger.info("Splitted data into training and test sets")
        logger.info(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        logger.info(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

        print(X_train.shape, y_train.shape)
        print(X_test.shape, y_test.shape)