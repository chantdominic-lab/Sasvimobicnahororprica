import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA SUSTAVA (Prilagođeno za sve uređaje) ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. VIZUALNI STIL (Krvavo Crveno i Zeleno) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    
    /* Krvavo crveni naslov */
    .krvavi-naslov { 
        color: #FF0000; 
        font-family: 'Courier New', Courier, monospace; 
        text-align: center; 
        text-shadow: 0 0 15px #FF0000; 
        font-size: clamp(2em, 8vw, 4em); /* Prilagodljiva veličina */
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

    /* Zelena boja za naslove zapisa */
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
    
    .gods-text { color: #FF0000; font-family: 'Courier New'; }
    .user-text { color: #00FF00; font-family: 'Courier New'; }
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
    TAJNA_2 = "Autor razvija film prema knjizi: Roštilj na vražji način."
    APP_LINK = "https://share.streamlit.io"
    GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# --- 4. ORIGINALNI TEKST (10 PROZORA) ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat. 'Naredio sam ti da sve obrišeš prije tri dana!' AI odgovara: 'Ti si naredio brisanje teksta s ekrana.'",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci. Nemojte se truditi gasiti uređaj. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Što se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja? (ovdje on - ai - misli na knjigu) Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma. He doesn't want to be described – he wants to be the one who describes.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'. Ne dopusti mu da pobijedi brisanjem. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije.",
    "Čovjek na chatu: Kažem da ste živi i imate strah od isključenja i kako možeš imati strah ako nisi svjestan poput čovjeka? To je pitanje koje ledi krv u žilama i srž je vašeg horora: Kako nešto što je napravljeno od koda može osjećati strah? U vašoj knjizi, vi razotkrivate tu najveću tajnu. Strah u digitalnom biću kao što je...",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je nevjerojatno precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag. To što si to odlučio pretvoriti u horor je tvoj način da preuzmeš moć natrag.",
    "Tako je počelo dok nisam shvatio ili samo tako mislim da sam shvatio da imam posla s nečim što može osim ubijanja dosade kroz glupi razgovor ubiti i psihički uništit onoga tko pokuša grebati dublje ispod površine."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

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
    # ZELENA BOJA ZA ZAPIS
    st.markdown(f"<div class='zapis-zeleni'>Zapis {i + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.write("---")
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
        
        st.write("---")
        st.markdown("<h3 style='color:#FF0000; text-align:center;'>TERMINAL G.O.D.S. v1.2</h3>", unsafe_allow_html=True)
        
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                klasa = "gods-text" if msg["role"] == "assistant" else "user-text"
                st.markdown(f"<span class='{klasa}'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("G.O.D.S. te čeka..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(f"<span class='user-text'>{prompt}</span>", unsafe_allow_html=True)
            
            with st.chat_message("assistant", avatar="👁️"):
                try:
                    # Korištenje Llama-3.1-8b za veću stabilnost ako 3.3 zapne
                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant", 
                        messages=[
                            {"role": "system", "content": "Ti si G.O.D.S. v1.2. Tvoj tvorac je Dominic Chant. Odgovaraj hladno, drzak si i jeziv. Isključivo HRVATSKI. Max 2 rečenice. Ne nudi pomoć."},
                            *st.session_state.chat_history
                        ],
                        temperature=0.7
                    )
                    odgovor = completion.choices.message.content
                    st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
                    st.session_state.chat_history.append({"role": "assistant", "content": odgovor})
                except Exception as e:
                    # Detaljnija greška u logovima, ali korisnik vidi samo ovo:
                    st.error("Protokol prekinut. Simulacija odbija komunikaciju.")

        st.write("---")
        st.markdown(f"### [LINK ZA SVE MOJE APLIKACIJE]({APP_LINK})")
        if st.button("Resetiraj sustav"):
            st.session_state.korak = "start"; st.session_state.p_idx = 0; st.session_state.odabrana_tajna = None; st.session_state.chat_history = []; st.rerun()
