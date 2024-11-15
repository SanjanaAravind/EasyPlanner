import streamlit as st

st.title("Plan Your Day!")

import matplotlib.pyplot as plt
import numpy as np

# Function to create the pie chart
def create_pie_chart(data, mylabels, todo_labels, colors):
    combined_labels = [f"{time} - {activity}" for time, activity in zip(mylabels, todo_labels)]
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.pie(data, labels=combined_labels, colors=colors, startangle=180, counterclock=False, wedgeprops={'edgecolor': 'black'})
    st.pyplot(fig)

# Streamlit interface
#st.title('24-Hour Activity Pie Chart')

# Initialize the data
data = np.ones(24)
mylabels = [f"{i}:00" for i in range(24)]

# Default activity labels for 24 hours
default_todo_labels = [
    "Sleep", "Sleep", "Sleep", "Sleep", "Sleep", "Sleep",  # 0-5 AM
    "Breakfast", "Work", "Work", "Work", "Work", "Lunch",  # 6 AM - 11 AM
    "Work", "Work", "Break", "Work", "Work", "Dinner",     # 12 PM - 5 PM
    "Leisure", "Leisure", "Leisure", "Leisure", "Sleep", "Sleep"  # 6 PM - 11 PM
]

# Color coding for day/night time
colors = [
    '#000033', '#000033', '#000033', '#000044', '#000055', '#000077',
    '#ffffff', '#fffacd', '#fff8b0', '#fff599', '#fff380', '#fff066',
    '#ffed4d', '#ffcc00', '#ffaa00', '#ff8800', '#ff6600', '#ff6600',
    '#ff4400', '#000099', '#000066', '#000055', '#000044', '#000033'
]

# Collect input from the user for each label
todo_labels = []
for i in range(24):
    activity = st.text_input(f"Activity for {mylabels[i]}", default_todo_labels[i])
    todo_labels.append(activity)

# Show the updated pie chart
create_pie_chart(data, mylabels, todo_labels, colors)

