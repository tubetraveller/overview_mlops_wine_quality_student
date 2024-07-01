import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from custom_logger import logger
from src.config_manager import ConfigurationManager
from src.data_module_def.data_ingestion import DataIngestion

# logging the parent directory
logger.info(f"Parent folder: {parent_folder}")

# Define stage name
STAGE_NAME = "Data Ingestion stage"



