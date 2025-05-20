import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Kangaroo Planet",
    page_icon="🦘",
    layout="wide"
)

# Chemins des fichiers
logo = "logo.jpg"
screenshot_1 = "kang.png"
screenshot_2 = "lune.png"

# Style CSS custom simple
st.markdown("""
    <style>
        .title-container {
            background: linear-gradient(135deg, #3f87a6, #ebf8e1, #f69d3c);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: #000000;
        }
        .title-container h1 {
            font-size: 48px;
            margin-bottom: 10px;
        }
        .title-container p {
            font-size: 18px;
        }
        .section-title {
            font-size: 30px;
            margin-top: 40px;
            color: #444;
        }
        .testimonial {
            font-style: italic;
            color: #555;
            margin-bottom: 10px;
        }
        .resource-link {
            font-size: 18px;
            padding: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Logo + Présentation
col1, col2 = st.columns([2, 3])
with col1:
    st.image(logo, use_container_width=True)
with col2:
    st.markdown("""
        <div class='title-container'>
            <h1>🌍 Kangaroo Planet</h1>
            <h3>Piou piou piou</h3>
            <p><strong>Kangaroo Planet</strong> est un jeu d'action-survie-shooter immersif où vous incarnez un kangourou défendant sa planète d'une invasion humaine. 
            Préparez-vous à combattre des ennemis redoutables et méchants !</p>
        </div>
    """, unsafe_allow_html=True)

# 🎮 Un jeu captivant
st.markdown("<div class='section-title'>🎮 Un jeu captivant</div>", unsafe_allow_html=True)
st.markdown("""
- 🦘 **Incarnez un kangourou et SHOOTEZ-LES TOUS**
- 😌 **Un jeu qui détend avant tout**
- 🎶 **Profitez d'une bonne musique en fond tout en exterminant les bad guys**
- 🔊 **Musique d’ambiance : Veridis Quo**
""")

# 📸 Aperçu du jeu
st.markdown("<div class='section-title'>📸 Aperçu du jeu</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image(screenshot_1, use_container_width=True, caption="Incarnez le meilleur des animaux : un kangourou")
with col2:
    st.image(screenshot_2, use_container_width=True, caption="Un univers magnifique et rigolo")

# 🛠️ Outils utilisés
st.markdown("<div class='section-title'>🛠️ Outils utilisés</div>", unsafe_allow_html=True)
st.markdown("""
- 🎨 **Blender** : pour la modélisation 3D et les animations.
- 🕹️ **Unity** : pour le gameplay, la gestion physique et le rendu.
- 🎼 **FL Studio** : pour certaines ambiances sonores et bruitages.
""")

# 🚀 Coulisses du développement
st.markdown("<div class='section-title'>🚀 Coulisses du développement</div>", unsafe_allow_html=True)
st.markdown("""
- 🧠 **IA ennemie** : comportements dynamiques et adaptatifs.
- 🧱 **Scripts** : gestion des vagues, armes, scoring.
- 🌌 **Direction artistique** : paysages extraterrestres + vibes australiennes.
""")

# 💬 Témoignages
st.markdown("<div class='section-title'>💬 Ce que disent les joueurs</div>", unsafe_allow_html=True)
testimonials = [
    "'Une expérience inoubliable, Kangaroo Planet est vraiment hors du commun !' – Alex",
    "'Des combats épiques et une exploration incroyable !' – Mia",
    "'Le jeu le plus immersif que j'ai joué cette année !' – Lucas",
    "'Un jeu créé par des goats pour les goats...' – Le grand-frère de Lucas",
    "'Dinguerie' – Le papa de Lucas",
    "'J'ai arrêté mon addiction à la douche grâce à Kangaroo Planet' – Kévin"
]
for t in testimonials:
    st.markdown(f"<div class='testimonial'>⭐️⭐️⭐️⭐️⭐️ {t}</div>", unsafe_allow_html=True)

# 📄 Rapport de soutenance
st.markdown("<div class='section-title'>📄 Téléchargez notre rapport de soutenance</div>", unsafe_allow_html=True)
st.markdown("""
Ce rapport présente en détail le processus de développement, les choix techniques et les fonctionnalités principales de **Kangaroo Planet**.
""")
with open("rapport_soutenance.pdf", "rb") as file:
    st.download_button(
        label="📥 Télécharger le rapport", 
        data=file, 
        file_name="rapport_soutenance.pdf", 
        mime="application/pdf"
    )
# 📁 Ressources
st.markdown("<div class='section-title'>📁 Les ressources utilisées</div>", unsafe_allow_html=True)
resources = [
    "🔗 [Blender](https://www.blender.org/download/)",
    "🔗 [Unity](https://www.unity.com)",
    "🔗 Musique : [Veridis Quo – Daft Punk](https://www.youtube.com/watch?v=TCd6PfxOy0Y)"
]
for r in resources:
    st.markdown(r)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)

st.header("👥 **L'équipe Kangaroo Planet**")
st.markdown("""
- 🟩 **Eliott - L’Énergique** : Sportif discipliné, il a transformé ses efforts en force mentale. A remplacé Windows par Linux au lycée.
- 🟪 **Nicolas - L’Inventif** : Passionné de Minecraft et de création de mondes. Expérimenté en modération de serveurs Discord.
- 🟥 **Hélios - Le Codeur** : Programme depuis la 6e, spécialisé en développement web. Il assure toute la structure technique du jeu.
- 🟧 **Tanguy - Le Stratège** : Amoureux des maths et des échecs, il a exploré la programmation d’IA pour mieux dominer le plateau.
""")

st.subheader("📧 **Contacts de l'équipe**")
st.markdown("""
- Tanguy : [tanguy.de-jerphanion@epita.fr](mailto:tanguy.de-jerphanion@epita.fr)
- Hélios : [helios.bringuet@epita.fr](mailto:helios.bringuet@epita.fr)
- Eliott : [eliott.caquelot@epita.fr](mailto:eliott.caquelot@epita.fr)
- Nicolas : [nicolas.delisle@epita.fr](mailto:nicolas.delisle@epita.fr)
""")
st.write("---")

st.markdown("<center>© 2025 Kangaroo Planet Team. Tous droits réservés.</center>", unsafe_allow_html=True)
