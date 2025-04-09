from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class TextParsing(BaseModel):
    summary: str = Field(description="大V个人简介")
    facts: List[str] = Field(description="大V的特点")
    interest: List[str] = Field(description="这个大V可能感兴趣的事情")
    letter: List[str] = Field(description="一篇联络这个大V的邮件")


    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "interest": self.interest,
            "letter": self.letter,
        }


letter_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=TextParsing
)