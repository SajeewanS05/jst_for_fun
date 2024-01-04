import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="HI Venuri!", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def typewriter(text: str):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.write(curr_full_text)
        time.sleep(1 / 30)

def typewriterH(text: str):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.header(curr_full_text)
        time.sleep(1 / 5)

#Access DATA
def loadLottie(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_friend = loadLottie("https://lottie.host/b2f4d0c2-6e24-4afe-947f-a34f8c9cfabe/CllA22C3w0.json")

# #HEADER
# with st.container():
#     st.subheader("WHY")
#     st.title("WHY NOT")
#     para1 = "WHAT THE HELL BN"
#     st.write(typewriter(para1))

# BODY

leftC,rightC = st.columns(2)
with leftC:
    typewriterH("Hi Venuri :wave:")


with rightC:
    st_lottie(lottie_friend,height="100",key="coding")

with leftC:
    para1 = "I hope this letter finds you in good spirits. I've been doing some thinking and couldn't help but put pen to paper to share a few things with you."
    typewriter(para1)
    para2 = "You, my friend, have been a constant source of goodness and warmth in my life. Whether it was the good times or the not-so-great ones, you were always there, being a great friend. Your ability to respect others, listen, and lend a helping hand is something I've always admired."
    typewriter(para2)
    para3 = "I know I might sound a bit sentimental, but hey, it's true! You're like this amazing mix of optimism, flexibility, and planning – qualities that make you truly one of a kind. And yes, sorry for noticing all these things so much, but they truly make you the wonderful person you are"
    typewriter(para3)
    para4 = "Remember those times when, despite your crazy schedule, you'd still find time to party and enjoy? That's one of the many things I'd love to learn from you. People say I'm not the most entertaining person, but you always managed to bring a good time, and I appreciate that more than you know."
    typewriter(para4)
    para5 = "Now, about that Y1S2 episode I've been carrying this weight of regret. I messed up, and I want to apologize sincerely. I let my emotions get the best of me, and it wasn't fair to you. I hope you can find it in your heart to forgive me. Lessons were learned, scars were made, and I wish I could turn back time."
    typewriter(para5)
    para6 = "I also wanted to share that I had big hopes for our friendship, like the ones I have with Kith and Thinu. But with you, I feel like I stumbled a bit. I regret that, truly. And with you about to fly off, I felt it was now or never to get these words out."
    typewriter(para6)

para7 = "You have a heart of gold and a soul that's truly beautiful. Keep being that amazing person, find the balance in life, achieve all those great things you dream of, and, hey, maybe find someone special (if you haven't already!). Don't forget to have fun, remember the big guy upstairs, and, as always, spread that happiness around."
typewriter(para7)
para8 = "I'm not sure if this letter will reach you, but I'm glad I had you as a friend during those tough times. Wishing you all the best in this new chapter of your life. I might not have aced this letter due to those darn exams, but one thing's for sure I won't forget you."
typewriter(para8)

leftC1,midc1,rightC1 = st.columns(3)
with midc1:
    typewriterH("With a bunch of fond memories")
    typewriterH("Rashid") 
    typewriterH("Your Buddy from SLIIT :heart_on_fire::partying_face:")