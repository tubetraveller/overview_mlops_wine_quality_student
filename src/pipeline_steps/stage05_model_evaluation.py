import sys
from pathlib import Path

# Add parent directory to path
parent_folder = str(Path(__file__).parent.parent.parent)
sys.path.append(parent_folder)

from src.config_manager import ConfigurationManager
from src.models_module_def.model_evaluation import ModelEvaluation
from custom_logger import logger

STAGE_NAME = "Model evaluation stage"
