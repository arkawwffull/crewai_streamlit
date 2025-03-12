'''import streamlit as st
from crew import SrsToSdd
import os
from datetime import datetime

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Title of the app
st.title("SRS to SDD Automation Tool")
st.markdown("""
Upload your SRS document (`.docx` or `.txt`), and this tool will generate an SDD document (`sdd1.md`) for you to download.
""")

# File uploader
uploaded_file = st.file_uploader("Upload SRS Document", type=["txt", "docx"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_file_path = f"temp_{datetime.now().strftime('%Y%m%d%H%M%S')}.{uploaded_file.name.split('.')[-1]}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Button to trigger the SDD generation process
    if st.button("Generate SDD"):
        try:
            # Initialize the SrsToSdd crew with the uploaded file path
            crew_instance = SrsToSdd(file_path=temp_file_path)

            # Run the CrewAI workflow
            st.info("Generating SDD... Please wait.")
            crew_instance.crew().kickoff()

            # Path to the generated SDD file
            sdd_file_path = "sdd1.md"

            # Check if the file was generated
            if os.path.exists(sdd_file_path):
                st.success("SDD generated successfully!")

                # Provide a download button for the SDD file
                with open(sdd_file_path, "r", encoding="utf-8") as file:
                    sdd_content = file.read()
                
                st.download_button(
                    label="Download SDD",
                    data=sdd_content,
                    file_name="sdd1.md",
                    mime="text/markdown"
                )
            else:
                st.error("Failed to generate SDD. Please check the logs.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)'''



import streamlit as st
from crew import SrsToSdd
import os
from datetime import datetime

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Function to add custom CSS
def add_custom_css():
    st.markdown("""
    <style>
        /* Style for the file uploader */
        .stFileUploader > div > button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        /* Hover effect for the file uploader button */
        .stFileUploader > div > button:hover {
            background-color: #45a049; /* Darker green on hover */
        }

        /* Style for the "Generate SDD" button */
        .stButton > button {
            background-color: #008CBA; /* Blue background */
            color: white; /* White text */
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        /* Hover effect for the "Generate SDD" button */
        .stButton > button:hover {
            background-color: #007A9E; /* Darker blue on hover */
        }

        /* Style for the sidebar */
        .css-1d391kg {
            background-color: #f4f4f4; /* Light gray background */
            padding: 20px;
            border-radius: 10px;
        }

        /* Style for success/error messages */
        .stSuccess {
            color: #28a745; /* Green text for success */
            font-size: 18px;
        }

        .stError {
            color: #dc3545; /* Red text for errors */
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Apply custom CSS
add_custom_css()

# Main section of the app
st.title("🚀 SRS to SDD Automation Tool")
st.markdown("""
Welcome to the **SRS to SDD Automation Tool**!  
Upload your SRS document (`.docx` or `.txt`), and this tool will automatically generate an SDD document (`sdd1.md`) for you to download.  
Use the sidebar on the left to upload your file and generate the SDD.
""")

# Sidebar for file upload and button
with st.sidebar:
    st.header("📝 Upload and Generate")
    uploaded_file = st.file_uploader("Upload SRS Document", type=["txt", "docx"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_file_path = f"temp_{datetime.now().strftime('%Y%m%d%H%M%S')}.{uploaded_file.name.split('.')[-1]}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Button to trigger the SDD generation process
    if st.button("Generate SDD", key="generate_button"):
        try:
            # Initialize the SrsToSdd crew with the uploaded file path
            crew_instance = SrsToSdd(file_path=temp_file_path)

            # Run the CrewAI workflow
            st.info("Generating SDD... Please wait.")
            crew_instance.crew().kickoff()

            # Path to the generated SDD file
            sdd_file_path = "sdd1.md"

            # Check if the file was generated
            if os.path.exists(sdd_file_path):
                st.success("SDD generated successfully!")

                # Provide a download button for the SDD file
                with open(sdd_file_path, "r", encoding="utf-8") as file:
                    sdd_content = file.read()
                
                st.download_button(
                    label="Download SDD",
                    data=sdd_content,
                    file_name="sdd1.md",
                    mime="text/markdown"
                )
            else:
                st.error("Failed to generate SDD. Please check the logs.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)