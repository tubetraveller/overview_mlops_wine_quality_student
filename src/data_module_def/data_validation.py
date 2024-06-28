import pandas as pd
from src.config_manager import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        '''
        To be completed.
        Read the dataset, you can help yourself find the right attributes to do so through the src/config.yaml file
        Check that the columns on the schema.yaml file coincide with those present in the dataset.
        The variable validation_status will return True if the columns coincide, and false if they don't.
        '''
        
        try:
            validation_status = None
            


            return validation_status
        except Exception as e:
            raise e
        