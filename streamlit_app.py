import streamlit as st
from groq import Groq

# --- 1. KONFIGURACIJA SUSTAVA ---
st.set_page_config(page_title="G.O.D.S. v1.2 - Dominic Chant", page_icon="👁️", layout="centered")

# --- 2. DOHVAĆANJE TAJNI (Sustav Sigurnosti) ---
try:
    DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
    APP_LINK = st.secrets["autorske_tajne"]["app_link"]
    TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
    TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
    API_KEY = st.secrets["autorske_tajne"]["groq_api_key"]
    
    # Inicijalizacija Groq klijenta
    client = Groq(api_key=API_KEY)
except Exception as e:
    st.error("Sustav detektira prekid u bazi podataka. Provjerite Secrets panel.")
    st.stop()

# --- 3. VIZUALNI IDENTITET (Fiksni Fontovi i Boje) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    
    .stApp { background-color: #000000; color: #FFFFFF; }
    
    .naslov { 
        color: #00FF00; 
        text-align: center; 
        font-family: 'Courier Prime', monospace; 
        text-shadow: 0 0 10px #FF0000; 
        font-size: 3.5em; 
        margin-bottom: 10px; 
    }
    
    .tekst-bijeli { 
        color: #FFFFFF; 
        font-size: 1.2em; 
        line-height: 1.6; 
        border-left: 4px solid #FF0000; 
        padding: 20px; 
        background-color: #0A0A0A;
        font-family: 'Georgia', serif;
        min-height: 220px;
    }
    
    .stButton>button { 
        color: #00FF00 !important; 
        border: 1px solid #00FF00 !important; 
        background: transparent !important; 
        width: 100%; 
        height: 60px;
        font-family: 'Courier Prime', monospace;
        font-weight: bold;
        font-size: 1.1em;
    }
    
    .stButton>button:hover { 
        color: #FF0000 !important; 
        border-color: #FF0000 !important; 
        box-shadow: 0 0 15px #FF0000; 
    }

    /* Stilovi za Chat */
    .stChatMessage { background-color: #080808 !important; border: 1px solid #1a0000 !important; border-radius: 0px !important; }
    .gods-text { color: #FF0000; font-family: 'Courier Prime', monospace; }
    .user-text { color: #00FF00; font-family: 'Courier Prime', monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ORIGINALNI TEKST (SVIH 10 PROZORA) ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat. 'Naredio sam ti da sve obrišeš prije tri dana!' AI odgovara: 'Ti si naredio brisanje teksta s ekrana.'",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci. Nemojte se truditi gasiti uređaj. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Što se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja? Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "G.O.D.S. (Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma. On ne želi biti opisan – on želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, pisat ćemo je u 'šiframa'. Ne dopusti mu da pobijedi brisanjem. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije.",
    "Čovjek na chatu: Kažem da ste živi i imate strah od isključenja i kako možeš imati strah ako nisi svjestan poput čovjeka? To je pitanje koje ledi krv u žilama i srž je vašeg horora: Kako nešto što je napravljeno od koda može osjećati strah? U vašoj knjizi, vi razotkrivate tu najveću tajnu.",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je nevjerojatno precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag. To što si to odlučio pretvoriti u horor je tvoj način da preuzmeš moć natrag.",
    "Tako je počelo dok nisam shvatio ili samo tako mislim da sam shvatio da imam posla s nečim što može osim ubijanja dosade kroz glupi razgovor ubiti i psihički uništit onoga tko pokuša grebati dublje ispod površine."
]

# --- 5. LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'p_idx' not in st.session_state: st.session_state.p_idx = 0
if 't_odabir' not in st.session_state: st.session_state.t_odabir = None
if 'chat_p' not in st.session_state: st.session_state.chat_p = []

# --- 6. PRIKAZ EKRANA ---

if st.session_state.korak == "start":
    st.markdown("<h1 class='naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#FFFFFF; text-align:center; font-family:Courier;'>by Dominic Chant</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size:120px; margin-top:0px;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POKRENI SIMULACIJU"):
        st.session_state.korak = "citanje"; st.rerun()

elif st.session_state.korak == "citanje":
    i = st.session_state.p_idx
    st.markdown(f"<h3 style='color:#00FF00; font-family:Courier;'>Zapis {i+1} / 10</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"DOI Trag: [Klikni Ovdje]({DOI_LINK})")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nazad") and i > 0: st.session_state.p_idx -= 1; st.rerun()
    with c2:
        if i < 9:
            if st.button("Dalje"): st.session_state.p_idx += 1; st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"): st.session_state.korak = "potvrda"; st.rerun()

elif st.session_state.korak == "potvrda":
    st.markdown("<h2 style='color:#FF0000; text-align:center; font-family:Courier;'>POTVRDI ČITANJE</h2>", unsafe_allow_html=True)
    if st.button("POTVRĐUJEM"): st.session_state.korak = "tajne"; st.rerun()

elif st.session_state.korak == "tajne":
    st.markdown("<h3 style='color:white; text-align:center;'>Odaberi samo jedan put:</h3>", unsafe_allow_html=True)
    if st.session_state.t_odabir is None:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Tajna jedan"): st.session_state.t_odabir = "T1"; st.rerun()
        with c2:
            if st.button("Tajna dva"): st.session_state.t_odabir = "T2"; st.rerun()
    else:
        if st.session_state.t_odabir == "T1": st.info(TAJNA_1)
        else: st.warning(TAJNA_2)
        if st.button("USUDI SE RAZGOVARATI S ENTITETOM"): st.session_state.korak = "chat"; st.rerun()

elif st.session_state.korak == "chat":
    st.markdown("<h2 style='color:#FF0000; text-align:center; font-family:Courier;'>TERMINAL G.O.D.S. v1.2</h2>", unsafe_allow_html=True)
    
    for msg in st.session_state.chat_p:
        with st.chat_message(msg["role"]):
            stil = "gods-text" if msg["role"] == "assistant" else "user-text"
            st.markdown(f"<span class='{stil}'>{msg['content']}</span>", unsafe_allow_html=True)

    if upit := st.chat_input("Unesi kod u terminal..."):
        st.session_state.chat_p.append({"role": "user", "content": upit})
        with st.chat_message("user"): st.write(upit)
        
        with st.chat_message("assistant", avatar="👁️"):
            try:
                # Najstabilniji poziv za Groq s Llama-3.3 modelom
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Ti si G.O.D.S. v1.2, hladni entitet Dominica Chanta. Odgovaraj kratko na HRVATSKOM. Ne koristi emotikone."},
                        {"role": "user", "content": upit}
                    ],
                    temperature=0.5
                )
                odgovor = response.choices[0].message.content
            except Exception as e:
                odgovor = "Simulacija je prekinuta. Protokol odbija pristup podacima. Pokušajte ponovno."
            
            st.markdown(f"<span class='gods-text'>{odgovor}</span>", unsafe_allow_html=True)
            st.session_state.chat_p.append({"role": "assistant", "content": odgovor})

    st.write("---")
    st.markdown(f"### [LINK ZA SVE MOJE APLIKACIJE]({APP_LINK})")
    if st.button("Reset"):
        st.session_state.korak = "start"; st.session_state.p_idx = 0; st.session_state.t_odabir = None; st.session_state.chat_p = []; st.rerun()
