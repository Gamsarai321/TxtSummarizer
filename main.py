import src.textSummarizer

from src.textSummarizer.logging import logger

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
    