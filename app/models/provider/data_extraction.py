from app.models.template import data_extraction
from app.models.schema import NewsDetails
from app.controllers.DataController import parse_json , raw_data
import json,os
import tqdm
from app.helpers.config import get_settings

settings  = get_settings()

cloud_model_id = "gpt_4o"
price_per_1m_input_token = 0.015
price_per_1m_output_token = 0.600

prompt_tokens = 0
completion_tokens = 0

save_to = os.path.join(settings.data_dir,"fine_tune_dataset", "sft.jsonl")

idx=0
for story in tqdm(raw_data):

    sample_details_extraction_messages = data_extraction.detailed_extraction_template(story['content'])


    response = openai_client.chat.completion.create(
        messages = sample_details_extraction_messages
        model=cloud_model_id,
        temperature=0.2,
    )

    if response.choices[0].finish_reason !="stop":
        prompt_tokens += response.usage.prompt_tokens
        continue

    llm_response = response.choices[0].message.content
    llm_response_dict = parse_json(llm_response)

    if not llm_response_dict:
        continue

    with open(save_to,"a",encoding="utf-8") as f:
        f.write(json.dumps({
            "id": idx,
            "story": story['content'].strip(),
            "task": "Extrat the story details into a JSON.",
            "output_scheme": json.dumps( NewsDetails.model_json_schema(), ensure_ascii=False ),
            "response": llm_response_dict,
        }, ensure_ascii=False, default=str)  + "\n" )

    idx += 1
    prompt_tokens += response.usage.prompt_tokens
    completion_tokens += response.usage.completion_tokens

    if(idx % 3) == 0:
        cost_input = (prompt_tokens / 1_000_000) * price_per_1m_input_token
        cost_output = (completion_tokens / 1_000_000) * price_per_1m_output_token
        total_cost = cost_input + cost_output

        print(f"Iteration {idx}: Total Cost = ${total_cost:.4f} ")