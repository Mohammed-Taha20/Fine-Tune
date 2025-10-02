from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

router = APIRouter()

# Model paths
BASE_MODEL_PATH = r"/content/drive/MyDrive/Fine Tune adapter/base_model"
FINETUNED_MODEL_PATH = r"/content/drive/MyDrive/Fine Tune adapter/finetuned_model"

# Load both models + tokenizers
base_tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH)
finetuned_tokenizer = AutoTokenizer.from_pretrained(FINETUNED_MODEL_PATH)

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

finetuned_model = AutoModelForCausalLM.from_pretrained(
    FINETUNED_MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

class RequestData(BaseModel):
    prompt: str

@router.post("/compare/")
async def compare_models(data: RequestData):
    # Base model
    base_inputs = base_tokenizer(data.prompt, return_tensors="pt").to(base_model.device)
    base_outputs = base_model.generate(**base_inputs, max_new_tokens=100)
    base_text = base_tokenizer.decode(base_outputs[0], skip_special_tokens=True)

    # Fine-tuned model
    finetuned_inputs = finetuned_tokenizer(data.prompt, return_tensors="pt").to(finetuned_model.device)
    finetuned_outputs = finetuned_model.generate(**finetuned_inputs, max_new_tokens=100)
    finetuned_text = finetuned_tokenizer.decode(finetuned_outputs[0], skip_special_tokens=True)

    return {
        "base_model": base_text,
        "finetuned_model": finetuned_text
    }
