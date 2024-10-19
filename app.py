import streamlit as st
import pandas as pd

# Streamlit App Title
st.title("Student's Day Timetable")

# Create lists to hold timetable data
tasks = []
start_times = []
end_times = []

# Input form for entering timetable data
st.subheader("Add a Task")
task = st.text_input("Task Name")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

# Add a button to submit the task
if st.button("Add Task"):
    if task and start_time and end_time:
        tasks.append(task)
        start_times.append(start_time)
        end_times.append(end_time)
        st.success(f"Task '{task}' added from {start_time} to {end_time}")
    else:
        st.error("Please fill all the fields")

# Display the timetable as a table once tasks have been added
if tasks:
    st.subheader("Today's Timetable")
    timetable_df = pd.DataFrame({
        "Task": tasks,
        "Start Time": start_times,
        "End Time": end_times
    })
    st.table(timetable_df)

# Optionally, allow the user to reset the timetable
if st.button("Clear Timetable"):
    tasks.clear()
    start_times.clear()
    end_times.clear()
    st.success("Timetable cleared successfully")
