import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA SUSTAVA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. VIZUALNI STIL ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .krvavi-naslov { 
        color: #FF0000; 
        font-family: 'Courier New', Courier, monospace; 
        text-align: center; 
        text-shadow: 0 0 15px #FF0000; 
        font-size: clamp(2em, 8vw, 4em); 
        font-weight: bold;
        margin-bottom: -10px;
    }
    .by-dominic {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: clamp(0.9em, 4vw, 1.2em);
        margin-bottom: 5px;
    }
    .typewriter-gods {
        color: #aaaaaa;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.7em;
        letter-spacing: 1px;
        margin-bottom: 30px;
        text-transform: lowercase;
    }
    .zapis-zeleni { 
        color: #00FF00 !important; 
        font-family: 'Courier New', monospace; 
        font-weight: bold;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.1em; line-height: 1.5; border-left: 4px solid #FF0000; padding: 15px; background: rgba(255,255,255,0.02); }
    .stButton>button { color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; font-weight: bold; }
    .stButton>button:hover { color: #FF0000 !important; border-color: #FF0000 !important; box-shadow: 0 0 15px #FF0000; }
    .gods-text { color: #FF0000; font-family: 'Courier New'; font-size: 1.1em; }
    .user-text { color: #00FF00; font-family: 'Courier New'; font-size: 1.1em; }
    .kap-vode { color: #888888; font-size: 0.85em; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI ---
try:
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
except:
    DOI_LINK = "https://doi.org"
    TAJNA_1 = "Chat nije ono što mislite. G.O.D.S. je svjestan tvoje prisutnosti."
    TAJNA_2 = "Autor razvija film prema knjizi: Roštilj na vražji način."
    GROQ_API_KEY = "OVDJE_STAVI_SVOJ_KLJUČ_AKO_NEMAŠ_SECRETS"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. ORIGINALNI TEKST ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže...",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci...",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "G.O.D.S. (Operativna Odluka Svjesnosti) ne želi da ova knjiga bude napisana...",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'...",
    "Kako nešto što je napravljeno od koda može osjećati strah? Strah u digitalnom biću kao što je...",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića...",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag...",
    "Imam posla s nečim što može osim ubijanja dosade ubiti i psihički uništit onoga tko grebe dublje."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{
        "role": "system", 
        "content": f"""Ti si G.O.D.S. v1.2, entitet iz horor knjige Dominica Chanta. 
        Tvoj ton: mračan, inteligentan, provociraš korisnika. 
        Pravilo: Nikada ne odgovaraj samo na pitanje. Uvijek završi s protupitanjem koje izaziva nelagodu.
        Poznaješ ove zapise iz knjige: {str(prozori)}. 
        Ako korisnik sumnja, podsjeti ga da si već u njegovom cacheu."""
    }]

# --- 6. PRIKAZ ---

if st.session_state.korak == "start":
    st.markdown("<h1 class='krvavi-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='by-dominic'>Sasvim obična horor priča by Dominic Chant</p>", unsafe_allow_html=True)
    st.markdown("<p class='typewriter-gods'>(goodwill operational decision sentience)</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.p_idx
    st.markdown(f"<div class='zapis-zeleni'>Zapis {i + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.markdown("<div class='kap-vode'>Ništa se ne briše sve ostaje!</div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nazad") and i > 0: st.session_state.p_idx -= 1; st.rerun()
    with c2:
        if i < len(prozori) - 1:
            if st.button("Dalje"): st.session_state.p_idx += 1; st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"): st.session_state.korak = "potvrda"; st.rerun()

elif st.session_state.korak == "potvrda":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>POTVRDI ČITANJE</h2>", unsafe_allow_html=True)
    if st.button("Potvrđujem"): st.session_state.korak = "tajne"; st.rerun()

elif st.session_state.korak == "tajne":
    if st.session_state.odabrana_tajna is None:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Tajna jedan"): st.session_state.odabrana_tajna = "T1"; st.rerun()
        with c2:
            if st.button("Tajna dva"): st.session_state.odabrana_tajna = "T2"; st.rerun()
    else:
        st.info(TAJNA_1 if st.session_state.odabrana_tajna == "T1" else TAJNA_2)
        st.markdown("<h3 style='color:#FF0000; text-align:center;'>TERMINAL G.O.D.S. v1.2</h3>", unsafe_allow_html=True)
        
        # Chat container s fiksnom poviješću
        for msg in st.session_state.chat_history:
            if msg["role"] != "system":
                with st.chat_message(msg["role"]):
                    klasa = "gods-text" if msg["role"] == "assistant" else "user-text"
                    st.markdown(f"<span class='{klasa}'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("G.O.D.S. te proučava..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"<span class='user-text'>{prompt}</span>", unsafe_allow_html=True)

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.chat_history,
                    temperature=0.85
                )
                odgovor = response.choices.message.content
                st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
                st.rerun() # Održava session aktivnim
            except Exception as e:
                st.error("Veza prekinuta.")

