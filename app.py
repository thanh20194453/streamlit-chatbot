import os
import sys

import openai
import streamlit as st
from streamlit_chat import message

repo_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(repo_dir, "src"))
from config import config
from conversation import init, reset, show_history
from models import get_model, generate_response, calculate_cost


# Initialize session state and set openAI API key
init()
openai.api_key = config.OPENAI_API_KEY


# Setting page title and header
st.set_page_config(
    page_title="VMO Chatbot", 
    page_icon="💬",
    layout="wide"
)
st.markdown(
	body="<h1 style='text-align: center;'>VMO - Demo chatbot 💭</h1>",
	unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
	st.title("Conversation")
	model_name = "GPT-3.5"
	model = get_model(model_name)
	temperature = 0.9
	counter_placeholder = st.empty()

	if config.DEBUG_MODE:
		counter_placeholder.write(
			f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
	
	clear_button = st.button("Start a new conversation", key="clear")


# reset everything
if clear_button:
	reset()
	if config.DEBUG_MODE:
		counter_placeholder.write(
			f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")

# container for chat history
response_container = st.container()
if st.session_state['generated'] == []:
	with response_container:
		message(message=config.DEFAULT_MESSAGE, avatar_style="bottts")

# container for text box
container = st.container()
with container:
	with st.form(key='my_form', clear_on_submit=True):
		user_input = st.text_area("Message:", key='input', height=100)
		submit_button = st.form_submit_button(label='Send')

	if submit_button and user_input:
		with st.spinner("Generating response..."):
			output, total_tokens, prompt_tokens, completion_tokens = generate_response(
				prompt=user_input,
				temperature=temperature,
				model=model
			)
		st.session_state['past'].append(user_input)
		st.session_state['generated'].append(output)
		st.session_state['model_name'].append(model_name)
		st.session_state['total_tokens'].append(total_tokens)

		cost = calculate_cost(model_name, total_tokens,
							prompt_tokens, completion_tokens)
		st.session_state['cost'].append(cost)
		st.session_state['total_cost'] += cost

if st.session_state['generated'] != []:
	with response_container:
		show_history(counter_placeholder)
