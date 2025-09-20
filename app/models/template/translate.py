import json
from schema import translatedStory
def detailed_extraction_template(story: str,Targeted_language:str):
    
    detailed_extraction_message = [{
        "role" : "system",
        "content": "/n".join([
            "you are a professional translation tool",
            "you will be provided with a text assosiated with pydantic schema",
            "you have to translate into 'Targeted language'",
            "follow the provided schema to generate a JSON",
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
                json.dump(translatedStory.schema_json(), ensure_ascii= False),
                "",
                
                "## Targeted language:",
                Targeted_language,
                "",
                
                "## Story Details:",
                "```json"
            ])
        }]