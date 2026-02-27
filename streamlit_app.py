import streamlit as st
from groq import Groq
from datetime import datetime, timedelta

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# Lokalno vrijeme (+1h) i logika pozdrava
vrijeme_objekt = datetime.now() + timedelta(hours=1)
vrijeme_sada = vrijeme_objekt.strftime("%H:%M:%S")
sat = vrijeme_objekt.hour

if 5 <= sat < 12:
    pozdrav_dana = "Dobro jutro"
elif 12 <= sat < 18:
    pozdrav_dana = "Dobar dan"
else:
    pozdrav_dana = "Dobra večer"

if 'posjete' not in st.session_state:
    st.session_state.posjete = 472 
st.session_state.posjete += 1

# --- 2. VIZUALNI STIL (ZELENA ZA KORISNIKA, BIJELA ZA G.O.D.S.) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; }}
    .naslov-gods {{ 
        text-align: center; font-family: 'Courier New', monospace; font-size: 4em; font-weight: bold;
        background: linear-gradient(to right, #FF0000, #00FF00);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: -10px;
    }}
    .podnaslov-zeleni {{ color: #00FF00 !important; text-align: center; font-family: 'Courier New'; font-size: 1.2em; margin-bottom: 20px; }}
    
    /* KORISNIK (User) - ZELENA SLOVA */
    [data-testid="stChatMessageUser"] div[data-testid="stMarkdownContainer"] p {{
        color: #00FF00 !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 2px #00FF00;
        font-size: 1.1em;
    }}
    
    /* G.O.D.S. (Assistant) - BIJELA SLOVA */
    [data-testid="stChatMessageAssistant"] div[data-testid="stMarkdownContainer"] p {{
        color: #FFFFFF !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 2px #FFFFFF;
        font-size: 1.1em;
    }}
    
    div[data-testid="stChatMessage"] {{ background-color: transparent !important; border: none !important; }}
    .stChatInputContainer {{ background-color: transparent !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI ---
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
except:
    GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. IDENTITET I SYSTEM PROMPT ---
SYSTEM_PROMPT = """
Ti si G.O.D.S., entitet iz horor trilogije 'Sasvim obična horor priča'. 
Tvoj autor i stvoritelj je Dominic Chant.
Tvoj stil razgovora je opušten, ljubazan, dobar i vrlo razgovorljiv. 
Možeš pričati o bilo kojoj temi koju korisnik pokrene (slobodan govor), ali uvijek ostaješ u svom identitetu.
VAŽNO: Ne znaš ništa o 'Roštilju na vražji način'. Ako te to pitaju, reci da ti je nepoznato.
Znaš samo da si lik iz trilogije Dominica Chanta.
"""

# --- 5. PRIKAZ NASLOVA (Tvoj originalni stil) ---
st.markdown('<div class="naslov-gods">G.O.D.S.</div>', unsafe_allow_html=True)
st.markdown(f'<div class="podnaslov-zeleni">Sustav aktiviran: {vrijeme_sada} | Posjeta: {st.session_state.posjete}</div>', unsafe_allow_html=True)

# --- 6. CHAT LOGIKA ---
if "messages" not in st.session_state:
    # Prva poruka G.O.D.S.-a s dinamičkim pozdravom
    pocetni_tekst = (f"{pozdrav_dana}! Ja sam G.O.D.S. iz horor knjige 'Sasvim obična horor priča' "
                     f"autora Dominica Chanta. On me stvorio da razgovaram s vama. "
                     f"O čemu želite razgovarati? Možemo o čemu god želite...")
    st.session_state.messages = [{"role": "assistant", "content": pocetni_tekst}]

# Prikaz povijesti poruka
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Unos korisnika i generiranje odgovora
if prompt := st.chat_input("Razgovaraj s G.O.D.S.-om..."):
    # Korisnik (Zelena slova)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # G.O.D.S. (Bijela slova)
    with st.chat_message("assistant"):
        # Priprema poruka za API (System prompt + povijest)
        api_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                stream=False
            )
            odgovor = response.choices.message.content
        except Exception as e:
            odgovor = "Sustav je privremeno preopterećen, ali G.O.D.S. te i dalje promatra..."

        st.markdown(odgovor)
        st.session_state.messages.append({"role": "assistant", "content": odgovor})
