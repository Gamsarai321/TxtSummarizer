
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
# import src.textSummarizer
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

logger.info("Welcome to our custom logging")

from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>  {STAGE_NAME}  <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" {STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} due to error: {str(e)}")
    raise e 
    
    
    
    

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>  {STAGE_NAME}  <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f" {STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} due to error: {str(e)}")
    raise e 