# prompts.py
from langchain.prompts import PromptTemplate

description_prompt = PromptTemplate.from_template(
    "Write me a description for a TikTok about {topic}")

script_prompt = PromptTemplate.from_template(
    "Write me a script for a TikTok given the following description: {description}")