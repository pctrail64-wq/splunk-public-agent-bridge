# @title 🛡️ Splunk Autonomous SOC Analyst {display-mode: "form"}

import os, sys, json, time, threading
from datetime import datetime
from google.colab import output
from IPython.display import HTML, display
import subprocess

try:
    import splunklib.client as client
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "splunk-sdk", "--quiet"])
    import splunklib.client as client

# Authoritative Config
SPLUNK_CFG = {'host': 'prd-p-2xnsr.splunkcloud.com', 'port': 8089, 'user': 'sc_admin', 'pass': 'zvg5y4x5uiitj9y0A'}
AGENT_LOGS = []

def run_triage():
    try:
        service = client.connect(**SPLUNK_CFG, autologin=True)
        AGENT_LOGS.append({'t': datetime.now().isoformat(), 'm': 'Connected to Splunk', 'v': 'sys'})
    except Exception as e:
        AGENT_LOGS.append({'t': datetime.now().isoformat(), 'm': str(e), 'v': 'verdict'})

# [Dashboard UI and Logic Omitted for brevity in file writing, but full code is in the Colab cell]