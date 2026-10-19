# fcos.py - Food Court Ordering System (Beginner)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fms import Food, add_food, food_list

# Tambah 10 item menu
menu_items = [
    Food("F01", "Burger", 5.00, 20),
    Food("F02", "Pizza", 8.50, 15),
    Food("F03", "Pasta", 7.00, 10),
    Food("F04", "Sandwich", 4.00, 25),
    Food("F05", "Salad", 3.50, 30),
    Food("F06", "Fried Rice", 6.00, 20),
    Food("F07", "Noodles", 5.50, 18),
    Food("F08", "Soup", 4.50, 12),
    Food("F09", "Tea", 2.00, 40),
    Food("F10", "Coffee", 2.50, 35),
]

for item in menu_items:
    add_food(item)

st.title("🍴 Food Court Ordering System")

# Pilih makanan
selected = st.multiselect("Select Food Items", [f.name for f in food_list])
quantities = {}
for name in selected:
    qty = st.number_input(f"Quantity for {name}", min_value=1, step=1)
    quantities[name] = qty

# Generate Receipt
if st.button("Generate Receipt"):
    data = []
    total = 0
    for f in food_list:
        if f.name in selected:
            qty = quantities[f.name]
            subtotal = f.price * qty
            data.append([f.name, f.price, qty, subtotal])
            total += subtotal

    df = pd.DataFrame(data, columns=["Food", "Price", "Quantity", "Subtotal"])
    st.write(df)
    st.success(f"Total Price: RM{total:.2f}")

    # Bar Chart
    fig, ax = plt.subplots()
    ax.bar(df["Food"], df["Price"])
    ax.set_title("Food Price Bar Chart")
    ax.set_xlabel("Food")
    ax.set_ylabel("Price (RM)")
    for i, v in enumerate(df["Price"]):
        ax.text(i, v + 0.1, f"RM{v:.2f}", ha="center")
    st.pyplot(fig)
