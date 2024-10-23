import openai
import streamlit as st


models_dict = {
    "GPT-3.5": "gpt-3.5-turbo",
    "GPT-4 (use your own key)": "gpt-4",
    "Claude Instant v1.3": "claude-instant-v1",
    "Claude v1.3": "claude-v1",
    "SD v2": "stabilityai/stable-diffusion-2",
    "SD v2.1": "stabilityai/stable-diffusion-2-1",
    "SD v1.5": "runwayml/stable-diffusion-v1-5",
    "Openjourney (SD)": "prompthero/openjourney",
}

def get_model(model_name):
	return models_dict.get(model_name, "gpt-3.5-turbo")


def get_models_list():
    return tuple(models_dict.keys())


def generate_response(prompt, temperature=0.9, model="gpt-3.5-turbo"):
	st.session_state['messages'].append({"role": "user", "content": prompt})

	completion = openai.ChatCompletion.create(
		model=model,
		messages=st.session_state['messages'],
		temperature=temperature
	)
	response = completion.choices[0].message.content
	total_tokens = completion.usage.total_tokens
	prompt_tokens = completion.usage.prompt_tokens
	completion_tokens = completion.usage.completion_tokens
	return response, total_tokens, prompt_tokens, completion_tokens


def calculate_cost(model_name, total_tokens, prompt_tokens, completion_tokens):
	# from https://openai.com/pricing#language-models
	if model_name == "GPT-3.5":
		cost = total_tokens * 0.002 / 1000
	else:
		cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000
	return cost
