import os 
from cnnClassifier_Eye.config.configuration import ConfigurationManager
from cnnClassifier_Eye.components.model_evaluation import Evaluation
from cnnClassifier_Eye import logger


STAGE_NAME='Model Evaluation Pipeline'

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/shreyasmendhekar77/End_to_End_Eyes_Cataract_detection_using_Deep_learning.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="shreyasmendhekar77"
os.environ["MLFLOW_TRACKING_PASSWORD"]="40a68921fc18c53ca9b654767e357ed1bc9e3903"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

   


