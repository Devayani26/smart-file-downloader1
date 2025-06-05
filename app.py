import streamlit as st
import requests
import os
import hashlib
import json

CACHE_FILE = "file_cache.json"
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)

def get_url_hash(url):
    return hashlib.sha256(url.encode()).hexdigest()

def download_file(url, cache):
    url_hash = get_url_hash(url)
    if url_hash in cache:
        return cache[url_hash], True

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        st.error(f"Download failed: {e}")
        return None, False

    filename = url.split("/")[-1]
    filepath = os.path.join(DOWNLOAD_FOLDER, filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    cache[url_hash] = filepath
    save_cache(cache)
    return filepath, False

def main():
    st.title("Smart File Downloader")

    cache = load_cache()

    url = st.text_input("Enter a file URL to download:")

    if st.button("Download"):
        if not url.strip():
            st.warning("Please enter a valid URL")
            return

        filepath, exists = download_file(url.strip(), cache)
        if filepath:
            if exists:
                st.success(f"File already downloaded: {filepath}")
            else:
                st.success(f"File downloaded successfully: {filepath}")
            st.write(f"**File location:** `{filepath}`")

if __name__ == "__main__":
    main()
