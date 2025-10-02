from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

router = APIRouter()

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# === CONFIG ===
BASE_MODEL_PATH = "/content/drive/MyDrive/models/base_model"
FINETUNED_MODEL_PATH = "/content/drive/MyDrive/models/finetuned_model"

# === Load Models ===
print("Loading base model...")
base_tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Loading fine-tuned model...")
finetuned_tokenizer = AutoTokenizer.from_pretrained(FINETUNED_MODEL_PATH)
finetuned_model = AutoModelForCausalLM.from_pretrained(
    FINETUNED_MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

# === FastAPI App ===
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/predict")
async def predict(request: PromptRequest):
    prompt = request.prompt

    # Base model response
    base_inputs = base_tokenizer(prompt, return_tensors="pt").to(base_model.device)
    base_outputs = base_model.generate(**base_inputs, max_new_tokens=200)
    base_text = base_tokenizer.decode(base_outputs[0], skip_special_tokens=True)

    # Fine-tuned model response
    finetuned_inputs = finetuned_tokenizer(prompt, return_tensors="pt").to(finetuned_model.device)
    finetuned_outputs = finetuned_model.generate(**finetuned_inputs, max_new_tokens=200)
    finetuned_text = finetuned_tokenizer.decode(finetuned_outputs[0], skip_special_tokens=True)

    return {
        "base_output": base_text,
        "finetuned_output": finetuned_text
    }
