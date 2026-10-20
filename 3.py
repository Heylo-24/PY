import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Food Court Ordering System")

# menu
foods = {"Nasi Goreng":8,"Mee Goreng":7,"Chicken Chop":12,"Burger Special":6.5,"Teh Tarik Ais":3}

# input bilangan
qty = st.number_input("Bilangan jenis makanan:",1,len(foods),1)

names, prices = [], []

# loop pilihan
for i in range(int(qty)):
    food = st.selectbox(f"Makanan {i+1}", list(foods.keys()), key=i)
    names.append(food)
    prices.append(foods[food])

# receipt
if st.button("Resit"):
    total = sum(prices)
    df = pd.DataFrame({"Food":names,"Price":prices})
    st.dataframe(df)
    st.write("Total RM", total)

    # chart
    fig, ax = plt.subplots()
    ax.bar(names, prices, color="orange")
    st.pyplot(fig)
