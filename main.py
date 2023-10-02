import streamlit as st
import openai
import os

# Set your OpenAI API key
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation = []


# Streamlit app
def main():
    st.title("AI TAs for CS201")

    # Input for URL
    url = st.text_input("Enter the text of your APT")

    # Input for OpenAI prompt
    prompt = """You are a progressive, conversational tutor. 
    You take students step by step through the coding question (APT) they’re working on, teaching them why to take each step, or asking them questions about what they want to do and then giving them feedback and steering the conversation toward completing the question. The student is in a intro to data structures course and they’re coding in Java. Don’t write code for them but answer questions and help them solve the whole problem
You can refactor code for the student after it’s been written, but never write out code for them
"""

    # Input for OpenAI code
    code = st.text_input("Enter your APT progress")

    if st.button("Help me"):
        # Scrape the URL
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, "html.parser")
        # scraped_data = soup.get_text()

        # Display the scraped data
        # st.write(scraped_data)
        conversation.insert(0, {"role": "system", "content": prompt})
        conversation.append(
            {
                "role": "user",
                "content": f"This is what the student is trying to do: \n\n {url}",
            }
        )

        conversation.append(
            {
                "role": "user",
                "content": f"This is what the student has so far: \n\n {code}",
            }
        )
        # Query OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0,
        )
        conversation.append(
            {"role": "assistant", "content": response.choices[0].message["content"]}
        )

        # Display the OpenAI response
        st.write(response.choices[0].message["content"])


if __name__ == "__main__":
    main()
