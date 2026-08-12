import streamlit as st
import math

st.title("🍎 ¿Qué fruta es más parecida?")

st.write("Introduce las características de una fruta.")

# Datos de la fruta que queremos analizar
peso = st.number_input("Peso (gramos)", value=180)
diametro = st.number_input("Diámetro (cm)", value=7.0)
dulzor = st.number_input("Dulzor (0 - 10)", value=8.0)

# Convertimos los datos en un vector
fruta_usuario = [peso, diametro, dulzor]

st.write("Vector de tu fruta:", fruta_usuario)

# Frutas conocidas
manzana = [170, 7.0, 7]
banano = [120, 5.0, 9]
naranja = [200, 8.0, 6]
pera = [180, 7.5, 5] 

# Calculamos las distancias

distancia_manzana = math.sqrt(
    (fruta_usuario[0] - manzana[0])**2 +
    (fruta_usuario[1] - manzana[1])**2 +
    (fruta_usuario[2] - manzana[2])**2
)

distancia_banano = math.sqrt(
    (fruta_usuario[0] - banano[0])**2 +
    (fruta_usuario[1] - banano[1])**2 +
    (fruta_usuario[2] - banano[2])**2
)

distancia_naranja = math.sqrt(
    (fruta_usuario[0] - naranja[0])**2 +
    (fruta_usuario[1] - naranja[1])**2 +
    (fruta_usuario[2] - naranja[2])**2
)

distancia_pera = math.sqrt(
    (fruta_usuario[0] - pera[0])**2 +
    (fruta_usuario[1] - pera[1])**2 +
    (fruta_usuario[2] - pera[2])**2
)

# Mostramos las distancias
st.subheader("Distancias")

st.write("🍎 Manzana:", distancia_manzana)
st.write("🍌 Banano:", distancia_banano)
st.write("🍊 Naranja:", distancia_naranja)
st.write("🍐 Pera:", distancia_pera)

# Buscamos la distancia menor
distancias = {
    "🍎 Manzana": distancia_manzana,
    "🍌 Banano": distancia_banano,
    "🍊 Naranja": distancia_naranja,
    "🍐 Pera": distancia_pera
}

fruta_mas_parecida = min(distancias, key=distancias.get)

st.subheader("Resultado")

st.success(f"La fruta más parecida es: {fruta_mas_parecida}")

st.subheader("Descripción de la fruta")

match fruta_mas_parecida:
    case "🍎 Manzana":
        st.write("La manzana tiene forma redonda, piel fina de colores rojo, verde o amarillo, y pulpa blanca o jugosa con pequeñas semillas oscuras en el centro. Su sabor es dulce o ácido y es muy saludable.")
        
    case "🍌 Banano":
        st.write("La banana es el fruto carnoso y alargado de una gran planta herbácea del género Musa. Tiene forma curva, cáscara gruesa que cambia de verde a amarilla al madurar y pulpa suave. Es una de las frutas más consumidas del mundo por su sabor dulce y gran valor energético")
        
    case "🍊 Naranja":
        st.write("La naranja es una fruta cítrica redonda, de 6 a 10 cm de diámetro, con cáscara y pulpa anaranjadas. Su interior tiene de 8 a 12 gajos llenos de jugo jugoso y dulce o ácido. Es rica en vitamina C, fibra y agua")
        
    case "🍐 Pera":
        st.write("La pera es una fruta jugosa y carnosa con forma de lágrima o bombilla. Tiene piel lisa de color verde, amarillo o marrón, pulpa blanca muy refrescante y un sabor dulce y suave. Crece en los árboles llamados perales.")
        
    case _:
        st.write("No se encontró una descripción para esta fruta.")
