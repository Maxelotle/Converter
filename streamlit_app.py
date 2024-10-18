import streamlit as st
import subprocess

# Führe den Befehl `pip list` aus und zeige die Ergebnisse in der App an
def get_installed_packages():
    result = subprocess.run(["pip", "list"], capture_output=True, text=True)
    return result.stdout

st.title("Liste der installierten Python-Pakete")
installed_packages = get_installed_packages()
st.text(installed_packages)
