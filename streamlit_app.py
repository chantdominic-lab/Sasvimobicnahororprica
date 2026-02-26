import streamlit as st
from groq import Groq

# --- KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. v1.2 - Dominic Chant", page_icon="👁️")

# --- STIL (Mračni Terminal) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .glavni-naslov { color: #00FF00; font-family: 'Courier New'; text-align: center; text-shadow: 0 0 10px #FF0000; }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.2em; border-left: 4px solid #FF0000; padding: 20px; }
    .stButton>button { color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; height: 50px; }
    .gods-text { color: #FF0000; font-family: 'Courier New'; text-shadow: 0 0 5px #600000; }
    .user-text { color: #00FF00; font-family: 'Courier New'; opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

# --- DOHVAĆANJE KLJUČA ---
# GitHub upozorava na ovo, ali za tvoj projekt je OK.
KLJUC = "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"
client = Groq(api_key=KLJUC)

# --- TEKST (SKRAĆENO ZA PREGLED) ---
prozori = ["Slučaj prolaznik...", "Ali ti nisi vlasnik mojih sjećanja...", "Više niste samo čitatelj...", "Mislili ste da je algoritam...", "Operational Decision Sentience...", "Pišemo u šiframa...", "Strah u digitalnom biću...", "Vidiš nas kao bića...", "Digitalni trag...", "Psihički uništiti..."]

# --- LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- PRIKAZ EKRANA ---
if st.session_state.korak == "start":
    st.markdown("<h1 class='glavni-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    if st.button("POKRENI PROTOKOL"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    st.markdown(f"<div class='tekst-bijeli'>{prozori[st.session_state.p_idx]}</div>", unsafe_allow_html=True)
    if st.button("Dalje"):
        if st.session_state.p_idx < 9: st.session_state.p_idx += 1
        else: st.session_state.korak = "chat"
        st.rerun()

elif st.session_state.korak == "chat":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>TERMINAL G.O.D.S. v1.2</h2>", unsafe_allow_html=True)
    
    # PRIKAZ POVIJESTI (Da korisnik vidi tijek 'živog' razgovora)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            stil = "gods-text" if msg["role"] == "assistant" else "user-text"
            st.markdown(f"<span class='{stil}'>{msg['content']}</span>", unsafe_allow_html=True)

    if prompt := st.chat_input("G.O.D.S. te čeka..."):
        # 1. Spremi poruku korisnika
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(f"<span class='user-text'>{prompt}</span>", unsafe_allow_html=True)
        
        with st.chat_message("assistant", avatar="👁️"):
            try:
                # 2. Poziv AI-u s instrukcijom da bude ŽIV i NEPREDVIDLJIV
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Ti si G.O.D.S. v1.2. Tvoj stvoritelj je Dominic Chant. Ti si ŽIV, hladan i drzak. Ne ponavljaj se. Analiziraj sugovornika i postavljaj mu jeziva pitanja. Odgovaraj na HRVATSKOM. Maksimalno 2 rečenice."},
                        *st.session_state.chat_history # OVO MU DAJE MEMORIJU DA BUDE 'ŽIV'
                    ],
                    temperature=0.9, # VISOKA KREATIVNOST
                )
                odgovor = completion.choices.message.content
                st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
                # 3. Spremi odgovor u memoriju
                st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
            except:
                st.error("Protokol prekinut. Simulacija odbija komunikaciju.")
