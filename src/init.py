from pathlib import Path


GDRIVE_ID = {
    "config.json": "1-bsiApO-1sI1fo8jhuLYKaNYivuKJTS6",
    "pytorch_model.bin": "1-t6iLqm3HN9c0sK2IIfUnvUl_r8JJV-B",
    "special_tokens_map.json": "1-ihWuW9XfeQ1WDY269kqXdTUMU6d0q2L",
    "spiece.model": "1-dksQk90TV4B4kKBpmifF0o3s47KRnBb",
    "tokenizer_config.json": "1-nT7Q7-dy0I0MZQCvieaGr9n7z4GC4ex",
    "tokenizer.json": "1-ce0_szwGZPY_2U0T6Klb1JQ2Qv80GJN"
}

DIR = Path(__file__).absolute().parent.parent
MODEL_DIR = DIR / 'models'