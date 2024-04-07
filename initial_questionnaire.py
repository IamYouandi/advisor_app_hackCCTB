import streamlit as st

def st_firstt():
    st.set_page_config(page_title="MH Advisor",
                       #layout="wide",
                       page_icon="🧊",
                       initial_sidebar_state="expanded"
                       )

    st.header("MH Advisor 👩‍⚕️")


# List of questions
st_firstt()
questions = [
    "Name:",
    "Age:",
    "Gender:",
    "Job/Occupation:",
    "Marital Status:",
    "How are you feeling today? Is there anything specific on your mind?",
    "Have you been experiencing any changes in your mood or behavior recently?",
    "What do you think might be contributing to your current feelings or struggles?",
    "Have there been any periods in your life where you've struggled with your mental well-being?",
    "Are there any specific areas of your life where you feel you need more support?",
    "Do you feel like your emotions are interfering with your ability to focus or concentrate on tasks?"
]

# Dict to hold the questions and responses
responses = {}

# Iterate over each question
for question in questions:
    # Special handling for the Gender and Marital Status questions
    if question == "Gender:":
        user_response = st.selectbox("Gender:", ["Male", "Female"])
    elif question == "Marital Status:":
        user_response = st.selectbox("Marital Status:", ["Single", "Married", "Divorced", "Widowed"])
    elif question == "Age:":
        user_response = st.number_input("Age:", min_value=0)
    else:
        # Get user response
        user_response = st.text_input(question)

    # If user has responded, store the question and user response in the responses dict
    if user_response:
        responses[question] = user_response

# If all questions have been asked and responses received
if len(responses) == len(questions):
    # Open the text file and write the questions and responses to it
    with open('chat_history.txt', 'w') as f:
        for question, response in responses.items():
            f.write(f"{question}\n{response}\n\n")


# Provide a download link for the chat history file
    st.download_button(label="Download chat history", data=open('chat_history.txt', 'r'), file_name='responses.txt',
                       mime='text/plain')

col1, col2, col3 = st.columns([1, 2, 1])
col2.image("img\sad_face.jpg")

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
