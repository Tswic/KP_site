import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(
    page_title="Kangaroo Planet",
    page_icon="🦘",
    layout="wide"
)

logo = "logo.jpg"  # Chemin correct et fichier existant
screenshot_1 = "kang.png"
screenshot_2 = "lune.png"

# Titre principal et introduction
col1, col2 = st.columns([2, 3])
with col1:
   st.image(logo, use_container_width=True)
with col2:
    st.markdown("""
    <div style='font-size: 39px;'>
        <br><br>
        <h1>🌍 Kangaroo Planet</h1>
        <h3>Piou piou piou</h3>
        <p><strong>Kangaroo Planet</strong> est un jeu d'action-survie-shooter immersif où vous incarnez un kangourou défendant sa planète d'une invasion humaine. 
        Préparez-vous à combattre des ennemis redoutables et méchants !</p>
    </div>
    """, unsafe_allow_html=True)

# Section : Un jeu captivant
st.header("🎮 **Un jeu captivant**")
st.markdown("""
- **Incarnez un kangourou et SHOOTEZ-LES TOUS**
- **Un jeu qui détend avant tout**
- **Profitez d'une bonne musique en fond tout en exterminant les bad guys**
- **🎵 Musique d’ambiance : Veridis Quo**
""")

# Section : Aperçu du jeu
st.header("📸 **Aperçu du jeu**")
col1, col2 = st.columns(2)
with col1:
    st.image(screenshot_1, use_container_width=True, caption="Incarnez le meilleur des animaux : un kangourou")
with col2:
    st.image(screenshot_2, use_container_width=True, caption="Un univers magnifique et rigolo")

# Section : Outils utilisés
st.header("🛠️ **Outils utilisés**")
st.markdown("""
Pour donner vie à **Kangaroo Planet**, nous avons utilisé des outils puissants du monde du jeu vidéo :

- 🎨 **Blender** pour la modélisation 3D et les animations.
- 🕹️ **Unity** pour le développement du gameplay, la gestion physique et le rendu final.
- 🎼 **FL Studio** pour certaines ambiances sonores.
""")

# Section : Coulisses du développement
st.header("🚀 **Coulisses du développement**")
st.write("""
L'équipe derrière **Kangaroo Planet** a travaillé d'arrache-pied pour offrir une expérience de jeu fluide et captivante. Voici quelques faits marquants :
- **Scripts principaux :** Gestion des ennemis, armes, et spawn dynamique, optimisés pour une performance maximale.
- **Intelligence artificielle :** Un système de comportement complexe permettant aux ennemis de s'adapter aux actions du joueur.
- **Graphismes :** Univers visuel unique, inspiré des paysages extraterrestres et de l'Australie sauvage.
""")

# Section : Témoignages
st.header("💬 **Ce que disent les joueurs**")
testimonials = [
    "⭐️⭐️⭐️⭐️⭐️ 'Une expérience inoubliable, Kangaroo Planet est vraiment hors du commun !' - Alex",
    "⭐️⭐️⭐️⭐️ 'Des combats épiques et une exploration incroyable !' - Mia",
    "⭐️⭐️⭐️⭐️⭐️ 'Le jeu le plus immersif que j'ai joué cette année !' - Lucas",
    "⭐️⭐️⭐️⭐️⭐️ 'Un jeu créé par des goats pour les goats...' - Le grand-frère de Lucas",
    "⭐️⭐️⭐️⭐️⭐️ 'Dinguerie' - Le papa de Lucas",
    "⭐️⭐️⭐️⭐️⭐️ 'J'ai arrêté mon addiction à la douche grâce à Kangaroo Planet' - Kévin"
]
for testimonial in testimonials:
    st.markdown(f"> {testimonial}")

st.write("---")
# Section : Téléchargement du rapport
st.header("📄 **Téléchargez notre rapport de soutenance**")
st.write("""
Vous pouvez télécharger notre rapport de soutenance en cliquant sur le bouton ci-dessous.
Ce rapport présente en détail le processus de développement, les choix techniques et les fonctionnalités principales du jeu **Kangaroo Planet**.
""")
with open("rapport_soutenance.pdf", "rb") as file:
    st.download_button(
        label="Télécharger le rapport de soutenance", 
        data=file, 
        file_name="rapport_soutenance.pdf", 
        mime="application/pdf"
    )

st.write("---")
# Section : Contact et fin
st.write("Nous n'avons pas de réseaux car nous sommes mystérieux mais nous sommes des élèves de la promo 2029 de l'EPITA !")

st.write("---")
st.header("📁 **les ressources utilisées**")
dos = {
    "[Blender](https://www.blender.org/download/)",
    "[Unity](https://www.unity.com)"
}

for i in dos:
    st.markdown(i)

st.markdown("© 2025 Kangaroo Planet Team. Tous droits réservés.")
