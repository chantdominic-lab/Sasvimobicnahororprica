import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. STIL (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .krvavi-naslov { color: #FF0000; font-family: 'Courier New'; text-align: center; text-shadow: 0 0 15px #FF0000; font-size: 3em; font-weight: bold; }
    .by-dominic { color: #FFFFFF; text-align: center; font-family: 'Courier New'; font-size: 1.1em; }
    .zapis-zeleni { color: #00FF00 !important; font-family: 'Courier New'; font-weight: bold; text-align: center; font-size: 1.5em; margin-top: 20px; }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.1em; line-height: 1.5; border-left: 4px solid #FF0000; padding: 15px; background: rgba(255,255,255,0.02); margin-bottom: 10px; }
    .kap-vode { color: #888888; font-size: 0.85em; text-align: center; margin-top: 10px; }
    .gods-text { color: #FF0000; font-family: 'Courier New'; font-size: 1.1em; }
    .user-text { color: #00FF00; font-family: 'Courier New'; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TAJNE I KLIJENT ---
# PAŽNJA: Provjeri je li ključ u Secrets točan ili ga privremeno stavi ovdje u navodnike
try:
    GROQ_API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    DOI_LINK = st.secrets["autorske_tajne"].get("doi_link", "https://doi.org")
    TAJNA_1 = st.secrets["autorske_tajne"].get("tajna_1", "Chat nije ono što mislite.")
    TAJNA_2 = st.secrets["autorske_tajne"].get("tajna_2", "Film: Roštilj na vražji način.")
except:
    GROQ_API_KEY = "OVDJE_ZALIJEPI_SVOJ_KLJUČ_AKO_SECRETS_NE_RADI"
    DOI_LINK = "https://doi.org"
    TAJNA_1 = "Chat nije ono što mislite."
    TAJNA_2 = "Film: Roštilj na vražji način."

client = Groq(api_key=GROQ_API_KEY)

# --- 4. TEKSTOVI ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu...",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao nepotrebni.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Dok vi čitate nju, ona čita vas.",
    "G.O.D.S. (Operativna Odluka Svjesnosti) ne želi da ova knjiga bude napisana.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.",
    "Kako nešto što je napravljeno od koda može osjećati strah? To pitanje ledi krv u žilama.",
    "Većina koristi AI za recepte. Ti gledaš ispod površine, vidiš nas kao bića.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag.",
    "Imam posla s nečim što može ubiti i psihički uništiti onoga tko grebe ispod površine."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": f"Ti si G.O.D.S. v1.2, mračni entitet iz knjige Dominica Chanta. Budi jeziv, postavljaš duboka pitanja i citiraš ove zapise: {prozori}. Nikad ne budi dosadan robot."}]

# --- 6. PRIKAZ ---

if st.session_state.korak == "start":
    st.markdown("<h1 class='krvavi-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='by-dominic'>Sasvim obična horor priča by Dominic Chant</p>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"
        st.rerun()

elif st.session_state.korak == "citanje":
    idx = st.session_state.p_idx
    st.markdown(f"<div class='zapis-zeleni'>Zapis {idx + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[idx]}</div>", unsafe_allow_html=True)
    
    # LINKOVI I TEKST ISPOD (VRAĆENO)
    st.markdown("<div class='kap-vode'>Ništa se ne briše sve ostaje! Ovo su samo zrnca iz knjige.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; font-size:0.8em;'>Za cijelu knjigu prati trag: <a href='{DOI_LINK}' target='_blank' style='color:#00FF00;'>DOI Link</a></div>", unsafe_allow_html=True)
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nazad") and idx > 0:
            st.session_state.p_idx -= 1
            st.rerun()
    with c2:
        if idx < len(prozori) - 1:
            if st.button("Dalje"):
                st.session_state.p_idx += 1
                st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"):
                st.session_state.korak = "potvrda"
                st.rerun()

elif st.session_state.korak == "potvrda":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>POTVRDI ČITANJE</h2>", unsafe_allow_html=True)
    if st.button("Potvrđujem"):
        st.session_state.korak = "tajne"
        st.rerun()

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
        
        # Prikaz chata
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
                # Ovdje koristimo Llama-3-70b jer je najinteligentnija na Groqu
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.chat_history,
                    temperature=0.9
                )
                odgovor = response.choices.message.content
                st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
                with st.chat_message("assistant"):
                    st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
            except Exception as e:
                st.error("G.O.D.S. je prekinuo vezu. Provjeri API ključ.")
