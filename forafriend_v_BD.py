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
        time.sleep(0.300)

def typewriterH(text: str):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.header(curr_full_text)
        time.sleep(0.300)

#Access DATA
def loadLottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#lottie_friend = loadLottie("https://lottie.host/b2f4d0c2-6e24-4afe-947f-a34f8c9cfabe/CllA22C3w0.json")
lottie_HappyBDAY = loadLottie("https://lottie.host/79c257cb-de36-47d2-860c-8bbf83d2c051/0jYoVA3vfB.json")
lottie_HappyGIFT = loadLottie("https://lottie.host/fbc30805-92fa-4583-8128-5d9e09d15168/vLsve7ZZRA.json")

# #HEADER
# with st.container():
#     st.subheader("WHY")
#     st.title("WHY NOT")
#     para1 = "WHAT THE HELL BN"
#     st.write(typewriter(para1))

# BODY

leftC,midC,rightC = st.columns(3)
with midC:
    typewriterH("     Hi Venuri :wave: :heart_on_fire:")
    typewriterH("-------  We meet AGAIN!!  -----")

    typewriterH("This Time It Is To Say")
    #typewriterH(".......................")

with st.container():
    st_lottie(lottie_HappyBDAY,height="100",key="BDAY")
    time.sleep(4.5)

leftC,midC,rightC = st.columns(3)
with midC:
    typewriterH("MANY MORE RETURNS OF THE DAY VENURI!")
    #typewriterH(" !.........")
    #typewriterH("............................")

    st_lottie(lottie_HappyGIFT, height ="500", key= "GIFT")

leftC1,midc1,rightC1 = st.columns([.3,.4,.3])
with midc1:
    #typewriterH("With a bunch of fond memories")
    typewriterH("_-Rashid-_") 
    typewriterH(":heart_on_fire: Buddy from SLIIT :heart_on_fire:")