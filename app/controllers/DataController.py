import json_repair
import json
import os
from dotenv import load_dotenv
load_dotenv()

data_dir = os.getenv("data_dir")
base_model_id = os.getenv("base_model_id")

device = os.getenv("device")

def raw_data():
    raw_data_path = os.path.join(data_dir, "fine_tune_dataset","news-sample.jsonl")

    raw_data = []
    for line in open(raw_data_path, "r"):
        if line.strip() == "":
            continue
    raw_data.append(json.loads(line.strip()))
    
    
def parse_json(text):
    try:
        return json_repair.loads(text)
    except:
        return None