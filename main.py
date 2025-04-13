from textSummarizer.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage02_Data_validation import DataValidationTrainingPipeline



stage_name = "Data Ingestion Stage"
try:
    logger.info(f"{'='*20} {stage_name} {'='*20}")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f"{'='*20} {stage_name} completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e