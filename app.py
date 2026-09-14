import streamlit as st
import os
import base64
from pathlib import Path
import textwrap
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Miika Koivisto | E-Portfolio",
    page_icon="💻",
    layout="wide"
)

# Load the portfolio background image from assets and convert it to a browser-safe data URI.
background_path = Path("assets/portfolio_network_bg.png")
background_data_uri = ""

if background_path.exists():
    encoded_background = base64.b64encode(background_path.read_bytes()).decode("utf-8")
    background_data_uri = f"data:image/png;base64,{encoded_background}"

# -------------------------
# THEME
# -------------------------

# Permanent dark mode
bg = "#0e1117"
card_bg = "#161b22"
text = "#f0f2f6"
muted = "#a7b0be"
border = "#30363d"
nav_bg = "#161b22"

# -------------------------
# CUSTOM CSS
# -------------------------



st.markdown(f"""
<style>



/* -------------------------
   PAGE
------------------------- */

.stApp {{
    background: {bg} !important;
    color: {text} !important;
}}

[data-testid="stAppViewContainer"] {{
    background: transparent !important;
    position: relative;
    min-height: 100vh;
    overflow-x: hidden;
}}

.network-image-bg {{
    position: fixed;
    inset: -6%;
    z-index: 0;
    pointer-events: none;
    background-color: {bg};
    background-image:
        linear-gradient(rgba(2, 7, 20, 0.34), rgba(2, 7, 20, 0.46)),
        url("{background_data_uri}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    transform: scale(1.07);
    animation: networkBackgroundFloat 22s ease-in-out infinite alternate;
    will-change: transform, background-position, filter;
}}

.network-image-bg::after {{
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 72% 35%, rgba(65, 125, 255, 0.08), transparent 28%),
        radial-gradient(circle at 84% 72%, rgba(90, 75, 230, 0.07), transparent 30%);
    animation: networkGlowPulse 10s ease-in-out infinite alternate;
}}

@keyframes networkBackgroundFloat {{
    0% {{
        transform: scale(1.07) translate3d(-1.5%, -0.8%, 0);
        background-position: 48% 50%;
        filter: brightness(0.92);
    }}
    50% {{
        transform: scale(1.10) translate3d(1.2%, 0.7%, 0);
        background-position: 52% 48%;
        filter: brightness(1.00);
    }}
    100% {{
        transform: scale(1.08) translate3d(-0.5%, 1.1%, 0);
        background-position: 50% 53%;
        filter: brightness(0.96);
    }}
}}

@keyframes networkGlowPulse {{
    0% {{
        opacity: 0.45;
        transform: scale(1);
    }}
    100% {{
        opacity: 0.85;
        transform: scale(1.05);
    }}
}}

.block-container {{
    position: relative;
    z-index: 2;
    max-width: 1180px;
    margin: 2.2rem auto 3rem auto;
    padding: 2.2rem 2.4rem 3rem 2.4rem !important;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    background: rgba(14, 17, 23, 0.88);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow:
        0 24px 70px rgba(0,0,0,0.42),
        0 1px 0 rgba(255,255,255,0.04) inset;
}}

@media (max-width: 900px) {{
    .block-container {{
        margin: 1rem;
        padding: 1.4rem 1.1rem 2rem 1.1rem !important;
        border-radius: 16px;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    .network-image-bg,
    .network-image-bg::after {{
        animation: none;
    }}
}}

/* -------------------------
   NORMAL TEXT
------------------------- */

p,
li {{
    color: {text};
}}

.hero-title {{
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 0;
    color: {text} !important;
}}

.hero-subtitle {{
    font-size: 1.5rem;
    color: {muted} !important;
    margin-top: 0.3rem;
}}

.hero-text {{
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 750px;
    color: {text} !important;
}}

.section-title {{
    font-size: 2rem;
    font-weight: 700;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: {text} !important;
}}




/* -------------------------
   INTRO / ABOUT CARD
------------------------- */

.intro-card {{
    margin-top: 0.4rem;
    padding: 2rem 2.1rem;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(22,27,34,0.96), rgba(17,23,34,0.90));
    box-shadow: 0 16px 42px rgba(0,0,0,0.24);
}}

.intro-name {{
    font-size: 3.15rem;
    line-height: 1.05;
    font-weight: 700;
    margin: 0;
    color: #f0f2f6 !important;
}}

.intro-role {{
    margin-top: 0.55rem;
    font-size: 1.25rem;
    font-weight: 500;
    color: #a7b0be !important;
}}

.intro-divider {{
    height: 1px;
    margin: 1.45rem 0 1.3rem 0;
    background: linear-gradient(90deg, rgba(85,145,255,0.65), rgba(255,255,255,0.08), transparent);
}}

.intro-about-title {{
    margin: 0 0 0.7rem 0;
    font-size: 1.35rem;
    font-weight: 700;
    color: #f0f2f6 !important;
}}

.intro-about {{
    margin: 0 0 0.9rem 0;
    font-size: 1rem;
    line-height: 1.72;
    color: #d7dce5 !important;
}}

.intro-about:last-child {{
    margin-bottom: 0;
}}

@media (max-width: 700px) {{
    .intro-card {{
        padding: 1.4rem;
    }}

    .intro-name {{
        font-size: 2.35rem;
    }}
}}

/* -------------------------
   CONTACT CTA
------------------------- */

.contact-cta {{
    margin-top: 1.2rem;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid {border} !important;
    background: {card_bg} !important;
    box-shadow: none;
}}

.contact-cta h2 {{
    margin: 0 0 0.45rem 0;
    font-size: 2rem;
    color: {text} !important;
}}

.contact-cta p {{
    margin: 0;
    color: {muted} !important;
    font-size: 1.02rem;
    line-height: 1.6;
}}

.contact-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem 1.2rem;
    margin-top: 1.1rem;
    color: {text};
    font-size: 0.95rem;
}}

.contact-copy-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    width: 100%;
    padding: 0.75rem 0.9rem;
    border: 1px solid {border};
    border-radius: 9px;
    background: {bg};
}}

.contact-copy-value {{
    color: {text} !important;
    user-select: text;
    -webkit-user-select: text;
}}

.contact-copy-btn {{
    flex-shrink: 0;
    padding: 0.38rem 0.65rem;
    border: 1px solid {border};
    border-radius: 7px;
    background: {card_bg};
    color: {text};
    cursor: pointer;
    font: inherit;
    font-size: 0.82rem;
}}

.contact-copy-btn:hover {{
    border-color: rgba(120, 180, 255, 0.7);
}}

.contact-copy-btn:active {{
    transform: translateY(1px);
}}



/* -------------------------
   SKILL CARDS
------------------------- */

.skill-card {{
    padding: 1.25rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    min-height: 285px;
    height: 100%;
    box-sizing: border-box;
    background: {card_bg} !important;
    color: {text} !important;
    display: flex;
    flex-direction: column;
}}

.skill-chip-container {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    align-content: flex-start;
}}

.skill-chip {{
    display: inline-flex;
    align-items: center;
    max-width: 100%;
    padding: 0.32rem 0.56rem;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    font-size: 0.80rem;
    line-height: 1.2;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
}}

.skill-card * {{
    color: {text} !important;
}}

.skill-card h3 {{
    color: {text} !important;
    margin-top: 0;
}}

.skill-card p {{
    color: {text} !important;
}}


/* Keep the four skill cards visually equal in height */
[data-testid="stHorizontalBlock"]:has(.skill-card) {{
    align-items: stretch;
}}

[data-testid="column"]:has(.skill-card) {{
    display: flex;
}}

[data-testid="column"]:has(.skill-card) > div {{
    width: 100%;
}}





/* -------------------------
   SHARED CONTENT CARDS
------------------------- */

.content-card {{
    padding: 1.6rem 1.8rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
    margin-bottom: 1rem;
}}

.content-card * {{
    color: {text} !important;
}}

.content-card h3 {{
    margin-top: 0;
    margin-bottom: 0.65rem;
}}

.content-card p {{
    line-height: 1.65;
}}

.content-card ul {{
    margin-bottom: 0.9rem;
}}

.content-card a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-top: 0.6rem;
    padding: 0.62rem 0.9rem;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    text-decoration: none !important;
    font-weight: 600;
    transition: transform 0.18s ease, border-color 0.18s ease;
}}

.content-card a:hover {{
    transform: translateY(-2px);
    border-color: rgba(120, 180, 255, 0.75);
}}


/* -------------------------
   FEATURED PROJECT ACTIONS
------------------------- */

.project-feature-card .project-actions {{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.65rem;
    margin-top: 0.9rem;
}}

.project-feature-card .project-assistant-row {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-wrap: wrap;
}}

.project-feature-card .project-btn {{
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    width: 220px;
    height: 42px;
    margin: 0 !important;
    padding: 0 0.9rem !important;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    text-decoration: none !important;
    font-weight: 600;
    line-height: 1;
    transition: transform 0.18s ease, border-color 0.18s ease;
}}

.project-feature-card .project-btn:hover {{
    transform: translateY(-2px);
    border-color: rgba(120, 180, 255, 0.75);
}}

.project-feature-card .project-btn-disabled {{
    color: {muted} !important;
    opacity: 0.65;
    cursor: default;
}}

.project-feature-card .project-btn-disabled:hover {{
    transform: none;
    border-color: {border};
}}

.project-feature-card .project-demo-access {{
    display: inline-flex;
    align-items: center;
    box-sizing: border-box;
    height: 42px;
    border: 1px solid {border};
    border-radius: 8px;
    background: {bg};
    overflow: hidden;
}}

.project-feature-card .project-demo-label {{
    display: inline-flex;
    align-items: center;
    height: 100%;
    padding: 0 0.75rem;
    border-right: 1px solid {border};
    color: {muted} !important;
    font-size: 0.88rem;
    font-weight: 600;
    white-space: nowrap;
}}

.project-feature-card .project-demo-code {{
    display: inline-flex;
    align-items: center;
    height: 100%;
    min-width: 88px;
    padding: 0 0.75rem;
    border: 0 !important;
    border-radius: 0 !important;
    background: transparent !important;
    color: {text} !important;
    font-size: 0.88rem;
    user-select: all;
    -webkit-user-select: all;
}}

@media (max-width: 700px) {{
    .project-feature-card .project-assistant-row {{
        align-items: flex-start;
        flex-direction: column;
    }}

    .project-feature-card .project-btn,
    .project-feature-card .project-demo-access {{
        width: 100%;
    }}

    .project-feature-card .project-demo-code {{
        flex: 1;
    }}
}}


.project-action-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
}}

.project-action-buttons {{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.15rem;
}}

.project-disabled-button {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-top: 0.6rem;
    padding: 0.62rem 0.9rem;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {muted} !important;
    font-weight: 600;
    opacity: 0.65;
}}

.demo-access-inline {{
    display: flex;
    align-items: center;
    gap: 0.55rem;
    margin-top: 0.6rem;
    flex-wrap: wrap;
}}

.demo-access-label {{
    color: {muted} !important;
    font-size: 0.9rem;
    font-weight: 600;
}}

.demo-access-inline code {{
    padding: 0.34rem 0.5rem;
    border-radius: 7px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    font-size: 0.88rem;
}}

.demo-copy-btn {{
    padding: 0.34rem 0.58rem;
    border-radius: 7px;
    border: 1px solid {border};
    background: {bg};
    color: {text};
    cursor: pointer;
    font: inherit;
    font-size: 0.82rem;
    font-weight: 600;
}}

.demo-copy-btn:hover {{
    border-color: rgba(120, 180, 255, 0.75);
}}

@media (max-width: 700px) {{
    .project-action-row {{
        align-items: flex-start;
        flex-direction: column;
    }}
}}

/* -------------------------
   PROJECT CARD
------------------------- */

.project-card {{
    padding: 1.5rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
}}

.project-card * {{
    color: {text} !important;
}}


/* -------------------------
   EXPERIENCE
------------------------- */

.experience-card {{
    padding: 1.6rem 1.8rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
    margin-bottom: 1rem;
}}

.experience-card * {{
    color: {text} !important;
}}

.experience-company {{
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    color: {text} !important;
}}

.experience-role {{
    font-size: 1.05rem;
    font-weight: 600;
    color: {muted} !important;
    margin-bottom: 1rem;
}}

.experience-category {{
    font-weight: 700;
    margin-top: 0.8rem;
    color: {text} !important;
}}



/* -------------------------
   METRICS
------------------------- */

[data-testid="stMetric"] {{
    border: 1px solid {border} !important;
    padding: 1rem;
    border-radius: 12px;
    background: {card_bg} !important;
}}

[data-testid="stMetric"] * {{
    color: {text} !important;
}}


/* -------------------------
   EXPANDER
------------------------- */

[data-testid="stExpander"] {{
    background: {card_bg} !important;
    border-color: {border} !important;
}}

[data-testid="stExpander"] * {{
    color: {text} !important;
}}


/* -------------------------
   BUTTONS
------------------------- */

.stLinkButton a,
.stDownloadButton button {{
    border-radius: 8px;
    font-weight: 600;
}}


/* -------------------------
   HIDE STREAMLIT UI
------------------------- */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="network-image-bg" aria-hidden="true"></div>
""", unsafe_allow_html=True)







