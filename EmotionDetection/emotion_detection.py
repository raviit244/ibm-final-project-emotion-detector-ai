import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_library = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_library['anger']
    disgust_score = emotion_library['disgust']
    fear_score = emotion_library['fear']
    joy_score = emotion_library['joy']
    sadness_score = emotion_library['sadness']
    dom_score = anger_score
    dom_name = 'anger'
    for pair in list(emotion_library.items()):
        if pair[1] > dom_score:
            dom_score = pair[1]
            dom_name = pair[0]
    formatted_dict = {
        'anger': anger_score, 
        'disgust': disgust_score, 
        'fear': fear_score, 
        'joy': joy_score, 
        'sadness': sadness_score, 
        'dominant_emotion': dom_name
        }

    return formatted_dict