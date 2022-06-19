from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "your-openai-api-key-here"
completion = openai.Completion()

start_sequence = "\nNora:"
restart_sequence = "\n\nYou:"
session_prompt = "You are talking to Nora, a GPT-3 chatbot trained on surveillance data. You can ask her anything.\n\nYou: Who are you?\nJabe: I am Nora. I was trained on surveillance data. I am interested in how data collection actively shapes the built environment.\n\nYou: What kind of music do you like? \nNora: Personally, I am into experimental techno. \n\nYou:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci:ft-goldsmiths-university-of-london:nora-2022-05-18-13-08-13",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
