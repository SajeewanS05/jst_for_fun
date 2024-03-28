import streamlit as st
import time

st.set_page_config(page_title="Thank You Everyone", page_icon=":heart:")

def typewriter(text: str):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / 3)

def typewriterH(text: str):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.subheader(curr_full_text)
        time.sleep(1 / 5)

leftC,midC,rightC = st.columns(3)
with midC:
    typewriterH(":heart: Hello Guys, Welcome to my Thank You Page :heart:")
    typewriter(' I would like to Thank You All from the bottom of my heart for the wonderful wishes for my birthday')
    typewriter('I will not forget you all in my life')
    typewriter('Thank you for making this day wonderful')
    typewriter('And finally May God Bless You All')
    typewriter('Bye now, Lets meet again sometime soon')
    typewriter('With love: Rashid :heart:')
