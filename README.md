# CCTB Hackathon Prototype, April 2024
---
![CCTB](https://www.canadianctb.ca/media/2559/cctb_logo_2_white.svg?anchor=center&mode=crop&quality=75&width=244&height=83&rnd=133531514380000000)

## Table of content

- [Theme of The Hackathon](#theme-of-the-hackathon)
  - [About the Application](#start-the-application)
  - [Start the Application](#start-the-application)
- [Walkthrough of Code](#walkthrough-of-code)
  - [advisor_app.py file](#advisor_apppy-file)
  - [llm.py file](#llmpy-file)
- [Team Structure](#ideal-team-structure)
- [FAQ](#faq)
- [Potential Ideas and Directions](#potential-ideas-and-directions)
  - [Domain of Application](#choose-a-domain-of-application)
  - [Technical Improvements](#technical-improvements)
- [Credits](#credit)

## Theme of The Hackathon

Large language models (LLM) are a type of artificial intelligence that can generate human-like text. They have been used to generate text, answer questions, and even write code. 

For example, ChatGPT is one of the most popular LLMs. It is based on the GPT-3 model, which was developed by OpenAI. ChatGPT has been used to create chatbots, answer questions, and generate text. It has been used in a wide range of applications, including customer service, education, and entertainment.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/768px-ChatGPT_logo.svg.png" style="width:200px;"/>
</p>


Meanwhile, building an LLM application is becoming more and more accessible. The goal of this hackathon is to build a prototype of an LLM application that can be used to solve a real-world problem. The modern tools like Langchain, Huggingface, and OpenAI are very helpful to build such an application. On another hand, libraries like Streamlit can be used to create a user-friendly interface for the application, which significantly reduces the idea-to-prototype time.

## About the Application

Mental Health Advisor Web App
This repository contains code for a Mental Health Advisor web application developed during a hackathon focused on LLM + Impactful Creativity themes and technologies. The application utilizes Streamlit for the frontend and leverages OpenAI's large language models (LLMs) for text processing and analysis.

Key Features
1.	File Upload: Users can upload a text file containing their responses, allowing the app to analyze and provide personalized recommendations.
2.	AI-powered Analysis: The app uses OpenAI's LLMs to process and analyze user-provided text, such as personal descriptions and feelings.
3.	Personalized Recommendations: Based on the user's input, the app generates personalized recommendations for literature, series, emergency numbers, and websites to improve mental health.
4.	User Interaction: Users can interact with the app by clicking on different buttons to access specific types of recommendations tailored to their needs.

Implementation Details
•	The application is built using Python and Streamlit for the frontend.
•	OpenAI's LLMs are integrated to process and analyze user-provided text data.
•	The app provides a user-friendly interface for uploading files, receiving recommendations, and displaying relevant information.
•	Recommendations are generated dynamically based on the user's input and are aimed at promoting mental well-being and providing support.

Usage
1.	Clone the repository to your local machine.
2.	Install the required dependencies using pip install -r requirements.txt.
3.	Run the app using streamlit run advisor_app.py.
4.	Answer the initial questionnaire to receive personalized recommendations.
5.	Upload a text file with your responses to get tailored advice and recommendations.


Additional File: Initial Questionnaire and Chat History
The repository also includes a file named initial_questionnaire.py, which handles the initial questionnaire process. Users are asked a series of questions about their demographics, mental state, and areas of concern. Their responses are stored in a chat history file (chat_history.txt), which can be downloaded for reference or further analysis.

Disclaimer
This application is designed for educational and informational purposes only. It does not provide medical advice, diagnosis, or treatment. Users are encouraged to seek professional help for any mental health concerns.


### Start the Application

To use the application, run the `main.py` file with the streamlit CLI (after having installed streamlit): 

```
streamlit run advisor_app.py
```

After a few seconds, a new tab will open in your default browser with the application running. You can then use the application to get the information about your Mental Health.


## Walkthrough of Code

Now let's walk through the code. You may be suprised that the code is very simple.

There are two main files: the [advisor_app](./advisor_app) and the [llm.py](./tool/llm.py) file. 

The `advisor_app.py` file contains the Streamlit application. The application then uses the `llm.py` file to communicate with OpenAI to get the information.


### advisor_app.py file

What's in the advisor_app.py?

1.	Import Statements:
•	The file starts with necessary import statements, including Streamlit (streamlit), dotenv (dotenv), and other modules required for text processing and AI integration.

2.	API Key Retrieval:
•	There is a function get_openai_key() to retrieve the OpenAI API key from the environment variables using dotenv.

3.	Text Processing Functions:
•	get_text(text_file) function reads and decodes text from a provided text file.
•	get_text_chunks(text) function splits the text into smaller chunks for processing.

4.	Streamlit Configuration:
•	The st_first() function configures the Streamlit app's initial settings, such as page title, icon, and header.

5.	Main Function:
•	The main() function is the core of the application.
•	It calls st_first() to set up the Streamlit app.
•	It includes a file uploader (st.file_uploader) to allow users to upload a text file containing their responses.
•	Upon file upload, the app processes the text using OpenAI's language models and generates personalized recommendations based on the user's input.

6.	Recommendation Buttons:
•	The app provides buttons for different types of recommendations, such as literature, series, emergency numbers, and websites.
•	Each button click triggers the generation of specific recommendations based on the uploaded text and user preferences.

7.	Download Button:
•	The app includes a download button (st.download_button) to allow users to download the chat history file containing their responses.

8.	Footer and Image Display:
•	It displays a footer with copyright information and a sad face image using Streamlit's st.image function.

9.	Execution:
•	The if __name__ == '__main__': block ensures that the main() function is executed when the script is run directly.
Overall, app.py combines Streamlit's interactive components with OpenAI's language models to create an engaging and personalized mental health advisor experience for users.


### llm.py file

The `llm.py` file contains only one class `LlmEngine`. 

Its `__init__` method defines which model to use. You can find available models in the [OpenAI documentation](https://platform.openai.com/docs/models). Ideally this is the only place you need to change the `__init__` method.

There are two methods left: `get_qa_chain` and `get_history_chain`. The biggest difference is that at the return line, one uses `RetrievalQA` and another uses `ConversationalRetrievalChain`.  These two methods are the gateway to the OpenAI API.

Both methods create a `prompt_template` variable. This is where prompt engineering happens. The current prompt is very simple. As you may know that with proper prompt crafting, LLM can generate very different and very interesting results.

> One of your team members will spend quite sometime on prompt engineering. It is a very important part of the application. The prompt engineering can be very creative and it can be very challenging. You can find some examples of prompt engineering in the [OpenAI documentation](https://platform.openai.com/docs/guides/prompt-engineering).

The difference between `get_qa_chain` and `get_history_chain` is that the `get_qa_chain` method only asks one question and gets one answer. The `get_history_chain` method need to take the history of the chats, as a list, as an input. If you use the `get_history_chain` method, you need to keep track of the history of the chats and pass it to the `chain()` call at line 58.


## Team Structure

1. Full-Stack Developer - Jhonny Condemarin
2. Full-Stack Developer - Camilo Acevedo
3. Product Manager && Prompt Engineer - Sofia Carrillo


### Domain of Application

1. Mental Health support tool that can automatically provide recommendations by reading your profile, which is evaluated based on specific questions. Please note: this should not replace real therapy

### Technical Improvements

1. The vectorstore can be pre-built so it contains much more information than a single file.
2. The prompt engineering can be much more sophisticated.
3. The UI can be improved significantly.
4. Fine-tune the API calls and the text splitter.
5. Integrate the initial questionnaire with the app
6. Many many others.

## Credit

The prototype was based on an early version of this [project](https://github.com/wsy258-strar/DocGPT). It is then customized for learning purposes.

Thanks go to the authors for their great work.
