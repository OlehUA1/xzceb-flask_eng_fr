
"""language_translator en->fr & fr->en"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']



authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    """language translator en->fr"""
    #write the code here
    translation = language_translator.translate(
    text = englishText,
    model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    frenchText = translation['translations'][0]['translation']
    return frenchText


def french_to_english(frenchText):
    """language translator fr->en"""
    #write the code here
    translation = language_translator.translate(
    text = frenchText,
    model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    englishText = translation['translations'][0]['translation']
    return englishText
