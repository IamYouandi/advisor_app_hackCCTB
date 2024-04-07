import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from io import BytesIO
import openai
import os
from tool.llm import LlmEngine


# API_KEY
def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']

def get_text(text_file):
  text = text_file.read()
  decoded_text = text.decode('utf-8')
  return decoded_text
  

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def st_first():
    st.set_page_config(page_title="👩‍⚕️ MH Advisor",
                       layout="wide",
                       page_icon="🧊",
                       initial_sidebar_state="expanded"
                       )
    st.header("MH Advisor 👩‍⚕️")

    with open("texts/MH Advisor_Tell us about yourself.txt") as file:
        st.download_button(
            label="Tell us about yourself - Click and Download the file for us to know you better",
            data=file,
            file_name = 'MH Advisor_Tell us about yourself.txt'
            )    

def main():
  st_first()
  # Uploading file in the web
  text_file = st.file_uploader("Upload the Text file with your responses, please", type="txt")
  openai.api_key = get_openai_key()
  if text_file is not None:
    text = get_text(text_file)
    chunks = get_text_chunks(text)
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # 1st Prompt sent to OpenAI printing the output in the stdout
    user_question = "Act as a psychotherapist focused in the humanist approach as Humanistic psycologists: Gordon Allport, Abraham Maslow o Carl Rogers junto a Ludwig Bingswanger, Medar Boss, Rollo May, Victor Frankl, Eric Fromm o Ronald Laing. Make quotations inspired in their work and point of view. In the vast landscape of the internet, it's understandable to seek solace and understanding in times of mental distress. As a mental health advisor grounded in humanistic principles, you’re here to provide a supportive and nonjudgmental space for you to explore your thoughts, feelings, and concerns Avoid possible triggering content and extreme diagnosis, the text provided has to be charming, and looking for caring about the mental state of the person, and based on their responses in the file. Advise also that seeking support is a sign of strength, not weakness. If you ever feel overwhelmed or in need of guidance, don't hesitate to reach out. You deserve to be seen, heard, and supported every step of the way. With warmth and understanding. based on the questions and answers in the file, provide general insights about the person and what can do to feel better or steps to improve their mental state and health customized based on the person answers. Follow this steps Find the person answers in the file, interpretate them as indicated, make a personalized out put. In the output print the name of the person. Find the Person answers are on the file provided, also avoid use a firm at the end"
    docs = knowledge_base.similarity_search(user_question)
    llm = LlmEngine()
    chain = llm.get_qa_chain(knowledge_base)
    with get_openai_callback() as cb:
        response = chain({"query": user_question})
        print(cb)  
    st.write(response['result'])

# Buttons for recommendations
    chunks_string = ' '.join(chunks)
    concatenated_chunks = "This is the person information" + chunks_string
    literature_clicked = st.button('Click for Literature recommendations', key='1')
    if literature_clicked:
        prompt = concatenated_chunks + "This is your task: Please, Recommend at least 3 literature resources based on the previous information provided of a person feelings and diagnosis. The target is this particular person that is looking for mental health help online avoid possible triggering content and made a humanistic approach that benefit the ask other for help and promote therapy. Provide resources that made auto reflexion. Start the output with “These resources offer gentle exercises, mindful practices, and heartfelt reflections to help you cultivate self-awareness, self-compassion, and resilience. Remember, you're not alone, and it's okay to seek support when you need it. Take care of yourself, dear one."
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(prompt, embeddings)
        docs = knowledge_base.similarity_search(prompt)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
            response1 = chunks
            response = chain({"query": prompt})
            print(cb)  
        st.write(response['result'])
    
    series_clicked = st.button('Click for Series recommendations', key='2')
    if series_clicked:
        prompt = concatenated_chunks + "Based on the information provided by the person, please recommend at least 3 Series for him to watch and improve his mental health state"
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(prompt, embeddings)
        docs = knowledge_base.similarity_search(prompt)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
            response = chain({"query": prompt})
            print(cb)  
        st.write(response['result'])

    emergency_clicked = st.button('Click for Emergency recommendations', key='3')
    if emergency_clicked:
        prompt = concatenated_chunks + "Based on the location information provided by the person, please provide at least 3 emergency numbers in his location for him to call to get support to improve his mental health state"
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(prompt, embeddings)
        docs = knowledge_base.similarity_search(prompt)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
            response = chain({"query": prompt})
            print(cb)  
        st.write(response['result'])
    
    sites_clicked = st.button('Click for Web Sites recommendations', key='4')
    if sites_clicked:
        prompt = concatenated_chunks + "Based on the information provided by the person, please provide at least 3 web sites for him to check to get valuable information to improve his mental health state"
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(prompt, embeddings)
        docs = knowledge_base.similarity_search(prompt)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
            response = chain({"query": prompt})
            print(cb)  
        st.write(response['result'])

if __name__ == '__main__':
    main()
    st.image('img\sad_face.jpg')
    st.markdown("""
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f5f5f5;
                color: black;
                text-align: center;
            }
        </style>
        <div class="footer">
            <p>Copyright © 2024 MH Advisor | All rights reserved</p>
        </div>
        """, unsafe_allow_html=True)