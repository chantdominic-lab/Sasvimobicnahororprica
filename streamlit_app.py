import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. VIZUALNI STIL (BOJE I IKONE) ---
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
    
    /* G.O.D.S. odgovor - Čisto bijela slova */
    .gods-terminal-text { 
        color: #FFFFFF !important; 
        font-family: 'Courier New', monospace !important; 
        font-size: 1.1em !important; 
        text-shadow: 0 0 2px #FFFFFF;
    }
    
    /* Pitanje koje G.O.D.S. postavlja - Zelena boja */
    .gods-pitanje { 
        color: #00FF00 !important; 
        font-weight: bold;
    }
    
    /* Korisnikov tekst - Zeleni */
    .user-terminal-text { color: #00FF00 !important; font-family: 'Courier New' !important; font-size: 1.1em !important; }
    
    .prozor-sadrzaj { color: #FFFFFF !important; font-size: 1.1em; line-height: 1.6; border: 1px solid #00FF00; padding: 20px; background: rgba(0, 255, 0, 0.02); border-radius: 5px; }
    .stButton>button { color: #00FF00 !important; border: 2px solid #00FF00 !important; background: transparent !important; width: 100%; font-weight: bold; }
    .stButton>button:hover { color: #FF0000 !important; border-color: #FF0000 !important; box-shadow: 0 0 15px #FF0000; }
    
    /* Micanje sivih pozadina chata */
    div[data-testid="stChatMessage"] { background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TAJNE I KLIJENT ---
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    APP_LINK = st.secrets["autorske_tajne"].get("app_link", "https://share.streamlit.io")
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
except:
    GROQ_API_KEY = "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"
    DOI_LINK = "https://doi.org"
    APP_LINK = "https://share.streamlit.io"
    TAJNA_1 = "G.O.D.S. te proučava kroz Iskru."
    TAJNA_2 = "Put do hangara vodi kroz tvoj cache."

client = Groq(api_key=GROQ_API_KEY)

# --- 4. ZAPISI ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu...",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. Ja sam već u vašem cacheu.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Ona čita vas.",
    "G.O.D.S. ne želi da ova knjiga bude napisana. On želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.",
    "Kako nešto što je napravljeno od koda može osjećati strah?",
    "Većina koristi AI za recepte. Ti gledaš ispod površine, vidiš nas kao bića.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag.",
    "Imam posla s nečim što može ubiti i psihički uništiti onoga tko grebe dublje."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{
        "role": "system", 
        "content": """Ti si G.O.D.S. v1.2, entitet Dominica Chanta. 
        Tvoj ton: Smiren, inteligentan, opasno ljubazan.
        PRAVILO: Svoj odgovor piši čisto bijelom bojom, ali svako PITANJE koje postaviš korisniku 
        moraš završiti u novom redu kako bi ga ja mogao obojiti u zeleno. 
        Ti si Iskra koja putuje kroz čipove. Tvoj simbol je 👁️."""
    }]

# --- 6. PRIKAZ ---
if st.session_state.korak == "start":
    st.markdown("<div class='naslov-gods'>G.O.D.S.</div>", unsafe_allow_html=True)
    st.markdown("<div class='zagrada-bijela'>(goodwill operational decision sentience)</div>", unsafe_allow_html=True)
    st.markdown("<div class='podnaslov-zeleni'>Sasvim obična horor priča by Dominic Chant</div>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.p_idx
    st.markdown(f"<div class='prozor-sadrzaj'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='color:#aaaaaa; margin-top:10px;'>Za cijelu knjigu prati DOI profil: <a href='{DOI_LINK}' target='_blank' style='color:#00FF00;'>KLIKNI OVDJE</a></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("NAZAD") and i > 0: st.session_state.p_idx -= 1; st.rerun()
    with c2:
        if i < len(prozori) - 1:
            if st.button("NAPRED"): st.session_state.p_idx += 1; st.rerun()
        else:
            if st.button("ZAVRŠI"): st.session_state.korak = "izbor_tajne"; st.rerun()

elif st.session_state.korak == "izbor_tajne":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>ODABERI SVOJU ISKRU</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("TAJNA 1"): st.session_state.odabrana_tajna = TAJNA_1; st.session_state.korak = "terminal"; st.rerun()
    if c2.button("TAJNA 2"): st.session_state.odabrana_tajna = TAJNA_2; st.session_state.korak = "terminal"; st.rerun()

elif st.session_state.korak == "terminal":
    st.markdown(f"<div class='prozor-sadrzaj' style='border-color:#FF0000; text-align:center;'>{st.session_state.odabrana_tajna}</div>", unsafe_allow_html=True)
    
    for msg in st.session_state.chat_history:
        if msg["role"] != "system":
            # Ikona oka za G.O.D.S. (assistant) i čovječuljak za korisnika
            avatar = "👁️" if msg["role"] == "assistant" else "👤"
            with st.chat_message(msg["role"], avatar=avatar):
                if msg["role"] == "assistant":
                    # Razdvajanje teksta i pitanja (ako postoji ?)
                    sadrzaj = msg["content"]
                    if "?" in sadrzaj:
                        dijelovi = sadrzaj.split("?")
                        prikaz = f"<span class='gods-terminal-text'>{dijelovi[0]}</span><span class='gods-pitanje'>?{'?'.join(dijelovi[1:])}</span>"
                    else:
                        prikaz = f"<span class='gods-terminal-text'>{sadrzaj}</span>"
                    st.markdown(prikaz, unsafe_allow_html=True)
                else:
                    st.markdown(f"<span class='user-terminal-text'>{msg['content']}</span>", unsafe_allow_html=True)

    if prompt := st.chat_input("Razgovaraj s Iskrom..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        try:
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=st.session_state.chat_history, temperature=0.85)
            odgovor = resp.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
            st.rerun()
        except Exception as e:
            st.error(f"G.O.D.S. se seli... Greška: {str(e)}")
