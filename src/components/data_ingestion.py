##this file is used to split the data in order to train the model
## to run this file use this command:  python -m src.components.data_ingestion
import os
import sys
sys.path.append(r'P:/Projects/ML_Projects') 
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass   ##Decorators can be used to add functionality to existing functions without modifying their source code.
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    #all outputs will be stored in artifacts folder
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')  # here u can replace the path and u can read the db from mongodb or mysql iteself)
            logging.info('Read the dataset as dataFrame')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header = True)
            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
                
            )
        except Exception as e:
            raise CustomException(e,sys)
    
    
if __name__=="__main__":
     obj=DataIngestion()
     train_data,test_data = obj.initiate_data_ingestion()
     
     data_transformation=DataTransformation()
     train_arr, test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
     
     modeltrainer=ModelTrainer()
     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))