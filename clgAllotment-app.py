import streamlit as st
import pandas as pd
import gdown

# Google Drive File ID
file_id = "1MZvqRk8-Ey_OLouqFLhQLaOtdSyVzkOQ"
download_url = f"https://drive.google.com/uc?id={file_id}"

# Download file
output = "Allocation_Results.csv"
gdown.download(download_url, output, quiet=False)

# Load CSV
allocation_results = pd.read_csv(output)

st.title("🎓 Seat Allocation Results Dashboard")


# --- Student lookup ---
unique_id = st.text_input("Enter your UniqueID:")
st.write(unique_id)
if unique_id:
    # Convert both sides to string to avoid type mismatch
    allocation_results["UniqueID"] = allocation_results["UniqueID"].astype(str)
    student_result = allocation_results[allocation_results["UniqueID"] == str(unique_id).strip()]

    if not student_result.empty:
        st.success("✅ Seat allocated!")
        st.write("### Student Details")
        st.dataframe(student_result[[
            "UniqueID", "Name", "Gender", "Caste", "Rank", 
            "CollegeID", "Institution", "PrefNumber"
        ]].reset_index(drop=True))
    else:
        st.error("❌ No seat allocated for this UniqueID.")
