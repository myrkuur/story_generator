from pathlib import Path
import gdown
import os

from init import MODEL_DIR, GDRIVE_ID

from keytotext import trainer


def download_from_google_drive(dest):
    for name, id in GDRIVE_ID.items():
        output = Path(dest) / name
        if output.name not in os.listdir(output.parent):
            print(name)
            gdown.download(id=id, output=str(output), quiet=False)
    return dest


MODEL_DIR.mkdir(parents=True, exist_ok=True)
download_from_google_drive(MODEL_DIR / 'keytotext')

model = trainer()
model.from_pretrained(MODEL_DIR / 'keytotext')

def predict(keywords, sep):
    kw = keywords.split(sep)
    pred = model.predict(kw, use_gpu=False)
    return pred