# -------------------------
# DEPLOYMENT SETTINGS
# -------------------------

def get_portfolio_setting(name, default=""):
    try:
        if name in st.secrets:
            return str(st.secrets[name]).strip()
    except Exception:
        pass
    return os.getenv(name, default).strip()


WORK_APPLICATION_URL = get_portfolio_setting("WORK_APPLICATION_URL")
WORK_APPLICATION_PASSCODE = get_portfolio_setting("WORK_APPLICATION_PASSCODE")

# -------------------------
# LANGUAGE
# -------------------------

if "portfolio_language" not in st.session_state:
    st.session_state.portfolio_language = "en"

LANG = {
    "en": {
        "language": "Language",
        "role": "IT Development • Automation • AI",
        "about_title": "About Me",
        "about_1": "I’m an IT professional with a background in developing and improving digital solutions, automation and business systems. My experience has given me the opportunity to work across different areas of IT, from system development and integrations to process automation and solving practical business needs with technology.",
        "about_2": "I enjoy understanding how things work, identifying opportunities for improvement and turning ideas into practical solutions. I’m systematic and solution-oriented in my work, but I also value collaboration, continuous learning and sharing knowledge with others.",
        "about_3": "I’m especially interested in how AI can be applied to real-world problems and existing business processes. As the next step in my career, I’m looking to move toward AI engineering, building on my existing IT experience while developing deeper expertise in AI-driven applications and intelligent automation.",
        "cv_en": "CV — English",
        "cv_fi": "CV — Finnish",
        "skills": "Skills",
        "skill_ai": "AI & Cloud",
        "skill_programming": "Programming",
        "skill_automation": "Automation & APIs",
        "skill_systems": "Systems & Low-code Platforms",
        "featured_project": "Featured Project",
        "project_intro": "A recruiter-facing, multi-company Retrieval-Augmented Generation application built to provide grounded information about my experience, technical skills, projects and suitability for a specific open position.",
        "what_built": "What I built",
        "project_items": [
            "Multi-company RAG architecture with isolated application contexts",
            "Hybrid keyword + vector retrieval with Azure AI Search",
            "Vector embeddings with Azure OpenAI",
            "Metadata filtering for company-specific and global applicant data",
            "Conversation-aware query rewriting for follow-up questions",
            "Grounded LLM responses with inline citations and inspectable evidence",
            "Automated company onboarding, chunking, embedding and indexing pipeline",
            "Cross-company isolation and conversation-aware retrieval evaluation",
            "Recruiter-facing Streamlit interface with transparent RAG diagnostics",
        ],
        "view_project": "View Project on GitHub",
        "open_live_project": "Try AI Assistant",
        "demo_access": "Demo access",
        "demo_passcode": "Passcode",
        "demo_not_configured": "Live demo URL has not been configured yet.",
        "how_it_works": "How the Work Application Assistant Works",
        "steps": [
            ("1. Identify", "Recruiter enters their company to select the correct application context."),
            ("2. Rewrite", "Follow-up questions are rewritten into standalone retrieval queries when needed."),
            ("3. Retrieve", "Azure AI Search performs hybrid keyword and vector retrieval."),
            ("4. Filter", "Metadata filtering limits evidence to the active company and global applicant data."),
            ("5. Answer", "Azure OpenAI generates a grounded answer with citations to retrieved evidence."),
        ],
        "retrieval_eval": "Retrieval Evaluation",
        "company_isolation": "Company Isolation",
        "conversation_tests": "Conversation Tests",
        "see_ui": "See Application UI",
        "see_rag": "See RAG Retrieval Details",
        "rag_caption": "Evidence, citations and RAG retrieval details",
        "experience": "Experience",
        "job_role": "IT Specialist / IT Development · 04/2024 – 09/2026",
        "development_apis": "Development & APIs",
        "development_items": [
            "Developed and modernized internal store and picking applications",
            "Built, tested and troubleshot REST API integrations",
            "Tested and documented integrations between business systems",
        ],
        "automation": "Automation",
        "automation_items": [
            "Automated weekly and monthly e-commerce content publishing",
            "Automated internal forms, approval processes and information flows with Power Automate",
        ],
        "systems_data": "Systems & Data",
        "systems_items": [
            "Worked with e-commerce, PIM and ERP environments",
            "Maintained product information and certificate data quality",
        ],
        "education": "Education",
        "degree": "Bachelor of Business Administration",
        "degree_field": "Business Information Technology",
        "contact": "Contact Me",
        "copy": "Copy",
        "copied": "Copied!",
    },
    "fi": {
        "language": "Kieli",
        "role": "IT-kehitys • Automaatio • Tekoäly",
        "about_title": "Minusta",
        "about_1": "Olen IT-ammattilainen, jolla on kokemusta digitaalisten ratkaisujen, automaation ja liiketoimintajärjestelmien kehittämisestä. Olen työskennellyt monipuolisesti IT:n eri osa-alueilla järjestelmäkehityksestä ja integraatioista prosessien automatisointiin ja käytännön liiketoimintatarpeiden ratkaisemiseen teknologian avulla.",
        "about_2": "Pidän siitä, että saan ymmärtää miten asiat toimivat, tunnistaa kehityskohteita ja muuttaa ideat käytännön ratkaisuiksi. Työskentelen järjestelmällisesti ja ratkaisukeskeisesti, ja arvostan yhteistyötä, jatkuvaa oppimista sekä osaamisen jakamista muiden kanssa.",
        "about_3": "Olen erityisen kiinnostunut tekoälyn soveltamisesta käytännön ongelmiin ja olemassa oleviin liiketoimintaprosesseihin. Seuraavana askeleena urallani haluan suuntautua yhä vahvemmin AI engineering -tehtäviin ja rakentaa nykyisen IT-kokemukseni päälle syvempää osaamista tekoälypohjaisista sovelluksista ja älykkäästä automaatiosta.",
        "cv_en": "CV — Englanti",
        "cv_fi": "CV — Suomi",
        "skills": "Osaaminen",
        "skill_ai": "Tekoäly & Pilvipalvelut",
        "skill_programming": "Ohjelmointi",
        "skill_automation": "Automaatio & API:t",
        "skill_systems": "Järjestelmät & Low-code-alustat",
        "featured_project": "Esittelyprojekti",
        "project_intro": "Rekrytoijille suunnattu usean yrityksen Retrieval-Augmented Generation -sovellus, joka tarjoaa lähteisiin perustuvaa tietoa kokemuksestani, teknisestä osaamisestani, projekteistani ja soveltuvuudestani tiettyyn avoimeen tehtävään.",
        "what_built": "Mitä rakensin",
        "project_items": [
            "Usean yrityksen RAG-arkkitehtuuri eristetyillä hakemuskonteksteilla",
            "Hybridi avainsana- ja vektorihaku Azure AI Searchilla",
            "Vektoriupotukset Azure OpenAI:lla",
            "Metadatasuodatus yrityskohtaiselle ja globaalille hakijatiedolle",
            "Keskusteluhistorian huomioiva kyselyiden uudelleenkirjoitus jatkokysymyksille",
            "Lähteisiin perustuvat LLM-vastaukset inline-viitteillä ja tarkasteltavalla evidenssillä",
            "Automatisoitu yritysten lisäys-, pilkkomis-, embedding- ja indeksointiputki",
            "Yritysten välisen eristyksen ja keskustelutietoisen haun evaluointi",
            "Rekrytoijille suunnattu Streamlit-käyttöliittymä läpinäkyvillä RAG-diagnostiikoilla",
        ],
        "view_project": "Näytä projekti GitHubissa",
        "open_live_project": "Kokeile AI Assistantia",
        "demo_access": "Demon käyttö",
        "demo_passcode": "Pääsykoodi",
        "demo_not_configured": "Live-demon URL-osoitetta ei ole vielä määritetty.",
        "how_it_works": "Miten Work Application Assistant toimii",
        "steps": [
            ("1. Tunnista", "Rekrytoija syöttää yrityksensä, jolloin sovellus valitsee oikean hakemuskontekstin."),
            ("2. Muotoile", "Jatkokysymykset kirjoitetaan tarvittaessa uudelleen itsenäisiksi hakukyselyiksi."),
            ("3. Hae", "Azure AI Search suorittaa hybridin avainsana- ja vektorihaun."),
            ("4. Suodata", "Metadatasuodatus rajaa evidenssin aktiiviseen yritykseen ja globaaliin hakijatietoon."),
            ("5. Vastaa", "Azure OpenAI muodostaa lähteisiin perustuvan vastauksen viittauksineen."),
        ],
        "retrieval_eval": "Haun evaluointi",
        "company_isolation": "Yrityseristys",
        "conversation_tests": "Keskustelutestit",
        "see_ui": "Näytä sovelluksen käyttöliittymä",
        "see_rag": "Näytä RAG-haun tiedot",
        "rag_caption": "Evidenssi, viittaukset ja RAG-haun tiedot",
        "experience": "Työkokemus",
        "job_role": "IT-asiantuntija / IT Development · 04/2024 – 09/2026",
        "development_apis": "Kehitys & API:t",
        "development_items": [
            "Kehitin ja modernisoin myymälä- ja keräilysovelluksia",
            "Rakensin, testasin ja selvitin REST API -integraatioita",
            "Testasin ja dokumentoin liiketoimintajärjestelmien välisiä integraatioita",
        ],
        "automation": "Automaatio",
        "automation_items": [
            "Automatisoin verkkokaupan viikoittaista ja kuukausittaista sisältöjulkaisua",
            "Automatisoin sisäisiä lomakkeita, hyväksyntäprosesseja ja tietovirtoja Power Automatella",
        ],
        "systems_data": "Järjestelmät & Data",
        "systems_items": [
            "Työskentelin verkkokauppa-, PIM- ja ERP-ympäristöissä",
            "Ylläpidin tuotetietojen ja sertifikaattitietojen laatua",
        ],
        "education": "Koulutus",
        "degree": "Tradenomi",
        "degree_field": "Tietojenkäsittely",
        "contact": "Ota yhteyttä",
        "copy": "Kopioi",
        "copied": "Kopioitu!",
    },
}

