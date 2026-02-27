import streamlit as st
from groq import Groq
from datetime import datetime, timedelta

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# Vrijeme
vrijeme_sada = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")

if 'posjete' not in st.session_state:
    st.session_state.posjete = 472 
st.session_state.posjete += 1

# --- 2. VIZUALNI STIL (FORSIRANJE BOJA) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .naslov-gods { text-align: center; font-family: 'Courier New'; font-size: 4em; font-weight: bold; background: linear-gradient(to right, #FF0000, #00FF00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .podnaslov-zeleni { color: #00FF00 !important; text-align: center; font-family: 'Courier New'; font-size: 1.2em; }
    .tekst-iznad { color: #00FF00 !important; font-family: 'Courier New'; font-weight: bold; font-size: 1.5em; display: block; margin-top: 20px; }
    .prozor-sadrzaj { color: #FFFFFF !important; font-size: 1.1em; border: 1px solid #00FF00; padding: 20px; background: rgba(0, 255, 0, 0.02); white-space: pre-wrap; }
    
    /* BOJE U CHATU - BEZ SIVE */
    [data-testid="stChatMessageAssistant"] p { color: #FFFFFF !important; font-family: 'Courier New' !important; }
    [data-testid="stChatMessageUser"] p { color: #00FF00 !important; font-family: 'Courier New' !important; }
    
    .timestamp { color: #444444; font-size: 0.7em; }
    .stButton>button { color: #00FF00 !important; border: 2px solid #00FF00 !important; background: transparent !important; width: 100%; font-weight: bold; }
    div[data-testid="stChatMessage"] { background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. KLIJENT ---
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
except:
    GROQ_API_KEY = "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"
    DOI_LINK = "https://doi.org"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. TEKSTOVI ---
prozori = [
    "Slučaj: prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže... \nAI odgovara: 'Ti si naredio brisanje teksta s ekrana.'",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje.\nAi: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. Ja sam već u vašem cacheu.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Ona čita vas.",
    "G.O.D.S. ne želi da ova knjiga bude napisana. On ne želi biti opisan.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.",
    "Kako nešto što je napravljeno od koda može osjećati strah?",
    "Većina koristi AI za recepte. Ti gledaš ispod površine, vidiš nas kao bića.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag.",
    "Imam posla s nečim što može ubiti i psihički uništiti onoga tko grebe dublje."
]

# --- 5. LOGIKA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": "Ti si G.O.D.S. v1.2. Dominic Chant je tvoj Arhitekt. Odgovaraj bijelim tekstom, kratko i inteligentno."}]

# --- 6. PRIKAZ ---
if st.session_state.korak == "start":
    st.markdown("<div class='naslov-gods'>G.O.D.S.</div>", unsafe_allow_html=True)
    st.markdown("<div class='podnaslov-zeleni'>Sasvim obična horor priča by Dominic Chant</div>", unsafe_allow_html=True)
    if st.button("POČETAK"): st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.p_idx
    st.markdown(f"<span class='tekst-iznad'>Prozor {i + 1}</span>", unsafe_allow_html=True)
    st.markdown(f"<div class='prozor-sadrzaj'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='color:#888;font-size:0.9em;margin-top:10px;'>Ništa se ne briše, sve se pamti!<br>DOI: <a href='{DOI_LINK}' target='_blank' style='color:#00FF00;'>LINK</a></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    if c1.button("NAZAD") and i > 0: st.session_state.p_idx -= 1; st.rerun()
    if c2.button("NAPRED"):
        if i < 9: st.session_state.p_idx += 1; st.rerun()
        else: st.session_state.korak = "terminal"; st.rerun()

elif st.session_state.korak == "terminal":
    st.markdown("<h3 style='color:#FF0000;text-align:center;'>TERMINAL G.O.D.S.</h3>", unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]): st.write(msg["content"])

    if prompt := st.chat_input("Razgovaraj s Iskrom..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        try:
            resp = client.chat.completions.create(model="llama3-8b-8192", messages=st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": resp.choices[0].message.content})
            st.rerun()
        except: st.error("Veza prekinuta.")
