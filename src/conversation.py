import streamlit as st
from streamlit_chat import message

from config import config


def init():
	# Initialise session state variables
	if "generated" not in st.session_state:
		st.session_state["generated"] = []
	if "past" not in st.session_state:
		st.session_state["past"] = []
	if "messages" not in st.session_state:
		st.session_state["messages"] = [
			{"role": "system", "content": config.FIRST_PROMPTS}
		]
	if "model_name" not in st.session_state:
		st.session_state["model_name"] = []
	if "cost" not in st.session_state:
		st.session_state["cost"] = []
	if "total_tokens" not in st.session_state:
		st.session_state["total_tokens"] = []
	if "total_cost" not in st.session_state:
		st.session_state["total_cost"] = 0.0
 

def reset():
	st.session_state['history'] = []
	st.session_state['generated'] = []
	st.session_state['past'] = []
	st.session_state['messages'] = [
		{"role": "system", "content": config.FIRST_PROMPTS}
	]
	st.session_state['number_tokens'] = []
	st.session_state['model_name'] = []
	st.session_state['cost'] = []
	st.session_state['total_cost'] = 0.0
	st.session_state['total_tokens'] = []
	

def show_history(counter_placeholder):
	for i in range(len(st.session_state['generated'])):
		message(st.session_state["past"][i], is_user=True, avatar_style="personas")
		message(st.session_state["generated"][i], avatar_style="bottts")

		if config.DEBUG_MODE:
			st.write(
				f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
			counter_placeholder.write(
				f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
