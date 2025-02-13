import os
import streamlit as st

from llama_index.llms.openai import OpenAI

llm_name = "gpt-4o-mini"
model_temperature = 0.8

st.title("🐘 AI Immunisation/MCH Nurse 🐘")
st.markdown(
    (
        "This demo allows you to query a LLM about immunisation and MCH topics."
    )
)

query_tab, = st.tabs(["Query"])

with query_tab:
    st.subheader("Query")
    st.markdown(
        (
            f"This is a simple wrapper around OpenAI's {llm_name} model."
        )
    )

    query_text = st.text_input("Ask a question:")
    if query_text:
        with st.spinner("Generating answer..."):
            llm = OpenAI(model=llm_name, temperature=model_temperature, api_key=os.environ["OPENAI_API_KEY"])
            response = llm.complete(query_text)
        st.markdown(str(response))