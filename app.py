import streamlit as st
from process_incoming import inference,create_embedding

st.title("RAG-Based AI Teaching Assistant")

question = st.text_input("Ask a question")

if st.button("Search"):
    if question:
        with st.spinner("Searching in your course..."):
            response = inference(question)
        st.success("Done!")
        st.write(response)