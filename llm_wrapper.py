import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


class LLMApiWrapper:

    def __init__(self, api_key : str, model : str):
        self.api_key = api_key
        self.model = model

    def process(self):
        pass


class GeminiWrapped(LLMApiWrapper):

    def __init__(self, api_key : str, model : str):
        super().__init__(api_key=api_key, model=model)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=model)
    
    def process(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
