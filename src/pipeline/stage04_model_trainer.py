import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.models.model_trainer import ModelTrainer
from custom_logger import logger

STAGE_NAME = "Model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        '''
        To be completed.
        We'll once again use the configuration manager, this time to instantiate the 
        ModelTrainer object from which we'll use the train method.
        '''

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x========x")
    except Exception as e:
        logger.exception(e)
        raise e