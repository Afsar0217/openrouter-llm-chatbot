import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

# --- OpenRouter LLM setup ---
llm = ChatOpenAI(
    openai_api_key="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",  # 🔁 REPLACE with your actual API key
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="mistralai/mistral-7b-instruct",
    temperature=0.7
)

# --- Prompt Template ---
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question:\n{question}"
)

# --- LangChain QA Chain ---
chain = LLMChain(llm=llm, prompt=prompt)

# --- Streamlit UI ---
st.title("🔍 Ask Me Anything (Powered by OpenRouter)")

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Thinking..."):
        response = chain.run({"question": query})
    st.success("Answer:")
    st.write(response)
