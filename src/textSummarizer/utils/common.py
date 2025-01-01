import os
import sys

# Add the path to the custom packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

# import textSummarizer
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yamL: Path) -> ConfigBox:
    """reads the yaml file and returns a ConfigBox instance

    Args:
        path_to_yamL (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yamL, 'r') as file:
            content = yaml.safe_load(file)
            if content:
                logger.info(f"yaml file: {path_to_yamL} is loaded successfully")
                return ConfigBox(content)
            else:
                raise ValueError("yaml file is empty")
    except FileNotFoundError as e:
        logger.error(f"File not found: {path_to_yamL}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error parsing yaml file: {path_to_yamL} has YAMLError")
        raise e
    except BoxValueError as e:
        logger.error(f"Error parsing yaml file: {path_to_yamL} has BoxValueError")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading yaml file: {path_to_yamL}")
        raise e
    
    
    
    
@ensure_annotations  
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
        
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory: {path} created successfully")
        except Exception as e:
            logger.error(f"An unexpected error occurred while creating directory: {path}")
            raise e
        
        
        


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in kb
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
    
    