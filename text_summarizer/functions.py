import openai
import streamlit as st


def summarize(prompt, model, temperature, max_tokens):
    augmented_prompt = f'summarize this text: {prompt}'
    models = {
        'Babbage': 'babbage-002',
        'Davinci': 'davinci-002',
        'GPT 3.5': 'gpt-3.5-turbo-instruct'
    }

    try:
        st.session_state["summary"] = openai.Completion.create(
            model=models[model],
            prompt=augmented_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')