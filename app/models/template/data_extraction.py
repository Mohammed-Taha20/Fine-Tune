import json
from schema import NewsDetails
def detailed_extraction_template(story: str):
    
    detailed_extraction_message = [{
        "role" : "system",
        "content": "/n".join([
            "you are a professional llm details extraction tool",
            "you will be provided with a text assosiated with pydantic schema",
            "generate the output in the same story language",
            "you have to extract JSON details from the text according to pydantic details",
            "extract details as mentioned in text",
            "do not generate and introduction or conclusion"
        ])
    },
        {
            "role": "user",
            "content" : "/n".join([
                "## Story:",
                story.strip(),
                "",
                "## Pydanic Details:",
                json.dump(NewsDetails.schema_json(), ensure_ascii= False),
                "",
                "## Story Details:",
                "```json"
            ])
        }]