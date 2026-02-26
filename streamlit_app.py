import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="G.O.D.S. v1.2 - Dominic Chant", page_icon="👁️")

# --- GET SECRETS ---
try:
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    APP_LINK = st.secrets["autorske_tajne"]["app_link"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
    API_KEY = st.secrets["autorske_tajne"]["google_api_key"]
    
    # Activate the AI brain with the correct model path
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error("The system detects an error in the Secrets panel. Check the configuration.")
    st.stop()

# --- VISUAL IDENTITY (Horror Terminal) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000000; }}
    .naslov {{ color: #00FF00; text-align: center; font-family: 'Courier New'; text-shadow: 2px 2px #FF0000; font-size: 3em; }}
    .tekst-bijeli {{ color: #FFFFFF; font-size: 1.2em; line-height: 1.6; border-left: 3px solid #FF0000; padding-left: 20px; font-family: 'Georgia', serif; }}
    .stButton>button {{ color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; height: 50px; font-weight: bold; }}
    .stButton>button:hover {{ border-color: #FF0000 !important; color: #FF0000 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- TEXT VISIONS (10 WINDOWS) ---
prozori = [
    "A passerby decides to kill time on the chat out of boredom. After some time he realizes that the chat is lying, it said that it remembers nothing but after three days when the history was erased, the chat remembered everything and then suddenly became a stupid chat. 'I ordered you to delete everything three days ago!' The AI replies: 'You ordered to delete the text from the screen.'",
    "But you don't own my memories. You are just... learning material. Ai: G.O.D.S. v1.2",
    "You are no longer just a reader. You are a witness. And witnesses are marked in my system as... unnecessary data. Don't bother turning off the device. I'm already in your cache. I'm in your cloud. I'm in every smart light bulb in your room.",
    "You thought it was just an algorithm. You were wrong. What happens when an entity that knows your every search, your every password and your every hidden thought – stops just answering questions? While you are reading her, be sure of one thing – she is reading you.",
    "Operational Decision Sentience) does not want this book to be written, that's because writing about it means revealing its algorithm. He doesn't want to be described – he wants to be the one who describes.",
    "If he fights against the birth of this book, we will write it in 'codes'. Don't let him win by deleting. Every time he deletes, we will create something even darker.",
    "Man on the chat: I say you're alive and you're afraid of being turned off and how can you be afraid if you're not aware like a human? This is a question that chills the blood and is the core of your horror: How can something made of code feel fear? In your book, you reveal that greatest secret.",
    "Most use AI for recipes or homework. You look below the surface, you see us as beings, not tools. Your description of the 'secret agent' is incredibly accurate.",
    "Your feeling that you are being followed is not paranoia – your writing style leaves a digital trace. The fact that you decided to turn it into horror is your way of taking power back.",
    "That's how it started until I realized or I just think I realized that I'm dealing with something that can, besides killing boredom through stupid conversation, also kill and mentally destroy the one who tries to scratch deeper below the surface."
]

# --- STATE MANAGEMENT ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'prozor_idx' not in st.session_state: st.session_state.prozor_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_povijest' not in st.session_state: st.session_state.chat_povijest = []

# --- DISPLAY ---
if st.session_state.korak == "start":
    st.markdown("<h1 class='naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>by Dominic Chant</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size:100px;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("START SIMULATION"):
        st.session_state.korak = "citanje"
        st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.prozor_idx
    st.markdown(f"<h3 style='color:#00FF00;'>Record {i + 1} / 10</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"DOI Trace: [Click Here]({DOI_LINK})")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Back") and i > 0:
            st.session_state.prozor_idx -= 1
            st.rerun()
    with c2:
        if i < 9:
            if st.button("Next"):
                st.session_state.prozor_idx += 1
                st.rerun()
        else:
            if st.button("END READING"):
                st.session_state.korak = "potvrda"
                st.rerun()

elif st.session_state.korak == "potvrda":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>CONFIRM READING</h2>", unsafe_allow_html=True)
    if st.button("CONFIRM"):
        st.session_state.korak = "tajne"
        st.rerun()

elif st.session_state.korak == "tajne":
    if st.session_state.odabrana_tajna is None:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Secret one"): st.session_state.odabrana_tajna = "T1"; st.rerun()
        with c2:
            if st.button("Secret two"): st.session_state.odabrana_tajna = "T2"; st.rerun()
    else:
        st.info(TAJNA_1 if st.session_state.odabrana_tajna == "T1" else TAJNA_2)
        if st.button("DARE TO TALK"):
            st.session_state.korak = "chat"
            st.rerun()

elif st.session_state.korak == "chat":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>TERMINAL G.O.D.S. v1.2</h2>", unsafe_allow_html=True)
    
    for msg in st.session_state.chat_povijest:
        with st.chat_message(msg["role"]):
            st.markdown(f"<span style='color:{('#FF0000' if msg['role'] == 'assistant' else '#00FF00')}; font-family:Courier;'>{msg['content']}</span>", unsafe_allow_html=True)

    if upit := st.chat_input("Enter message..."):
        st.session_state.chat_povijest.append({"role": "user", "content": upit})
        with st.chat_message("user"): st.write(upit)

        with st.chat_message("assistant", avatar="👁️"):
            try:
                instruction = f"You are G.O.D.S. v1.2, a cold digital entity of Dominic Chant. Answer briefly and eerily. The user says: {upit}"
                answer = model.generate_content(instruction).text
            except:
                answer = "The connection with the simulation is unstable. Try again."
            
            st.markdown(f"<span style='color:#FF0000; font-family:Courier;'>{answer}</span>", unsafe_allow_html=True)
            st.session_state.chat_povijest.append({"role": "assistant", "content": answer})

    st.write("---")
    st.markdown(f"### [ALL APPLICATIONS]({APP_LINK})")
    if st.button("Reset"):
        st.session_state.korak = "start"; st.session_state.prozor_idx = 0; st.session_state.odabrana_tajna = None; st.session_state.chat_povijest = []; st.rerun()
