from langchain_openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.config import config
import json

def analyze_content(content: str) -> dict:
    # Initialize OpenAI LLM
    try:
        llm = ChatOpenAI(model_name="gpt-4o-mini",temperature=0, openai_api_key=config.OPENAI_API_KEY)
        
        prompt_template = """
        You are an expert website analyzer. Using the provided homepage content, answer these questions:
        
        1. What industry does the website belong to?
        2. What is the size of the company (e.g., small, medium, large)?
        3. Where is the company located?
        
        Website Content:
        {content}
        
        Provide answers **strictly in this exact JSON format**(without any extra formatting like backticks or text outside the JSON):
        {{
            "industry": "INDUSTRY_PLACEHOLDER",
            "company_size": "COMPANY_SIZE_PLACEHOLDER",
            "location": "LOCATION_PLACEHOLDER"
        }}
        Use the following phrases for missing information:
        - For industry: "Industry not mentioned in the content"
        - For company size: "Company size not mentioned in the content"
        - For location: "Location not mentioned in the content"

        Return only the JSON object. Do not include backticks, explanations, or any other text.
        """
        
        prompt = PromptTemplate(template=prompt_template, input_variables=["content"])
        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.invoke(content)
        try:
            response = json.loads(result.get("text"))
            return {
                "industry": response.get("industry"),
                "company_size": response.get("company_size"),
                "location": response.get("location"),
            }
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse AI response: {e}")
    except Exception as e:
        raise e