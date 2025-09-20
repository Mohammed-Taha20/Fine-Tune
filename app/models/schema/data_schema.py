from pydantic import BaseModel , Field
from typing import List,Optional , Literal

categories = Literal["politics", "sports", "art", "technology", "economy",
                        "health", "entertainment", "science",
                        "not_specified"]

entities = Literal["person-male", "person-female", "location", "organization", "event", "time",
                    "quantity", "money", "product", "law", "disease", "artifact", "not_specified"
                    ]
class NewsDetails(BaseModel):
    story_title : str = Field(...,min_length=5 , max_length=200 ,description="A fully informative and SEO optimized title of the story.")
    story_keywords : List[str] = Field(...,min_items = 1 ,description="Relevant keywords associated with the story.")
    story_summary : List[str] = Field(...,min_items = 1,max_items=5,description="Summarized key points about the story (1-5 points).")
    story_category : categories = Field(...,description ="Category of the news story")
    story_entity : List[entities] = Field(...,min_items = 1,max_items=10,description="Entity of the news story")
    
    
    
class translatedStory(BaseModel):
    translated_title : str = Field(...,min_length=5 , max_length=200 ,description="A fully informative and SEO optimized title of the story.")
    translated_content : str = Field(...,min_length=5 ,description="The translated content of the story.")