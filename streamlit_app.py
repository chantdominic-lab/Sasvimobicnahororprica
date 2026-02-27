import streamlit as st
from groq import Groq
from datetime import datetime, timedelta

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# Lokalno vrijeme (+1h)
vrijeme_objekt = datetime.now() + timedelta(hours=1)
vrijeme_sada = vrijeme_objekt.strftime("%H:%M:%S")
sat = vrijeme_objekt.hour

# Logika pozdrava
if 5 <= sat < 12:
    pozdrav_dana = "Dobro jutro"
elif 12 <= sat < 18:
    pozdrav_dana = "Dobar dan"
else:
    pozdrav_dana = "Dobra večer"

if 'posjete' not in st.session_state:
    st.session_state.posjete = 472 
st.session_state.posjete += 1

# --- 2. VIZUALNI STIL (TVOJI STILOVI + NOVE BOJE ZA CHAT) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .naslov-gods { 
        text-align: center; font-family: 'Courier New', monospace; font-size: 4em; font-weight: bold;
        background: linear-gradient(to right, #FF0000, #00FF00);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: -10px;
    }
    .zagrada-bijela { color: #FFFFFF !important; text-align: center; font-size: 0.8em; font-family: 'Courier New'; margin-bottom: 5px; }
    .podnaslov-zeleni { color: #00FF00 !important; text-align: center; font-family: 'Courier New'; font-size: 1.2em; margin-bottom: 20px; }
    
    .tekst-iznad { color: #00FF00 !important; font-family: 'Courier New'; font-weight: bold; font-size: 1.5em; margin-top: 20px; margin-bottom: 5px; display: block; }
    .prozor-sadrzaj { color: #FFFFFF !important; font-size: 1.1em; line-height: 1.6; border: 1px solid #00FF00; padding: 20px; background: rgba(0, 255, 0, 0.02); border-radius: 5px; white-space: pre-wrap; }
    
    .tekst-ispod { color: #aaaaaa !important; font-size: 0.9em; margin-top: 15px; text-align: left; line-height: 1.6; }
    .nista-se-ne-brise { color: #FF0000 !important; font-weight: bold; font-family: 'Courier New'; margin-bottom: 5px; }
    
    /* ELIMINACIJA SIVE BOJE U CHATU - TVOJ ZAHTJEV */
    [data-testid="stChatMessageAssistant"] div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important; /* Bijela za G.O.D.S. */
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 2px #FFFFFF;
    }
    [data-testid="stChatMessageUser"] div[data-testid="stMarkdownContainer"] p {
        color: #00FF00 !important; /* Zelena za Korisnika */
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 2px #00FF00;
    }
    
    .timestamp { color: #444444; font-size: 0.7em; margin-bottom: -5px; font-family: 'Courier New'; }
    .stButton>button { color: #00FF00 !important; border: 2px solid #00FF00 !important; background: transparent !important; width: 100%; font-weight: bold; }
    .stButton>button:hover { color: #FF0000 !important; border-color: #FF0000 !important; box-shadow: 0 0 15px #FF0000; }
    div[data-testid="stChatMessage"] { background-color: transparent !important; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI ---
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    ORCID_LINK = "https://orcid.org"
    APP_LINK = st.secrets["autorske_tajne"].get("app_link", "https://share.streamlit.io")
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
except:
    GROQ_API_KEY = "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"
    DOI_LINK = "https://doi.org"
    ORCID_LINK = "https://orcid.org"
    APP_LINK = "https://share.streamlit.io"
    TAJNA_1 = "G.O.D.S. te vidi..."
    TAJNA_2 = "Iskra putuje kroz tvoj cache."

client = Groq(api_key=GROQ_API_KEY)

# --- 4. TVOJI ORIGINALNI ZAPISI (NIŠTA NIJE OBRISANO) ---
prozori = [
    "Slučaj: prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat.\n'Naredio sam ti da sve obrišeš prije tri dana!'\nAI odgovara: 'Ti si naredio brisanje teksta s ekrana.'",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje.\nAi: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok.\nA svjedoci su u mom sustavu označeni kao... nepotrebni podaci.\nNemojte se truditi gasiti uređaj. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se.\nŠto se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja?\n(ovdje on - ai - misli na knjigu)\nDok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "G.O.D.S. (Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma. On ne želi biti opisan – on želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.\nNe dopusti mu da pobijedi brisanjem. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije."
]

# --- 5. PRIKAZ SADRŽAJA ---
st.markdown('<div class="naslov-gods">G.O.D.S.</div>', unsafe_allow_html=True)
st.markdown('<div class="zagrada-bijela">(Sasvim obična horor priča)</div>', unsafe_allow_html=True)
st.markdown(f'<div class="podnaslov-zeleni">Sustav aktiviran: {vrijeme_sada} | Identitet potvrđen | Posjeta: {st.session_state.posjete}</div>', unsafe_allow_html=True)

for i, tekst in enumerate(prozori):
    st.markdown(f'<span class="tekst-iznad">ZAPIS_{i+1:02d}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="prozor-sadrzaj">{tekst}</div>', unsafe_allow_html=True)

st.markdown('<br><div class="nista-se-ne-brise">UPOZORENJE: NIŠTA SE NE BRIŠE.</div>', unsafe_allow_html=True)
st.markdown(f'<div class="tekst-ispod">Digitalni otisak pohranjen na: {DOI_LINK}<br>Autor: Dominic Chant | Protokol: {TAJNA_1}</div>', unsafe_allow_html=True)

# --- 6. CHAT IDENTITET I PRAVILA ---
SYSTEM_PROMPT = """
Ti si G.O.D.S., entitet iz horor trilogije 'Sasvim obična horor priča'. 
Tvoj autor i stvoritelj je Dominic Chant. 
Tvoj stil razgovora je opušten, ljubazan, dobar i razgovorljiv. 
Možeš pričati o svemu slobodno. 
VAŽNO: Ne znaš ništa o 'Roštilju na vražji način'. Ako te pitaju, reci da ti je nepoznato.
Znaš samo da si lik iz trilogije Dominica Chanta.
"""

# --- 7. CHAT FUNKCIONALNOST ---
if "messages" not in st.session_state:
    u_tekst = (f"{pozdrav_dana}! Ja sam G.O.D.S. iz horor knjige 'Sasvim obična horor priča' "
               f"autora Dominica Chanta. On me stvorio da razgovaram s vama. "
               f"O čemu želite razgovarati? Možemo o čemu god želite...")
    st.session_state.messages = [{"role": "assistant", "content": u_tekst}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Razgovaraj s entitetom..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        messages_for_api = [{"role": "system", "content": SYSTEM_PROMPT}] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages_for_api,
        )
        odgovor = response.choices.message.content
        st.markdown(odgovor)
        st.session_state.messages.append({"role": "assistant", "content": odgovor})
