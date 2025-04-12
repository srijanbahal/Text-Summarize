from textSummarizer.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipline
from textSummarizer.logging import logger



stage_name = "Data Ingestion Stage"
try:
    logger.info(f"{'='*20} {stage_name} {'='*20}")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f"{'='*20} {stage_name} completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e