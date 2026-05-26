# Multiclient Monitor

<p align="center">
  <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width="220">
</p>

<p align="center">
  <b>Multithreaded Client-Server File Management & Monitoring System</b>
</p>

---

## Overview

**Multiclient Monitor** is a Python-based multithreaded client-server application designed for efficient file management and real-time server monitoring.

The system allows multiple clients to simultaneously:
- Upload files
- Read files
- Delete files
- View server statistics
- Monitor network performance

The project combines **Socket Programming**, **Streamlit UI**, and **System Monitoring Tools** to provide a scalable and interactive monitoring dashboard.

The project is based on the CN-IOT synopsis and implementation files.
---

## Features

Multithreaded Client-Server Architecture  
Real-Time File Upload & Management  
Interactive Streamlit Dashboard  
CPU, RAM & Disk Monitoring  
Internet Speed & Ping Testing  
File Read/Delete Operations  
TCP/IP Socket Communication  
Multiple Client Support  

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| Streamlit | Frontend Dashboard |
| Socket Programming | Client-Server Communication |
| psutil | System Monitoring |
| speedtest | Network Speed Testing |
| Matplotlib | Graph Visualization |
| PIL | Image Handling |

---

## Project Structure

```text
MulticlientMonitor/
│
├── app.py
├── server.py
├── client_module.py
├── uploads/
├── server_data/
├── requirements.txt
└── README.md
```

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/ahsansabeeh910/MulticlientMonitor.git
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Start Server

```bash
python server.py
```

---

### Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

---

## Functionalities

### Upload File
- Upload `.txt`, `.pdf`, `.jpg`, `.png` files
- Files stored on server

### View Files
- Browse uploaded files dynamically

### Read File
- Read text files directly in dashboard

### Delete File
- Remove unnecessary files from server

### Server Stats
- CPU Usage
- Memory Usage
- Disk Usage
- Live graphical monitoring

### Network Stats
- Download Speed
- Upload Speed
- Ping Testing

---

## Client-Server Communication

The application uses:
- TCP/IP Socket Programming
- Multithreading for concurrent client handling

Supported Commands:
- `LIST`
- `UPLOAD`
- `READ`
- `DELETE`
- `STATS`
- `HELP`
- `LOGOUT`

Server implementation uses threaded socket handling for multiple clients. 

---

## Monitoring Dashboard

The Streamlit interface provides:
- Interactive sidebar navigation
- Real-time server statistics
- Network diagnostics
- File management controls

Implemented using Streamlit and psutil libraries. 

---

## System Architecture

```text
Client (Streamlit UI)
        │
        ▼
TCP/IP Socket Communication
        │
        ▼
Python Multithreaded Server
        │
        ├── File Operations
        ├── System Monitoring
        └── Network Diagnostics
```

---

## requirements.txt

```txt
streamlit
streamlit-autorefresh
pillow
matplotlib
psutil
speedtest-cli
pandas
numpy
```

---



## 👨‍💻 Team Members

- Sabeeh Ahsan
- Tanmay Butta
- Aryan Khanna

---

