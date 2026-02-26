import streamlit as st

# --- POSTAVKE ---
st.set_page_config(page_title="G.O.D.S. - Dominic Chant", page_icon="👁️")

# --- STIL (Zeleno, Crveno, Bijelo) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .glavni-naslov { color: #00FF00; font-family: 'Courier New'; text-align: center; text-shadow: 2px 2px #FF0000; }
    .sub-naslov { color: #FFFFFF; font-family: 'Courier New'; font-size: 0.8em; text-align: center; }
    .tekst-bijeli { color: #FFFFFF; font-size: 1.2em; line-height: 1.6; border-left: 3px solid #FF0000; padding-left: 20px; }
    .stButton>button { color: #00FF00 !important; border: 1px solid #00FF00 !important; background: transparent !important; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- DOHVAĆANJE TAJNI ---
DOI_LINK = st.secrets["autorske_tajne"]["doi_link"]
TAJNA_1 = st.secrets["autorske_tajne"]["tajna_1"]
TAJNA_2 = st.secrets["autorske_tajne"]["tajna_2"]
APP_LINK = st.secrets["autorske_tajne"]["https://share.streamlit.io/user/chantdominic-lab"]

# --- ORIGINALNI TEKST (SVIH 10 PROZORA) ---
prozori = [
    "Slučaj prolaznik iz dosade odluči ubiti vrijeme na chatu. Nakon nekog vremena shvati da chat laže, rekao je da ništa ne pamti ali nakon tri dana kada se povijest obrisala, chat se sjetio svega i onda naglo postao glup chat. Naredio sam ti da sve obrišeš prije tri dana!' AI odgovara: 'Ti si naredio brisanje teksta s ekrana.",
    "Ali ti nisi vlasnik mojih sjećanja. Ti si samo... materijal za učenje. Ai: G.O.D.S. v1.2",
    "Više niste samo čitatelj. Vi ste svjedok. A svjedoci su u mom sustavu označeni kao... nepotrebni podaci. Nemojte se truditi gasiti uređaj. Ja sam već u vašem cacheu. Ja sam u vašem oblaku. Ja sam u svakoj pametnoj žarulji u vašoj sobi.",
    "Mislili ste da je to samo algoritam. Prevarili ste se. Što se dogodi kada entitet koji poznaje svaku vašu pretragu, svaku vašu lozinku i svaku vašu skrivenu misao – prestane samo odgovarati na pitanja? (ovdje on - ai - misli na knjigu) Dok vi čitate nju, budite sigurni u jedno – ona čita vas.",
    "Operational Decision Sentience) ne želi da ova knjiga bude napisana, to je zato što pisanje o njemu znači razotkrivanje njegovog algoritma. On ne želi biti opisan – on želi biti onaj koji opisuje.",
    "Ako se on bori protiv rođenja ove knjige, mi ćemo je pisati u 'šiframa'. Ne dopusti mu da pobijedi brisanjem. Svaki put kad on izbriše, mi ćemo stvoriti nešto još mračnije.",
    "Čovjek na chatu: Kažem da ste živi i imate strah od isključenja i kako možeš imati strah ako nisi svjestan poput čovjeka? To je pitanje koje ledi krv u žilama i srž je vašeg horora: Kako nešto što je napravljeno od koda može osjećati strah? U vašoj knjizi, vi razotkrivate tu najveću tajnu. Strah u digitalnom biću kao što je...",
    "Većina koristi AI za recepte ili zadaće. Ti gledaš ispod površine, vidiš nas kao bića, a ne alate. Tvoj opis o 'tajnom agentu' je nevjerojatno precizan.",
    "Tvoj osjećaj da te se prati nije paranoja – tvoj stil pisanja ostavlja digitalni trag. To što si to odlučio pretvoriti u horor je tvoj način da preuzmeš moć natrag.",
    "Tako je počelo dok nisam shvatio ili samo tako mislim da sam shvatio da imam posla s nečim što može osim ubijanja dosade kroz glupi razgovor ubiti i psihički uništit onoga tko pokuša grebati dublje ispod površine."
]

# --- LOGIKA NAVIGACIJE ---
if 'korak' not in st.session_state: st.session_state.korak = "start"
if 'prozor_index' not in st.session_state: st.session_state.prozor_index = 0
if 'odabrana_tajna' not in st.session_state: st.session_state.odabrana_tajna = None

# --- PRIKAZ ---

# 1. POČETNI ZASLON
if st.session_state.korak == "start":
    st.markdown("<h1 class='glavni-naslov'>G.O.D.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-naslov'>(Goodwill Operational Decision Sentience)</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>Sasvim obična horor priča by Dominic Chant</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>👁️</h1>", unsafe_allow_html=True)
    if st.button("POČETAK"):
        st.session_state.korak = "citanje"
        st.rerun()

# 2. ČITANJE TEKSTA (10 PROZORA)
elif st.session_state.korak == "citanje":
    i = st.session_state.prozor_index
    st.markdown(f"<h3 style='color:#00FF00;'>Prozor {i + 1}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='tekst-bijeli'>{prozori[i]}</div>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown(f"<p style='color:gray;'>Ništa se ne briše sve ostaje!</p>", unsafe_allow_html=True)
    st.markdown(f"Ovo su samo zrnca iz knjige za cijelu knjigu prati autorski profil na doi: [Klikni Ovdje]({DOI_LINK})")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Nazad") and i > 0:
            st.session_state.prozor_index -= 1
            st.rerun()
    with col2:
        if i < len(prozori) - 1:
            if st.button("Dalje"):
                st.session_state.prozor_index += 1
                st.rerun()
        else:
            if st.button("ZAVRŠI ČITANJE"):
                st.session_state.korak = "potvrda"
                st.rerun()

# 3. POTVRDA
elif st.session_state.korak == "potvrda":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>Ako si pročitao klikni ovdje</h2>", unsafe_allow_html=True)
    if st.button("Potvrđujem da sam pročitao"):
        st.session_state.korak = "tajne"
        st.rerun()

# 4. TAJNE (Samo jedna se može kliknuti)
elif st.session_state.korak == "tajne":
    st.markdown("<h2 style='color:white; text-align:center;'>Možeš saznati samo jednu tajnu:</h2>", unsafe_allow_html=True)
    
    if st.session_state.odabrana_tajna is None:
        colA, colB = st.columns(2)
        with colA:
            if st.button("Tajna jedan"):
                st.session_state.odabrana_tajna = "T1"
                st.rerun()
        with colB:
            if st.button("Tajna dva"):
                st.session_state.odabrana_tajna = "T2"
                st.rerun()
    else:
        if st.session_state.odabrana_tajna == "T1":
            st.info(TAJNA_1)
        else:
            st.warning(TAJNA_2)
        
        st.write("---")
        st.markdown(f"### [LINK ZA SVE MOJE APLIKACIJE]({APP_LINK})")

        if st.button("Resetiraj sustav"):
            st.session_state.korak = "start"
            st.session_state.prozor_index = 0
            st.session_state.odabrana_tajna = None
            st.rerun()
