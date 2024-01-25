import streamlit as st
from pandas import DataFrame
from recomend_system import get_meal_options, parse_to_process


def app():
    meal_option = None

    st.title("Recomendação de refeições")
    col1, col2 = st.columns(2)

    weight = col1.number_input("Seu peso", 0.0, 200.0, 0.0, 0.1, "%.2f")

    height = col2.number_input("Sua altura", 0.0, 2.5, 0.0, 0.01, "%.2f")

    activity_level = col1.selectbox(
        "nível de atividade física",
        ["Sedentária", "Leve", "Moderara", "intensa", "muito intensa"],
        None,
    )

    current_meal = col2.selectbox(
        "Refeição", ["Café da manhã", "Brunch", "Janta"], None
    )

    if current_meal:
        meal_option = st.selectbox(
            "Opções de refeição", get_meal_options(current_meal), None
        )

    age = st.number_input("Sua idade", 0, 100, 0, 1)

    gender = st.radio("Seu gênero", ["Masculino", "Feminino"], None)

    button = st.button("Recomendar refeição")

    if button:
        if not gender or not activity_level or not current_meal or not meal_option:
            st.subheader("Preencha todos os campos")
        else:
            recomendations = parse_to_process(
                weight,
                height,
                age,
                gender,
                activity_level,
                current_meal,
                meal_option,
            )
            st.write("Opções de pratos similares ao escolhido:")
            st.dataframe(recomendations, hide_index=True)


app()
