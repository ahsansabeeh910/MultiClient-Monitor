import streamlit as st
from streamlit_autorefresh import st_autorefresh
from PIL import Image
import matplotlib.pyplot as plt
import os
import socket
import speedtest  # Correct import
import psutil
import time

# Set page configuration
st.set_page_config(
    page_title="CN File Management",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    body {
        background-color: #1e272e;
    }
    .main {
        background-color: #1e272e;
        color: white;
    }
    .st-emotion-cache-1v0mbdj, .st-emotion-cache-1c7y2kd, .stMarkdown, .stText {
        color: white !important;
    }
    .stTextArea textarea {
        background-color: #2f3640 !important;
        color: white !important;
    }
    .stSelectbox div, .stButton button {
        background-color: #4cd137 !important;
        color: black !important;
        font-weight: bold;
    }
    .sidebar .sidebar-content {
        background-color: #2f3640;
    }
    .css-1d391kg, .css-1v0mbdj h1 {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎛️ Choose an Action")
menu = st.sidebar.radio("",
    ["🔴 Upload File", "📁 View Files", "📖 Read File", "🗑️ Delete File", "📊 Server Stats", "📶 Network Stats", "💬 Help"])

# Constants
SERVER_IP = "127.0.0.1"
PORT = 5001
ADDR = (SERVER_IP, PORT)
BUFFER_SIZE = 1024
UPLOAD_DIR = "uploads"

# Create uploads directory if not exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Upload File
if menu == "🔴 Upload File":
    st.markdown("## 📤 Upload Your File to Server")
    uploaded_file = st.file_uploader(
    "Choose a file (txt, pdf, jpg, png)",
    type=["txt", "pdf", "jpg", "jpeg", "png"]
)


    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File `{uploaded_file.name}` uploaded successfully!")

# View Files
elif menu == "📁 View Files":
    st.markdown("## 📁 Uploaded Files on Server")
    files = os.listdir(UPLOAD_DIR)
    if files:
        for file in files:
            st.markdown(f"- {file}")
    else:
        st.info("No files found.")

# Read File
elif menu == "📖 Read File":
    st.markdown("## 📖 Read Uploaded File")
    files = os.listdir(UPLOAD_DIR)
    if files:
        selected_file = st.selectbox("Choose a file", files)
        file_path = os.path.join(UPLOAD_DIR, selected_file)

        file_ext = selected_file.split('.')[-1].lower()

        if file_ext == 'txt':
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()
                st.text_area("File Content", file_content, height=300)

                st.download_button(
                    label="📥 Download File",
                    data=file_content,
                    file_name=selected_file,
                    mime="text/plain"
                )

        elif file_ext in ['jpg', 'jpeg', 'png']:
            image = Image.open(file_path)
            st.image(image, caption=selected_file, use_column_width=True)

            with open(file_path, "rb") as img_file:
                img_bytes = img_file.read()

            st.download_button(
                label="📥 Download Image",
                data=img_bytes,
                file_name=selected_file,
                mime="image/png" if file_ext == 'png' else "image/jpeg"
            )

        elif file_ext == 'pdf':
            st.info("📖 PDF preview not available yet. Download it below.")
            with open(file_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()

            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name=selected_file,
                mime="application/pdf"
            )

        else:
            st.warning("Unsupported file format.")
    else:
        st.warning("No file available to read.")

# Delete File
elif menu == "🗑️ Delete File":
    st.markdown("## 🗑️ Delete a File")
    files = os.listdir(UPLOAD_DIR)
    if files:
        file_to_delete = st.selectbox("Select a file to delete", files)
        if st.button("Delete"):
            os.remove(os.path.join(UPLOAD_DIR, file_to_delete))
            st.success(f"File `{file_to_delete}` deleted successfully.")
    else:
        st.warning("No files to delete.")



# Server Stats
elif menu == "📊 Server Stats":
    st.markdown("## 📊 Real-Time Server Stats with Live Graphs")

    st_autorefresh(interval=5000, limit=None, key="serverstats")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    st.metric("🧠 CPU Usage (%)", f"{cpu}%")
    st.metric("🗃️ Memory Usage (%)", f"{memory}%")
    st.metric("💾 Disk Usage (%)", f"{disk}%")

    # Plotting
    fig, ax = plt.subplots()
    labels = ['CPU', 'Memory', 'Disk']
    usage = [cpu, memory, disk]
    colors = ['#03dac6', '#ff0266', '#ffab00']

    ax.bar(labels, usage, color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel('Usage (%)')
    ax.set_title('Resource Usage')

    st.pyplot(fig)

# Network Stats
elif menu == "📶 Network Stats":
    st.markdown("## 📶 Real-Time Network Speed Test")
    if st.button("Start Speed Test"):
        with st.spinner('Running speed test... please wait ⏳'):
            test = speedtest.Speedtest()
            download = test.download() / 1_000_000
            upload = test.upload() / 1_000_000
            ping = test.results.ping

        col1, col2, col3 = st.columns(3)
        col1.metric("⬇️ Download Speed", f"{download:.2f} Mbps")
        col2.metric("⬆️ Upload Speed", f"{upload:.2f} Mbps")
        col3.metric("📡 Ping", f"{ping:.2f} ms")


# Help Section
elif menu == "💬 Help":
    st.markdown("## ℹ️ How to Use This App")
    st.markdown("""
    - **Upload File**: Send a `.txt` file to the server.
    - **View Files**: Browse uploaded files.
    - **Read File**: Open any text file to read its contents.
    - **Delete File**: Remove unwanted files.
    - **Server Stats**: View CPU, RAM, and Disk usage.
    - **Network Stats**: Test current internet speed and ping.
    """)
