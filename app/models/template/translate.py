import json
from schema import translatedStory

def translation_template(story: str, Targeted_language: str = "English"):
    detailed_extraction_message = [
        {
            "role": "system",
            "content": "\n".join([
                "you are a professional translation tool",
                "you will be provided with a text associated with pydantic schema",
                "you have to translate into 'Targeted language'",
                "follow the provided schema to generate a JSON",
                "do not generate an introduction or conclusion"
            ])
        },
        {
            "role": "user",
            "content": "\n".join([
                "## Story:",
                story.strip(),
                "",
                "## Pydantic Details:",
                translatedStory.schema_json(),
                "",
                "## Targeted language:",
                Targeted_language,
                "",
                "## Story Details:",
                "```json"
            ])
        }
    ]
    # For Qwen, you likely want a chat-style prompt
    prompt = ""
    for msg in detailed_extraction_message:
        prompt += f"<|im_start|>{msg['role']}\n{msg['content']}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"
    return prompt