def tr(key):
    return LANG[st.session_state.portfolio_language][key]

language_choice = st.radio(
    tr("language"),
    ["EN", "FI"],
    horizontal=True,
    index=0 if st.session_state.portfolio_language == "en" else 1,
    key="portfolio_language_selector",
)

selected_language = language_choice.lower()
if selected_language != st.session_state.portfolio_language:
    st.session_state.portfolio_language = selected_language
    st.rerun()


# -------------------------
# INTRO / ABOUT
# -------------------------

st.markdown('<div id="home" class="anchor"></div>', unsafe_allow_html=True)

left, right = st.columns([1.8, 1], gap="large")

with left:
    st.markdown(f"""
    <div class="intro-card">
        <div class="intro-name">Miika Koivisto</div>
        <div class="intro-role">{tr("role")}</div>
        <div class="intro-divider"></div>
        <div class="intro-about-title">{tr("about_title")}</div>
        <p class="intro-about">{tr("about_1")}</p>
        <p class="intro-about">{tr("about_2")}</p>
        <p class="intro-about">{tr("about_3")}</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.image("assets/profile.jpeg", width=280)

st.write("")

button1, button2, button3, button4 = st.columns(4)

with button1:
    st.link_button("GitHub", "https://github.com/MiikaKoivisto", use_container_width=True)

with button2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/miikakoivisto98", use_container_width=True)

with button3:
    english_cv = Path("assets/Koivisto_Miika_Resume.pdf")
    if english_cv.exists():
        with english_cv.open("rb") as pdf_file:
            st.download_button(
                label=tr("cv_en"),
                data=pdf_file.read(),
                file_name=english_cv.name,
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.button(tr("cv_en"), disabled=True, use_container_width=True)

with button4:
    finnish_cv = Path("assets/Koivisto_Miika_Resume_FI.pdf")

    if finnish_cv.exists():
        with finnish_cv.open("rb") as pdf_file:
            st.download_button(
                label=tr("cv_fi"),
                data=pdf_file.read(),
                file_name="Koivisto_Miika_Resume_FI.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.button(tr("cv_fi"), disabled=True, use_container_width=True)

st.divider()

# -------------------------
# SKILLS
# -------------------------

st.markdown('<div id="skills" class="anchor"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{tr("skills")}</div>', unsafe_allow_html=True)

skill_cards = [
    (tr("skill_ai"), ["Azure OpenAI", "Azure AI Search", "Microsoft Foundry", "RAG", "Vector Embeddings", "Hybrid Search", "Microsoft Azure"]),
    (tr("skill_programming"), ["Python", "JavaScript", "HTML", "CSS", "JSON", "XML"]),
    (tr("skill_automation"), ["REST API", "Postman", "Power Automate", "Power Apps", "UiPath", "RPA"]),
    (tr("skill_systems"), ["PIM", "ERP Systems", "WMS", "Cloudinary", "SharePoint", "Docker", "AWS", "Streamlit"]),
]

skill_columns = st.columns(4)
for column, (title, skills) in zip(skill_columns, skill_cards):
    chips = "".join(f'<span class="skill-chip">{skill}</span>' for skill in skills)
    with column:
        skill_html = f"""<div class="skill-card">
<h3>{title}</h3>
<div class="skill-chip-container">{chips}</div>
</div>"""
        st.markdown(skill_html, unsafe_allow_html=True)

# -------------------------
# PROJECTS
# -------------------------

st.markdown('<div id="projects" class="anchor"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{tr("featured_project")}</div>', unsafe_allow_html=True)

project_items_html = "".join(f"<li>{item}</li>" for item in tr("project_items"))

live_button = (
    f'<a class="project-btn" href="{WORK_APPLICATION_URL}" target="_blank" rel="noopener noreferrer">'
    f'{tr("open_live_project")}</a>'
    if WORK_APPLICATION_URL
    else f'<span class="project-btn project-btn-disabled">{tr("open_live_project")}</span>'
)

demo_access = ""
if WORK_APPLICATION_PASSCODE:
    demo_access = f"""
    <div class="project-demo-access">
        <span class="project-demo-label">{tr("demo_access")}</span>
        <code class="project-demo-code">{WORK_APPLICATION_PASSCODE}</code>
    </div>
    """

project_html = textwrap.dedent(f"""
<div class="content-card project-feature-card">
<h3>AI Work Application Assistant</h3>
<p>{tr("project_intro")}</p>
<p><strong>{tr("what_built")}</strong></p>
<ul>{project_items_html}</ul>
<div class="project-actions">
<a class="project-btn" href="https://github.com/MiikaKoivisto/Work-Application-Assistant" target="_blank" rel="noopener noreferrer">{tr("view_project")}</a>
<div class="project-assistant-row">
{live_button}
{demo_access}
</div>
</div>
</div>
""").strip()

st.markdown(project_html, unsafe_allow_html=True)

if not WORK_APPLICATION_URL:
    st.caption(tr("demo_not_configured"))
st.write("")
st.markdown(f'<div class="section-title">{tr("how_it_works")}</div>', unsafe_allow_html=True)

step_columns = st.columns(5)
for column, (title, description) in zip(step_columns, tr("steps")):
    with column:
        st.markdown(f"### {title}")
        st.write(description)

st.write("")
metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.metric(tr("retrieval_eval"), "100%")
with metric2:
    st.metric(tr("company_isolation"), "100%")
with metric3:
    st.metric(tr("conversation_tests"), "3 / 3")

st.write("")

application_ui = Path("assets/WorkApplicationAssistant.png")
rag_debug = Path("assets/WorkApplicationRAG.png")

if application_ui.exists():
    with st.expander(tr("see_ui")):
        st.image(str(application_ui), caption="AI Work Application Assistant")

if rag_debug.exists():
    with st.expander(tr("see_rag")):
        st.image(str(rag_debug), caption=tr("rag_caption"))

# -------------------------
# EXPERIENCE
# -------------------------

st.markdown('<div id="experience" class="anchor"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{tr("experience")}</div>', unsafe_allow_html=True)

development_items = "".join(f"<li>{item}</li>" for item in tr("development_items"))
automation_items = "".join(f"<li>{item}</li>" for item in tr("automation_items"))
systems_items = "".join(f"<li>{item}</li>" for item in tr("systems_items"))

experience_html = f"""<div class="experience-card">
<div class="experience-company">LVI-Dahl Suomi Oy</div>
<div class="experience-role">{tr("job_role")}</div>

<div class="experience-category">{tr("development_apis")}</div>
<ul>{development_items}</ul>

<div class="experience-category">{tr("automation")}</div>
<ul>{automation_items}</ul>

<div class="experience-category">{tr("systems_data")}</div>
<ul>{systems_items}</ul>
</div>"""
st.markdown(experience_html, unsafe_allow_html=True)


# -------------------------
# EDUCATION
# -------------------------

st.markdown('<div id="education" class="anchor"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-title">{tr("education")}</div>', unsafe_allow_html=True)

education_html = f"""<div class="content-card">
<h3>{tr("degree")}</h3>
<p><strong>{tr("degree_field")}</strong></p>
<p>HAMK University of Applied Sciences | 08/2021 – 06/2025</p>
</div>"""
st.markdown(education_html, unsafe_allow_html=True)

# -------------------------
# CONTACT
# -------------------------

st.markdown('<div id="contact" class="anchor"></div>', unsafe_allow_html=True)

contact_title = tr("contact")
copy_label = tr("copy")
copied_label = tr("copied")

components.html(
    f"""
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            color: #f0f2f6;
        }}
        .contact-card {{
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #30363d;
            background: #161b22;
        }}
        .contact-card h2 {{
            margin: 0 0 1.1rem 0;
            font-size: 2rem;
        }}
        .contact-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 0.75rem 0.9rem;
            margin-top: 0.7rem;
            border: 1px solid #30363d;
            border-radius: 9px;
            background: #0e1117;
        }}
        .contact-value {{
            user-select: text;
            font-size: 0.95rem;
        }}
        .copy-btn {{
            padding: 0.38rem 0.7rem;
            border: 1px solid #30363d;
            border-radius: 7px;
            background: #161b22;
            color: #f0f2f6;
            cursor: pointer;
        }}
        .copy-btn:hover {{
            border-color: rgba(120, 180, 255, 0.8);
        }}
    </style>

    <div class="contact-card">
        <h2>{contact_title}</h2>

        <div class="contact-row">
            <span class="contact-value">📧 Miikak123@gmail.com</span>
            <button class="copy-btn" onclick="copyValue('Miikak123@gmail.com', this)">
                {copy_label}
            </button>
        </div>

        <div class="contact-row">
            <span class="contact-value">📞 +358 505731282</span>
            <button class="copy-btn" onclick="copyValue('+358505731282', this)">
                {copy_label}
            </button>
        </div>
    </div>

    <script>
        function copyValue(value, button) {{
            navigator.clipboard.writeText(value).then(() => {{
                const original = button.innerText;
                button.innerText = "{copied_label}";
                setTimeout(() => {{
                    button.innerText = original;
                }}, 1200);
            }});
        }}
    </script>
    """,
    height=245,
)
