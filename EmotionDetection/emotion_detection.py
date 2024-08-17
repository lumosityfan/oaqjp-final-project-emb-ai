import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze }}
    response = requests.post(url, json = input_json, headers=header)
    formatted_response = json.loads(response.text)
    max_emotion_score = 0
    max_emotion = None
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None 
    if response.status_code == 400:
        return {'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': max_emotion
               }
    elif response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        for emotion in emotions:
            if emotions[emotion] > max_emotion_score:
                max_emotion_score = emotions[emotion]
                max_emotion = emotion
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]
    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
            }