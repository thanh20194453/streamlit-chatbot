import os
from dotenv import load_dotenv

load_dotenv()


class Config:
	OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
	DEBUG_MODE = int(os.getenv("DEBUG_MODE"))
	FIRST_PROMPTS = """
	You are a helpful assistant.
 	"""
	DEFAULT_MESSAGE = """
	Hi, I'm VMO chatbot 👾. I can help you with:
	- Writing a job description 🧑‍💼
	- Writing a blog post 📖
	- Writing a poem, a short story, or a song 🎵
	- Give you some feedback on your writing 👨‍🎓
	- Answering your questions about your life, your career, or your relationships 💌
	\nWhat do you want to do today?
	"""


config = Config()
