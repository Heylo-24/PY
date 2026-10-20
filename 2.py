import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Display the title
st.title("Food Court Ordering System (FCOS)")

# 2. Dictionary to store food names and prices
foods = {
    "Nasi Goreng": 8.00,
    "Mee Goreng": 7.00,
    "Chicken Chop": 12.00,
    "Burger Special": 6.50,
    "Teh Tarik Ais": 3.00
}

# 3. Enter the number of food types to purchase
quantity = st.number_input(
    "Enter the number of food types to purchase:",
    min_value=1,
    max_value=len(foods),
    step=1
)

# 4. Create two empty lists
food_names = []
food_prices = []

# 5. Use a for loop and selectbox
for i in range(int(quantity)):
    st.subheader(f"Food Item {i + 1}")

    food = st.selectbox(
        f"Select food {i + 1}:",
        list(foods.keys()),
        key=f"food_{i}"
    )

    # 6. Display the price of each selected food
    price = foods[food]
    st.write(f"Price: RM {price:.2f}")

    # 7. Store the food name and price using append()
    food_names.append(food)
    food_prices.append(price)

# 8. Create a Generate Receipt button
if st.button("Generate Receipt"):

    # 9. Calculate total price and quantity
    total_price = sum(food_prices)
    total_quantity = len(food_names)

    # Create a Pandas DataFrame
    receipt = pd.DataFrame({
        "Food Name": food_names,
        "Price (RM)": food_prices
    })

    # Display food records
    st.subheader("Receipt")
    st.dataframe(receipt)

    # Display total price and quantity
    st.write(f"Total Price: RM {total_price:.2f}")
    st.write(f"Total Quantity: {total_quantity}")

    # 10. Create a bar chart using Matplotlib
    fig, ax = plt.subplots()

    bars = ax.bar(food_names, food_prices, color='orange')

    ax.set_xlabel("Food Name")
    ax.set_ylabel("Price (RM)")
    ax.set_title("Food Price Chart")

    # Display price above each bar
    ax.bar_label(
        bars,
        labels=[f"RM {price:.2f}" for price in food_prices],
        padding=3
    )

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    st.pyplot(fig)
