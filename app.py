# app.py - Main Application
import streamlit as st
import fms
import fcos

st.title("🍴 Food Business System")

menu = st.sidebar.selectbox("Menu", ["Add Food", "View Food", "Search Food", "Place Order", "Food Court System", "About"])

if menu == "Add Food":
    st.subheader("Add Food")
    food_id = st.text_input("Food ID")
    name = st.text_input("Food Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    if st.button("Save Food"):
        new_food = fms.Food(food_id, name, price, quantity)
        fms.add_food(new_food)
        st.success("Food added successfully!")

elif menu == "View Food":
    st.subheader("View Food")
    for food in fms.food_list:
        st.write(str(food))

elif menu == "Search Food":
    st.subheader("Search Food")
    keyword = st.text_input("Enter food name")
    if st.button("Search"):
        results = fms.search_food(keyword)
        if results:
            for f in results:
                st.write(str(f))
        else:
            st.error("Food not found!")

elif menu == "Place Order":
    st.subheader("Place Order")
    food_id = st.text_input("Food ID to order")
    qty = st.number_input("Quantity", min_value=1, step=1)
    if st.button("Order"):
        if fms.place_order(food_id, qty):
            st.success("Order placed successfully!")
        else:
            st.error("Invalid order or insufficient stock.")

elif menu == "Food Court System":
    st.subheader("Food Court Ordering System")
    fcos.main()  # panggil fungsi utama dari fcos.py

elif menu == "About":
    st.write("This is a order")
