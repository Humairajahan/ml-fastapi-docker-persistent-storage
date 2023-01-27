import pickle
import re

__version__ = "0.1.0"

with open(f"./app/model_weight/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portuguese",
    "Russian",
    "Spanish",
    "Swedish",
    "Tamil",
    "Turkish",
]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]