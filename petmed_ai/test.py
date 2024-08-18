import os
from pathlib import Path

def list_txt_files(data_dir="petmed_ai\data"):
    paths = Path(data_dir).glob('**/*.csv')
    for path in paths:
        yield str(path)

def load_txt_files(data_dir="petmed_ai\data"):
    print(data_dir)
    docs = []
    paths = list_txt_files(data_dir)
    for path in paths:
        print(f"Loading {path}")
        #loader = TextLoader(path)
        #docs.extend(loader.load())
    return docs

load_txt_files()

