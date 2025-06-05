# Smart File Downloader (Streamlit App)

## Overview

This Python-based Streamlit app smartly downloads files by checking if a file has already been downloaded before, preventing duplicate downloads. It uses SHA-256 hashing of URLs and a lightweight JSON cache to save bandwidth and storage.

The app runs on Google Colab or locally, providing a simple web interface for real-time file downloads.

---

## Features

- Prevents duplicate downloads by hashing URLs and caching file paths.
- Saves downloaded files in a dedicated `downloads/` folder.
- User-friendly interface built with Streamlit.
- Supports real-time downloads from any valid file URL.
- Lightweight JSON cache for persistence between sessions.

---

## Installation & Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/<your-github-username>/smart-file-downloader.git
   cd smart-file-downloader
