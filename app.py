import random
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Aprende con Gamaliel", page_icon="🌟", layout="wide"
)

# Estilos CSS personalizados para mejorar el diseño visual y botones grandes
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        background-color: #ff4b4b;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #ff1c1c;
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #1e3d59;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título principal
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>🚀 El Mundo Mágico de Gamaliel 🌟</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: #1e3d59;'>¡Aprende jugando, sumando, restando y descubriendo palabras!</h3>",
    unsafe_allow_html=True,
)

# Menú de navegación lateral
menu = st.sidebar.selectbox(
    "🎯 Elige una sección:",
    [
        "Inicio",
        "🧮 Matemática Divertida",
        "📖 Lengua y Palabras",
        "⭐ Mis Logros",
    ],
)

if menu == "Inicio":
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400",
            use_container_width=True,
        )
    st.markdown(
        "<h3 style='text-align: center;'>¡Bienvenido! Usa el menú de la izquierda para empezar la aventura.</h3>",
        unsafe_allow_html=True,
    )

elif menu == "🧮 Matemática Divertida":
    st.header("🧮 Zona de Matemática con Apoyo Visual")

    opcion_mat = st.radio(
        "Elige el juego:",
        ["Sumas con Objetos", "Restas Mágicas", "Tablas y Multiplicaciones"],
    )

    if opcion_mat == "Sumas con Objetos":
        st.subheader("🍎 Sumemos con frutas y elementos visuales")
        n1 = random.randint(1, 5)
        n2 = random.randint(1, 5)

        st.markdown(
            f"<div class='card'>¿Cuánto es {'🍎' * n1} ({n1}) + {'🍎' * n2} ({n2})?</div>",
            unsafe_allow_html=True,
        )

        respuesta = st.number_input(
            "Escribe tu respuesta:", min_value=0, max_value=20, step=1, key="suma"
        )
        if st.button("¡Comprobar Suma!"):
            if respuesta == (n1 + n2):
                st.success(
                    "🎉 ¡Excelente! ¡Lo lograste! 🌟 Estrellas para Gamaliel."
                )
                st.balloons()
            else:
                st.error(
                    "❌ ¡Casi! Vuelve a contar los dibujitos. ¡Tú puedes!"
                )

    elif opcion_mat == "Restas Mágicas":
        st.subheader("🎈 Restas divertidas")
        n1 = random.randint(3, 8)
        n2 = random.randint(1, n1)

        st.markdown(
            f"<div class='card'>De {'🎈' * n1} ({n1}), si pinchamos {'🎈' * n2} ({n2}), ¿cuántos quedan?</div>",
            unsafe_allow_html=True,
        )

        respuesta = st.number_input(
            "Escribe tu respuesta:", min_value=0, max_value=20, step=1, key="resta"
        )
        if st.button("¡Comprobar Resta!"):
            if respuesta == (n1 - n2):
                st.success("🎉 ¡Muy bien hecho! ¡Genio total! 🚀")
                st.balloons()
            else:
                st.error("❌ ¡Inténtalo de nuevo! Mira bien los globos.")

    elif opcion_mat == "Tablas y Multiplicaciones":
        st.subheader("⭐ Tablas de multiplicar visuales (Nivel 4° Grado)")
        n1 = random.randint(2, 5)
        n2 = random.randint(2, 5)

        st.markdown(
            f"<div class='card'>Calcula: {n1} veces el número {n2} ({n1} x {n2})</div>",
            unsafe_allow_html=True,
        )
        respuesta = st.number_input(
            "Tu respuesta:", min_value=0, max_value=50, step=1, key="multi"
        )
        if st.button("¡Comprobar Multiplicación!"):
            if respuesta == (n1 * n2):
                st.success("🏆 ¡Impresionante! ¡Vas directo a 4° grado! 🌟")
                st.balloons()
            else:
                st.error("❌ ¡Prueba otra vez! Puedes usar tus deditos o marcas.")

elif menu == "📖 Lengua y Palabras":
    st.header("📖 Zona de Lengua: Memoria Ocular y Deletreo")

    juego_lengua = st.radio(
        "Elige el desafío:",
        ["Memoria Visual (Encuentra la palabra)", "Deletreo de Palabras"],
    )

    if juego_lengua == "Memoria Visual (Encuentra la palabra)":
        st.subheader(
            "👁️ Memoria Ocular: Observa la imagen y selecciona la palabra correcta"
        )

        palabras_dict = {
            "🐶 Perro": "Perro",
            "🚗 Auto": "Auto",
            "🏡 Casa": "Casa",
            "🌳 Árbol": "Árbol",
            "⚽ Pelota": "Pelota",
        }
        item_elegido = random.choice(list(palabras_dict.keys()))
        correcta = palabras_dict[item_elegido]

        st.markdown(
            f"<div class='card'>¿Qué ves aquí? <br><span style='font-size: 60px;'>{item_elegido.split()[0]}</span></div>",
            unsafe_allow_html=True,
        )

        opciones = list(palabras_dict.values())
        random.shuffle(opciones)

        eleccion = st.selectbox("Selecciona la palabra escrita correcta:", opciones)

        if st.button("¡Verificar Palabra!"):
            if eleccion == correcta:
                st.success(
                    f"🎉 ¡Exacto! Tu memoria ocular reconoció la palabra **{correcta}** a la perfección."
                )
                st.balloons()
            else:
                st.error("❌ Mírvala bien de nuevo. ¡Inténtalo otra vez!")

    elif juego_lengua == "Deletreo de Palabras":
        st.subheader("🔤 Deletreo paso a paso")
        st.markdown(
            "Ordena las letras en tu mente y escribe la palabra que corresponde a la imagen 🐱"
        )

        st.markdown(
            "<div class='card'>🐱 = G - A - T - O</div>", unsafe_allow_html=True
        )

        palabra_usuario = st.text_input(
            "Escribe la palabra completa:"
        ).strip().capitalize()

        if st.button("¡Comprobar Deletreo!"):
            if palabra_usuario == "Gato":
                st.success("🏆 ¡Increíble! ¡Deletreador experto! 🌟")
                st.balloons()
            else:
                st.error("❌ Revisa las letras: G-A-T-O. ¡Inténtalo otra vez!")

elif menu == "⭐ Mis Logros":
    st.header("🏆 ¡Panel de Campeón!")
    st.markdown(
        "<div class='card'>¡Aquí guardamos todas tus estrellas y avances diarios! 🌟🚀</div>",
        unsafe_allow_html=True,
    )
    st.balloons()
