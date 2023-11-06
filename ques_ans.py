import streamlit as st
from transformers import pipeline  #pip install transformers

model=pipeline(task='question-answering')

st.title("Question Anwering Model")
st.text("This model uses transformers.")

def main():
	context=st.text_input("Enter Context here:")
	query=st.text_input("Enter Query here: ")
	if context and query:
		answer = model(question=query, context=context)
		st.text(answer["answer"])

main()