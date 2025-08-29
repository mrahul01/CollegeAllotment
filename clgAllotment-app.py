import streamlit as st
import pandas as pd
import gdown

# Google Drive File ID
file_id = "1MZvqRk8-Ey_OLouqFLhQLaOtdSyVzkOQ"
download_url = f"https://drive.google.com/uc?id={file_id}"

# Download file locally (Streamlit Cloud safe)
output = "Allocation_Results.csv"
gdown.download(download_url, output, quiet=False)

# Load CSV
allocation_results = pd.read_csv(output)

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
