from flask import Flask, render_template, request
import json
from googletrans import Translator


# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from ibm_watson.natural_language_understanding_v1
#     import Features, EmotionOptions

# authenticator = IAMAuthenticator('{apikey}')
# natural_language_understanding = NaturalLanguageUnderstandingV1(
#     version='2019-07-12',
#     authenticator=authenticator
# )

# natural_language_understanding.set_service_url('{url}')

# response = natural_language_understanding.analyze(
#     html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
#     features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

# print(json.dumps(response, indent=2))

app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/receiveLang', methods=['GET', 'POST'])
def receive_lang():
    data = json.loads(str(request.get_data(), 'utf-8'))['data']
    lang = json.loads(str(request.get_data(), 'utf-8'))['lang']
    print(f'Receive Data: {data} in {lang}')
    translator = Translator()
    return translator.translate(data, dest=lang).text
