from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.models.template.translate import translation_template
import torch

router = APIRouter()

# Model paths
BASE_MODEL_PATH = r"/content/drive/MyDrive/Fine Tune adapter/base_model"
FINETUNED_MODEL_PATH = r"/content/drive/MyDrive/Fine Tune adapter/finetuned_model"

# Load both models + tokenizers
base_tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH, trust_remote_code=True)
finetuned_tokenizer = AutoTokenizer.from_pretrained(FINETUNED_MODEL_PATH, trust_remote_code=True)

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
    targeted_language: str = "English"

@router.post("/compare/")
async def compare_models(data: RequestData):
    # Use the same prompt for both models
    prompt = translation_template(data.prompt, data.targeted_language)

    # Base model
    base_inputs = base_tokenizer(prompt, return_tensors="pt").to(base_model.device)
    base_outputs = base_model.generate(
        base_inputs.input_ids,
        max_new_tokens=1024,
        do_sample=False
    )
    base_generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(base_inputs.input_ids, base_outputs)
    ]
    base_text = base_tokenizer.batch_decode(base_generated_ids, skip_special_tokens=True)[0]
    print("Base output:", base_text)

    # Finetuned model (same prompt and logic)
    finetuned_inputs = finetuned_tokenizer(prompt, return_tensors="pt").to(finetuned_model.device)
    finetuned_outputs = finetuned_model.generate(
        finetuned_inputs.input_ids,
        max_new_tokens=1024,
        do_sample=False
    )
    finetuned_generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(finetuned_inputs.input_ids, finetuned_outputs)
    ]
    finetuned_text = finetuned_tokenizer.batch_decode(finetuned_generated_ids, skip_special_tokens=True)[0]
    print("Finetuned output:", finetuned_text)

    return {
        "base_model": base_text,
        "finetuned_model": finetuned_text
    }