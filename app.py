import streamlit as st
import openai
import os
from text_summarizer.functions import summarize


try: 
    with st.sidebar:
        openai.api_key = st.text_input("OpenAI API Key", key="file_qa_api_key", type="password")
        "[View the source code](https://github.com/el-grudge/text-summarizer)"

    # initialize a state variable
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text Summarizer")

    with st.form(key='my_form'):
        # augmented prompt
        input_text = st.text_area(label="Enter full text:", value="", height=250)
        col1, col2, col3 = st.columns(3)
        # model
    
        with col1:
            model = st.selectbox(
                'Select the model',
                ('Babbage','Davinci','GPT 3.5'),
                help='TBD'
            )
        # temperature
        with col2:
            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=2.0,
                value=1.0,
                step=0.1,
                key="temperature",
                help="TBD"
            )
        # max_token
        with col3:
            max_tokens = st.number_input(
                'Set the number of words',
                max_value=2048,
                value=1000,
                step=1,
                help='TBD'
            )
        submit_button = st.form_submit_button('Submit')

    if submit_button:
        summarize(input_text, model, temperature, max_tokens)
        # configure text area to populate with current state of summary
        output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)

except:
    st.write('There was an error =(')