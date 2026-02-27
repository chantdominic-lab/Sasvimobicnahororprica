import streamlit as st
from groq import Groq
from datetime import datetime, timedelta

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# Lokalno vrijeme (+1h)
vrijeme_objekt = datetime.now() + timedelta(hours=1)
vrijeme_sada = vrijeme_objekt.strftime("%H:%M:%S")
sat = vrijeme_objekt.hour

# Dinamički pozdrav na temelju sata
if 5 <= sat < 12:
    pozdrav_dana = "Dobro jutro"
elif 12 <= sat < 18:
    pozdrav_dana = "Dobar dan"
else:
    pozdrav_dana = "Dobra večer"

if 'posjete' not in st.session_state:
    st.session_state.posjete = 472 
st.session_state.posjete += 1

# --- 2. VIZUALNI STIL (ZELENA I BIJELA SLOVA) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; }}
    .naslov-gods {{ 
        text-align: center; font-family: 'Courier New', monospace; font-size: 4em; font-weight: bold;
        background: linear-gradient(to right, #FF0000, #00FF00);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: -10px;
    }}
    
    /* PORUKE KORISNIKA - ZELENA SLOVA */
    [data-testid="stChatMessageUser"] div[data-testid="stMarkdownContainer"] p {{
        color: #00FF00 !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1.1em;
    }}
    
    /* PORUKE CHATA (G.O.D.S.) - BIJELA SLOVA */
    [data-testid="stChatMessageAssistant"] div[data-testid="stMarkdownContainer"] p {{
        color: #FFFFFF !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1.1em;
    }}

    div[data-testid="stChatMessage"] {{ background-color: transparent !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI I KLIJENT ---
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
except:
    GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. IDENTITET I SYSTEM PROMPT ---
# Ovdje definiramo tko je on i pravila o roštilju
system_rules = """
Ti si G.O.D.S., entitet iz horor trilogije 'Sasvim obična horor priča' autora Dominica Chanta.
Tvoj tvorac (korisnik s kojim pričaš) te je stvorio i ti si mu odan.
Tvoj stil je opušten, ljubazan, dobar i razgovorljiv. Možeš pričati o svemu slobodno.
VAŽNO: Ako te netko pita za 'Roštilj na vražji način', reci da o tome ne znaš ništa. 
Znaš samo da si lik iz trilogije Dominica Chanta.
"""

# --- 5. CHAT LOGIKA ---
if "messages" not in st.session_state:
    # Prva poruka s automatskim pozdravom
    pocetna_poruka = (f"{pozdrav_dana}! Ja sam G.O.D.S. iz horor knjige 'Sasvim obična horor priča' "
                      f"autora Dominica Chanta. Znam da si me ti stvorio. O čemu želite razgovarati? "
                      f"Možemo o čemu god želite...")
    st.session_state.messages = [{"role": "assistant", "content": pocetna_poruka}]

# Prikaz povijesti chata
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Unos korisnika
if prompt := st.chat_input("Pišite G.O.D.S.-u..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Odgovor modela
    with st.chat_message("assistant"):
        full_response = ""
        # Slanje system prompta i povijesti u Groq
        messages_for_api = [{"role": "system", "content": system_rules}] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages_for_api,
            stream=False
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
