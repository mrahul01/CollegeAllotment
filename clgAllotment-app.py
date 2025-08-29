import streamlit as st
import pandas as pd

# Load allocation results
allocation_results = pd.read_csv("Allocation_Results.csv")

# Optional: Load not allocated students if needed
# not_allocated = pd.read_csv("Not_Allocated.csv")

st.title("🎓 Seat Allocation Results Dashboard")

# Input: Student UniqueID
unique_id = st.text_input("Enter your UniqueID:")

if unique_id:
    student_result = allocation_results[allocation_results["UniqueID"] == unique_id]

    if not student_result.empty:
        st.success("✅ Seat allocated!")
        st.write("### Student Details")
        st.dataframe(student_result[[
            "UniqueID", "Name", "Gender", "Caste", "Rank", 
            "CollegeID", "Institution", "PrefNumber"
        ]].reset_index(drop=True))
    else:
        st.error("❌ No seat allocated for this UniqueID.")

