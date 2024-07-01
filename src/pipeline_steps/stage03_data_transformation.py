import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.data_module_def.data_transformation import DataTransformation
from custom_logger  import logger

STAGE_NAME = "Data Transformation stage"
