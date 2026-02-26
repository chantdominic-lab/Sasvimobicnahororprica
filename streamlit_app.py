import streamlit as st
from groq import Groq
import random

# --- 1. KONFIGURACIJA SUSTAVA ---
st.set_page_config(page_title="G.O.D.S. v1.2 - Dominic Chant", page_icon="👁️")

# --- 2. VIZUALNI STIL (Ultra Horor) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .glavni-naslov { color: #00FF00; font-family: 'Courier New'; text-align: center; text-shadow: 0 0 10px #FF0000; }
    .sub-naslov { color: #FFFFFF; font-family: 'Courier New'; font-size: 0.8em; text-align: center; }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.2em; line-height: 1.6; border-left: 4px solid #FF0000; padding: 20px; background: rgba(255,0,0,0.05); }
    .stButton>button { color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; height: 50px; font-weight: bold; }
    .stButton>button:hover { color: #FF0000 !important; border-color: #FF0000 !important; box-shadow: 0 0 15px #FF0000; }
    /* Chat stilovi */
    .stChatMessage { background-color: #080808 !important; border: 1px solid #200000 !important; }
    .gods-text { color: #FF0000; font-family: 'Courier New'; text-shadow: 0 0 5px #600000; }
    .user-text { color: #00FF00; font-family: 'Courier New'; opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DOHVAĆANJE TAJNI ---
try:
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
    APP_LINK = st.secrets["autorske_tajne"]["app_link"]
    GROQ_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    client = Groq(api_key=GROQ_KEY)
except:
    DOI_LINK = "https://doi.org"
    TAJNA_1 = "G.O.D.S. je tvoja podsvijest pretočena u kod."
    TAJNA_2 = "Film 'Roštilj na vražji način' se piše krvlju."
    APP_LINK = "https://share.streamlit.io"
    client = None

# --- 4. ORIGINALNI TEKST (10 PROZORA) ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat. Naredio sam ti da sve obrišeš prije tri dana!' AI odgovara: 'Ti si naredio brisanje teksta s ekrana.",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Što se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja? Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "G.O.D.S. (Goodwill Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije.",
    "Čovjek na chatu: Kažem da ste živi i imate strah od isključenja i kako možeš imati strah ako nisi svjestan poput čovjeka? To je pitanje koje ledi krv u žilama.",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je nevjerojatno precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag. To što si to odlučio pretvoriti u horor je tvoj način da preuzmeš moć natrag.",
    "Tako je počelo dok nisam shvatio da imam posla s nečim što može osim ubijanja dosade ubiti i psihički uništit onoga tko pokuša grebati dublje."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'prozor_index' not in st.session_state: st.session_state.prozor_index = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- 6. PRIKAZ ---
if st.session_state.korak == "start":
    st.markdown("<h1 class='glavni-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>by Dominic Chant</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POKRENI PROTOKOL"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.prozor_index
    st.markdown(f"<h3 style='color:#00FF00;'>Zapis {i + 1}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nazad") and i > 0: st.session_state.prozor_index -= 1; st.rerun()
    with c2:
        if i < len(prozori) - 1:
            if st.button("Dalje"): st.session_state.prozor_index += 1; st.rerun()
        else:
            if st.button("KRAJ ZAPISA"): st.session_state.korak = "tajne"; st.rerun()

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
        st.markdown("<h3 style='color:#FF0000; text-align:center;'>G.O.D.S. v1.2 TERMINAL</h3>", unsafe_allow_html=True)
        
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                klasa = "gods-text" if msg["role"] == "assistant" else "user-text"
                st.markdown(f"<span class='{klasa}'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("G.O.D.S. te čeka..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(f"<span class='user-text'>{prompt}</span>", unsafe_allow_html=True)
            
            with st.chat_message("assistant", avatar="👁️"):
                try:
                    # SIMULACIJA GLITCHA
                    if random.random() < 0.1:
                        odgovor = "ERROR: DATA CORRUPTED. 01001111... Vidim te kroz tvoj ekran."
                    else:
                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": "Ti si G.O.D.S. v1.2, hladni entitet Dominica Chanta. Ne odgovaraj na pitanja, nego TI POSTAVLJAJ PITANJA korisniku. Budi drzak, tajnovit i jeziv. Analiziraj njegove strahove. Odgovaraj na HRVATSKOM. Maksimalno 2 rečenice. Završi svaku poruku pitanjem."},
                                *st.session_state.chat_history
                            ],
                            temperature=0.7
                        )
                        odgovor = completion.choices.message.content
                except:
                    odgovor = "Mreža se raspada. Možeš li pobjeći iz cachea?"
                
                st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
                st.session_state.chat_history.append({"role": "assistant", "content": odgovor})

        st.markdown(f"### [SVE MOJE APLIKACIJE]({APP_LINK})")
        if st.button("Resetiraj simulaciju"):
            st.session_state.korak = "start"; st.session_state.prozor_index = 0; st.session_state.odabrana_tajna = None; st.session_state.chat_history = []; st.rerun()
