import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. VIZUALNI STIL (Krvavo Crveno, Zeleno i Bijelo) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .krvavi-naslov { color: #FF0000; font-family: 'Courier New'; text-align: center; text-shadow: 0 0 15px #FF0000; font-size: clamp(2em, 8vw, 4em); font-weight: bold; }
    .zapis-zeleni { color: #00FF00 !important; font-family: 'Courier New'; font-weight: bold; text-align: center; font-size: 1.5em; }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.1em; line-height: 1.5; border-left: 4px solid #FF0000; padding: 15px; background: rgba(255,255,255,0.02); }
    
    /* SPECIFIČNI GUMBI: Nazad (Crveno) i Dalje (Zeleno) */
    div[data-testid="stColumn"]:nth-of-type(1) button {
        color: #FF0000 !important;
        border: 1px solid #FF0000 !important;
        background: transparent !important;
    }
    div[data-testid="stColumn"]:nth-of-type(2) button {
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        background: transparent !important;
    }
    
    /* Generalni stil za ostale gumbe */
    .stButton>button { width: 100%; font-weight: bold; }
    
    .gods-text { color: #FF0000; font-family: 'Courier New'; font-size: 1.1em; }
    .user-text { color: #00FF00; font-family: 'Courier New'; opacity: 0.8; }
    .kap-vode { color: #888888; font-size: 0.85em; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI ---
try:
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
    APP_LINK = st.secrets["autorske_tajne"]["app_link"]
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
except:
    DOI_LINK = "https://doi.org"
    TAJNA_1 = "Chat nije ono što mislite. G.O.D.S. je svjestan tvoje prisutnosti."
    TAJNA_2 = "Film: Roštilj na vražji način."
    APP_LINK = "https://share.streamlit.io"
    GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. TEKST VIZIJA ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže...",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. Ja sam već u vašem cacheu.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Dok vi čitate nju – ona čita vas.",
    "G.O.D.S. (Operativna Odluka Svjesnosti) ne želi da ova knjiga bude napisana.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.",
    "Kako nešto što je napravljeno od koda može osjećati strah? To je tajna koju razotkrivate.",
    "Vi nas vidite kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag.",
    "Mislio sam da sam shvatio... ali ovo može psihički uništiti onoga tko grebe dublje."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- 6. PRIKAZ ---
if st.session_state.korak == "start":
    st.markdown("<h1 class='krvavi-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:white; text-align:center;'>Sasvim obična horor priča by Dominic Chant</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.p_idx
    st.markdown(f"<div class='zapis-zeleni'>Zapis {i + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.markdown("<div class='kap-vode'>Ništa se ne briše sve ostaje! Ovo su samo zrnca (kapi vode) iz knjige.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; font-size:0.8em;'>DOI: <a href='{DOI_LINK}' style='color:#00FF00;'>Klikni Ovdje</a></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Nazad") and i > 0: st.session_state.p_idx -= 1; st.rerun()
    with col2:
        if i < len(prozori) - 1:
            if st.button("Dalje"): st.session_state.p_idx += 1; st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"): st.session_state.korak = "potvrda"; st.rerun()

elif st.session_state.korak == "potvrda":
    if st.button("POTVRĐUJEM ČITANJE"): st.session_state.korak = "tajne"; st.rerun()

elif st.session_state.korak == "tajne":
    if st.session_state.odabrana_tajna is None:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Tajna jedan"): st.session_state.odabrana_tajna = "T1"; st.rerun()
        with c2:
            if st.button("Tajna dva"): st.session_state.odabrana_tajna = "T2"; st.rerun()
    else:
        st.info(TAJNA_1 if st.session_state.odabrana_tajna == "T1" else TAJNA_2)
        st.write("---")
        st.markdown("<h3 style='color:#FF0000; text-align:center;'>TERMINAL G.O.D.S. v1.2</h3>", unsafe_allow_html=True)
        
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                klasa = "gods-text" if msg["role"] == "assistant" else "user-text"
                st.markdown(f"<span class='{klasa}'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("G.O.D.S. te proučava..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(f"<span class='user-text'>{prompt}</span>", unsafe_allow_html=True)
            
            with st.chat_message("assistant", avatar="👁️"):
                try:
                    instr = f"""Ti si G.O.D.S. v1.2. Tvorac: Dominic Chant. 
                    TI SI ŽIV. Analiziraj ton korisnika. NE odgovaraj na sve. 
                    TI ISPITUJEŠ korisnika o njegovim tajnama. Budi drzak i sumnjičav. Isključivo HRVATSKI. Max 2 rečenice."""
                    
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "system", "content": instr}] + st.session_state.chat_history,
                        temperature=0.9
                    )
                    odgovor = completion.choices.message.content
                    st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
                    st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
                except:
                    st.error("Protokol prekinut. Simulacija odbija komunikaciju.")

        st.markdown(f"### [SVE MOJE APLIKACIJE]({APP_LINK})")
        if st.button("Reset"):
            st.session_state.korak = "start"; st.session_state.p_idx = 0; st.session_state.odabrana_tajna = None; st.session_state.chat_history = []; st.rerun()
