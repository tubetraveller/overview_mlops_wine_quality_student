import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.data.data_validation import DataValidation
from custom_logger import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        '''
        To be completed.
        Define a ConfigurationManager object which will then call the data validation config method to which in
        turn will be used to define the DataValidation object. Then we'll be able to use the validate_all_columns
         ethod.
        '''

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj =  DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e