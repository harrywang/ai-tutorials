# chain.py
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from dotenv import load_dotenv
from prompts import description_prompt, script_prompt
import langchain
langchain.verbose = True
# loads the .env file
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
description_chain = LLMChain(llm=llm, prompt=description_prompt, verbose=True)
#output = description_chain.predict(topic="Cats are cool")
#print('********', output)

# new code below this line
script_chain = LLMChain(llm=llm, prompt=script_prompt)
#script = script_chain.predict(description=output, verbose=True)
#print('********', script)

tiktok_chain = SimpleSequentialChain(chains=[description_chain, script_chain], verbose=True)

script = tiktok_chain.run("cats are cool")

print(script)