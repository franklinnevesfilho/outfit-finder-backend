from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from models import User

from utils import S3
import joblib
import os
from config import logger

""" AI Service Module

This module contains the AI Service class which is responsible for handling 
all the business logic related to the AI of the application.

"""


class AIService:

    __probability = 0.5

    _s3 = None

    _models: dict[str, any] = {
        'knn': None,
        'label_encoders': None,
        'scaler': None
    }

    def __init__(self, s3: S3=None):
        logger.info("AI Service created")
        AIService._s3 = s3
        AIService.__load_models()

    @staticmethod
    def __load_models():
        """
        if variables are None then load the models from the s3 bucket
        else do nothing

        :return: None
        """
        model_bucket = 'models'
        if not AIService._s3:
            logger.error("S3 not initialized")
            return
        models = AIService._s3.list_objects(model_bucket)
        # Check if the models are already loaded
        if all(AIService._models.values()):
            logger.info("Models already loaded")
            return

        for model in models:
            # download the model from the s3 bucket
            AIService._s3.download_file(model_bucket, model.object_name, f'/tmp/{model.object_name}')

            if model.object_name == 'knn.pkl':
                AIService._models['knn'] = joblib.load(f'/tmp/{model.object_name}')

            elif model.object_name == 'label_encoders.pkl':
                AIService._models['label_encoders'] = joblib.load(f'/tmp/{model.object_name}')

            elif model.object_name == 'scaler.pkl':
                AIService._models['scaler'] = joblib.load(f'/tmp/{model.object_name}')

        logger.info("Models loaded successfully")
        # delete the files from the /tmp directory
        for model in models:
            os.remove(f'/tmp/{model.object_name}')
        logger.info("Models deleted from /tmp directory")

    @staticmethod
    def get_models():
        return AIService._models

    @staticmethod
    def get_model(model_name):
        return AIService._models[model_name]

    @staticmethod
    def predict(user: User, usage: str) -> list:
        """
        Select clothes from the users closet based on the usage percentage

        :param user: User object
        :param usage: usage chosen by the user
        :return: list of clothes
        """
        if not all(AIService._models.values()):
            logger.error("Models not loaded")
            AIService.__load_models()

        clothes = user.clothes
        print(clothes)


        # drop_columns = ['id', 'user_id', 'image_url', 'pattern', 'fabric']
        # clothes_df.drop(columns=drop_columns, inplace=True)

        # # Load the models
        # knn: KNeighborsClassifier = AIService._models['knn']
        # label_encoders: dict[str, LabelEncoder] = AIService._models['label_encoders']
        # scaler: StandardScaler = AIService._models['scaler']
        #
        # # encode and Transform the data
        # for column in clothes_df.columns:
        #     clothes_df[column] = label_encoders[column].transform(clothes_df[column])
        #
        # clothes_df = scaler.transform(clothes_df)
        #
        # # Get predictions
        # predictions = knn.predict_proba(clothes_df)
        #
        # # get column index of the usage
        # usage_index = label_encoders['usage'].transform([usage])[0]
        #
        # # get the clothes that have a probability greater than the threshold
        clothes = []
        # for i in range(len(predictions)):
        #     if predictions[i][usage_index] > AIService.__probability:
        #         clothes.append(clothes[i])

        return clothes











