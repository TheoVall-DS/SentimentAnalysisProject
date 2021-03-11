import numpy as np
import joblib

class SentimentClassifier:
    def __init__(self):
        self.model = joblib.load('model/model.joblib')
        self.classes = {1: 'Положительный отзыв', 0: 'Отрицательный отзыв'}

    def getSentiment(self, text):
        try:
            return self.classes[int(self.model.predict([text])[0])]
        except:
            return 'Ошибка'