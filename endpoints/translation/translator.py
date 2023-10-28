from googletrans import Translator
from flask import Flask, request, jsonify


def translate(phrase, language):

    translator = Translator()

    out = translator.translate(phrase, dest=language)

    return out.text