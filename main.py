from cnnClassifier_Eye.pipeline.stage_01_data_ingeation import DataIngestionTrainingPipeline
from cnnClassifier_Eye.pipeline.stage_02_prepare_base_model import ModelBuildingPipeline
from cnnClassifier_Eye.pipeline.stage_03_model_train import ModelTrainingPipeline
from cnnClassifier_Eye.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from cnnClassifier_Eye import logger

STAGE_NAME='Data Ingestion'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Building'


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj =  ModelBuildingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Model Training'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Evaluation'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


