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

    def __init__(self, s3: S3 = None):
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
        else:
            if not all(AIService._models.values()):
                logger.info("Loading models")

                models = AIService._s3.list_objects(model_bucket)

                try:
                    for model in models:
                        # download the model from the s3 bucket
                        AIService._s3.download_file(model_bucket, model.object_name, f'/tmp/{model.object_name}')

                    AIService._models['knn'] = joblib.load('/tmp/knn.joblib')
                    AIService._models['label_encoders'] = joblib.load('/tmp/label_encoders.joblib')
                    AIService._models['scaler'] = joblib.load('/tmp/scaler.joblib')
                    logger.info("Models loaded successfully")

                    for model in models:
                        os.remove(f'/tmp/{model.object_name}')

                    logger.info("Models deleted from /tmp directory")

                except FileNotFoundError:
                    logger.info("Models not found in /tmp directory")
            else:
                logger.info("Models already loaded")

    @staticmethod
    def get_models():
        return AIService._models

    @staticmethod
    def get_model(model_name):
        return AIService._models[model_name]

    @staticmethod
    def predict(user: User, usage: str, season: str) -> list:
        """
        Select clothes from the users closet based on the usage percentage

        :param user: User object
        :param usage: usage chosen by the user
        :param season: season chosen by the user
        :return: list of clothes
        """
        if not all(AIService._models.values()):
            logger.error("Models not loaded")
            AIService.__load_models()

        clothes = user.clothes
        if not clothes:
            logger.error("User has no clothes")
            return []

        # create a dataframe with the clothes
        clothes_df = pd.DataFrame([
            {
                'gender': user.gender,
                'category': cloth.category,
                'style': cloth.style,
                'color': cloth.color,
                'season': season
            } for cloth in clothes
        ])

        # print to visualize the dataframe
        for column in clothes_df.columns:
            print(column)
            print(clothes_df[column])

        # Load the models
        knn: KNeighborsClassifier = AIService._models['knn']
        label_encoders: dict[str, LabelEncoder] = AIService._models['label_encoders']
        scaler: StandardScaler = AIService._models['scaler']

        # Transform the data
        for column in clothes_df.columns:
            if column in label_encoders:
                clothes_df[column] = label_encoders[column].transform(clothes_df[column])

        clothes_df = scaler.transform(clothes_df)

        # Predict the clothes
        predictions = knn.predict_proba(clothes_df)
        print(predictions)

        if usage == 'any':
            return clothes
        else:
            # Select the clothes based on the usage
            try:
                user_usage = label_encoders['usage'].transform([usage])[0]
            except KeyError:
                logger.error("Usage not found")
                return []

            predicted_clothes = []
            for i in range(len(predictions)):
                if predictions[i][user_usage] > AIService.__probability:
                    predicted_clothes.append(clothes[i])

            return predicted_clothes











