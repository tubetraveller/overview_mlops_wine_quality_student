import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.data_module_def.data_transformation import DataTransformation
from custom_logger  import logger

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        '''
        To be completed.
        We first read the status.txt to see if our data is valid or not.
        If it's valid, then  we'll define de DataTransformation object through the configuration 
        manager. We'll then call the train_test_splitting method from the DataTransformation object.
        '''
        try:
            with open(Path("data/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()

            else:
                raise Exception("Your data schema is not valid")
        
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj =  DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e