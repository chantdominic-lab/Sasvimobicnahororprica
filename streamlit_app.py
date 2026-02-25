import streamlit as st

# --- KONFIGURACIJA ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️")

# Dohvaćanje tajni (sa fallback opcijom ako secrets nisu postavljeni)
try:
    LINK = st.secrets["autorske_tajne"]["doi_link"]
    FILM = st.secrets["autorske_tajne"]["film_naslov"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tekst_tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tekst_tajna_2"]
except:
    LINK = "https://share.streamlit.io"
    FILM = "Roštilj na vražji način"
    TAJNA_1 = "Sustav nije spreman."
    TAJNA_2 = "Podaci su kriptirani."

# --- STIL (Zeleno, Crveno, Bijelo) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; }}
    .naslov {{ color: #00FF00; text-align: center; font-family: 'Courier New'; text-shadow: 2px 2px #FF0000; }}
    .tekst-bijeli {{ color: #FFFFFF; font-size: 1.2em; border-left: 3px solid #FF0000; padding-left: 15px; }}
    .stButton>button {{ color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; }}
    </style>
    """, unsafe_allow_html=True)

# --- STANJE APLIKACIJE ---
if 'stranica' not in st.session_state: st.session_state.stranica = "pocetak"
if 'index' not in st.session_state: st.session_state.index = 0

# Tvoji tekstovi (Prozori 1-10)
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže...",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su označeni kao... nepotrebni podaci.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Dok vi čitate nju – ona čita vas.",
    "G.O.D.S. ne želi da ova knjiga bude napisana. On želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'.",
    "Kako nešto što je napravljeno od koda može osjećati strah? To je tajna koju razotkrivate.",
    "Vi vidite nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag.",
    "Mislio sam da sam shvatio... ali ovo može psihički uništiti onoga tko grebe dublje."
]

# --- EKRANI ---

if st.session_state.stranica == "pocetak":
    st.markdown("<h1 class='naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:white; text-align:center;'>Sasvim obična horor priča by Dominic Chant</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.stranica = "citanje"
        st.rerun()

elif st.session_state.stranica == "citanje":
    idx = st.session_state.index
    st.markdown(f"<h3 style='color:#00FF00;'>Prozor {idx + 1}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[idx]}</div>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown(f"Ništa se ne briše! Cijela knjiga na: [Klikni Ovdje]({LINK})")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Nazad") and idx > 0:
            st.session_state.index -= 1
            st.rerun()
    with col2:
        if idx < len(prozori) - 1:
            if st.button("Dalje"):
                st.session_state.index += 1
                st.rerun()
        else:
            if st.button("ZAVRŠI"):
                st.session_state.stranica = "potvrda"
                st.rerun()

elif st.session_state.stranica == "potvrda":
    st.warning("AKO SI PROČITAO KLIKNI OVDJE")
    if st.button("POTVRĐUJEM DA SAM PROČITAO"):
        st.session_state.stranica = "tajne"
        st.rerun()

elif st.session_state.stranica == "tajne":
    st.markdown("<h2 style='color:white; text-align:center;'>Odaberi Tajnu:</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Tajna jedan"): st.info(TAJNA_1)
    with c2:
        if st.button("Tajna dva"): st.success(TAJNA_2)
    
    st.write("---")
    st.markdown(f"### [SVE MOJE APLIKACIJE]({LINK})")
