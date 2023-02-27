import openai
import streamlit as st


def summarize(prompt, model, temperature, max_tokens):
    augmented_prompt = f'summarize this text: {prompt}'
    models = {
        'Ada': 'text-ada-001',
        'Babbage': 'text-babbage-001',
        'Curie': 'text-curie-001',
        'Davinci': 'text-davinci-003'
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
