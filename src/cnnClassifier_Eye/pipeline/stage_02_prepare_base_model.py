from cnnClassifier_Eye.config.configuration import ConfigurationManager
from cnnClassifier_Eye.components.prepare_Base_model import PrepareBaseModel
from cnnClassifier_Eye import logger


STAGE_NAME='Model BUilding Pipeline'

class ModelBuildingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj =  ModelBuildingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

   


