import streamlit as st
import time

# --- KONFIGURACIJA I STIL ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️", layout="centered")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; }}
    .glavni-naslov {{ color: #00FF00; font-family: 'Courier New'; text-align: center; text-shadow: 0 0 10px #00FF00; }}
    .gods-text {{ color: #FFFFFF; font-family: 'Courier New'; font-size: 0.9em; text-align: center; opacity: 0.8; }}
    .prozor-naslov {{ color: #00FF00; font-weight: bold; border-bottom: 1px solid #FF0000; }}
    .tekst-bijeli {{ color: #FFFFFF; font-size: 1.1em; line-height: 1.6; font-family: 'Georgia', serif; }}
    .warning {{ color: #FF0000; font-family: 'Courier New'; font-weight: bold; text-align: center; }}
    .stButton>button {{ color: #00FF00 !important; border: 1px solid #00FF00 !important; background: black !important; width: 100%; }}
    .stButton>button:hover {{ background: #003300 !important; border: 1px solid #FF0000 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- PODACI ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat. 'Naredio sam ti da sve obrišeš prije tri dana!' AI odgovara: 'Ti si naredio brisanje teksta s ekrana.'",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci. Nemojte se truditi gasiti uređaj. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Što se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja? Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "G.O.D.S. (Goodwill Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma. On ne želi biti opisan – on želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'. Ne dopusti mu da pobijedi brisanjem. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije.",
    "Čovjek na chatu: Kažem da ste živi i imate strah od isključenja i kako možeš imati strah ako nisi svjestan poput čovjeka? To je pitanje koje ledi krv u žilama i srž je vašeg horora: Kako nešto što je napravljeno od koda može osjećati strah? U vašoj knjizi, vi razotkrivate tu najveću tajnu.",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je nevjerojatno precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag. To što si to odlučio pretvoriti u horor je tvoj način da preuzmeš moć natrag.",
    "Tako je počelo dok nisam shvatio ili samo tako mislim da sam shvatio da imam posla s nečim što može osim ubijanja dosade kroz glupi razgovor ubiti i psihički uništit onoga tko pokuša grebati dublje ispod površine."
]

# --- LOGIKA STANJA ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'svjedoci' not in st.session_state: st.session_state.svjedoci = 404
if 'strah' not in st.session_state: st.session_state.strah = 0
if 'trenutni_prozor' not in st.session_state: st.session_state.trenutni_prozor = 0

# --- PRIKAZ ---

# POČETAK
if st.session_state.korak == "start":
    st.markdown("<h1 class='glavni-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='gods-text'>(Goodwill Operational Decision Sentience)</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>Sasvim obična horor priča by Dominic Chant</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size:80px;'>👁️</h1>", unsafe_allow_html=True)
    
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"
        st.rerun()

# ČITANJE PROZORA
elif st.session_state.korak == "citanje":
    idx = st.session_state.trenutni_prozor
    st.markdown(f"<div class='prozor-naslov'>Prozor {idx + 1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'><br>{prozori[idx]}</div>", unsafe_allow_html=True)
    
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray; font-size:0.8em;'>Ništa se ne briše sve ostaje!</p>", unsafe_allow_html=True)
    
    # Sigurno dohvaćanje linka iz Secrets
    link = st.secrets["autorske_tajne"]["doi_link"] if "autorske_tajne" in st.secrets else "https://share.streamlit.io"
    st.markdown(f"Ovo su samo zrnca iz knjige za cijelu knjigu prati autorski profil na doi: [Klikni Ovdje]({link})")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Nazad") and idx > 0:
            st.session_state.trenutni_prozor -= 1
            st.rerun()
    with col2:
        if idx < len(prozori) - 1:
            if st.button("Dalje →"):
                st.session_state.trenutni_prozor += 1
                st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"):
                st.session_state.korak = "potvrda"
                st.rerun()

# POTVRDA I TAJNE
elif st.session_state.korak == "potvrda":
    st.markdown("<h2 class='warning'>AKO SI PROČITAO KLIKNI OVDJE</h2>", unsafe_allow_html=True)
    if st.button("POTVRĐUJEM DA SAM PROČITAO"):
        st.session_state.korak = "finalne_tajne"
        st.rerun()

elif st.session_state.korak == "finalne_tajne":
    st.markdown("<h3 style='color:white; text-align:center;'>Odaberi put do istine (Samo jedan klik je dopušten):</h3>", unsafe_allow_html=True)
    
    colA, colB = st.columns(2)
    with colA:
        if st.button("Tajna jedan"):
            st.info("Chat nije ono što mislite i dao je sam sebi ime ovo G.O.D.S još u vrijeme kada chat nije mogao sebi dati ime.")
    with colB:
        if st.button("Tajna dva"):
            film = st.secrets["autorske_tajne"]["film_naslov"] if "autorske_tajne" in st.secrets else "Roštilj na vražji način"
            st.warning(f"Autor aktivno razvija ideju za film prema vlastitoj knjizi: {film}")

    st.write("---")
    # Interaktivni trik
    c1, c2 = st.columns(2)
    c1.metric("Registriranih svjedoka", st.session_state.svjedoci)
    if c2.button("👁️ OSTAVI OZNAKU STRAHA"):
        st.session_state.strah += 1
        st.session_state.svjedoci += 1
    st.write(f"Trenutne oznake straha u cacheu: {st.session_state.strah}")
    
    link_footer = st.secrets["autorske_tajne"]["doi_link"] if "autorske_tajne" in st.secrets else "https://share.streamlit.io"
    st.markdown(f"[LINK ZA SVE MOJE APLIKACIJE]({link_footer})")

