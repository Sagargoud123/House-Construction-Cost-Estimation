
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(page_title="House Construction Cost Estimation", layout="wide")

st.title(" House Construction Cost & Completion Estimation")


st.header(" Enter House Details")

col1, col2 = st.columns(2)

with col1:
    land_area = st.number_input("Land Area (sq.ft)", 500, 10000, 1200)
    floors = st.number_input("Number of Floors", 1, 5, 1)
    rooms = st.number_input("Number of Rooms", 1, 10, 3)
    no_of_labour = st.number_input("Number of Labour", 1, 50, 6)
    labour_cost_per_day = st.number_input("Labour Cost per Day (INR)", 200, 5000, 500)
    work_efficiency = st.number_input(
        "Work Efficiency (sq.ft / day / labour)", 50, 500, 120
    )

with col2:
    cement_rate = st.number_input("Cement Rate (INR / ton)", 3000, 8000, 5000)
    bricks_rate = st.number_input("Bricks Rate (INR / brick)", 2, 20, 10)
    steel_rate = st.number_input("Steel Rate (INR / ton)", 40000, 120000, 75000)


if st.button(" Estimate Construction"):


    total_builtup_area = land_area * floors

    cement_bags_per_sqft = 0.45
    bricks_per_sqft = 9
    steel_kg_per_sqft = 4

    room_factor = 1 + (rooms * 0.02)

    cement_bags = total_builtup_area * cement_bags_per_sqft * room_factor
    cement_qty = cement_bags / 20  

    bricks_qty = total_builtup_area * bricks_per_sqft * room_factor
    steel_qty = (total_builtup_area * steel_kg_per_sqft * room_factor) / 1000 


    material_cost = (
        cement_qty * cement_rate +
        bricks_qty * bricks_rate +
        steel_qty * steel_rate
    )

 
    active_days = total_builtup_area / (no_of_labour * work_efficiency)

    site_prep = 7
    foundation_curing = 10
    column_curing = 7 * floors
    slab_curing = 7 * floors
    plaster_drying = 5
    painting_drying = 4
    finishing = 7

    buffer_days = (
        site_prep +
        foundation_curing +
        column_curing +
        slab_curing +
        plaster_drying +
        painting_drying +
        finishing
    )

    total_days = round(active_days + buffer_days, 1)


    labour_cost = total_days * no_of_labour * labour_cost_per_day

    total_cost = material_cost + labour_cost

    st.success(f"###  Estimated Total Cost: ₹ {total_cost:,.2f}")
    st.info(f"###  Estimated Completion Time: {total_days} days")

    st.subheader(" Material Requirement")
    st.write(f"Built-up Area: {total_builtup_area} sq.ft")
    st.write(f"Cement: {cement_qty:.2f} tons")
    st.write(f"Bricks: {int(bricks_qty)} bricks")
    st.write(f"Steel: {steel_qty:.2f} tons")


    labels = ["Material Cost", "Labour Cost"]
    values = [material_cost, labour_cost]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    ax.set_title("Cost Distribution")
    st.pyplot(fig)
