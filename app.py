import streamlit as st
import pandas as pd
import requests
import base64

REPO = "mikelfc12/scc_test"
FILE_PATH = "test_data_conn.csv"
BRANCH = "main"

TOKEN = st.secrets["GITHUB_TOKEN"]

st.title("CSV Data Entry")

# GitHub file URL
url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"

headers = {
    "Authorization": f"token {TOKEN}"
}

# Get existing file
response = requests.get(url, headers=headers).json()

content = base64.b64decode(response["content"]).decode("utf-8")

df = pd.read_csv(pd.io.common.StringIO(content))

st.subheader("Current Data")
st.dataframe(df)

# User input
code = st.number_input("Code", step=1)
text = st.text_input("Text")

if st.button("Add Row"):

    df.loc[len(df)] = [code, text]

    new_content = df.to_csv(index=False)

    encoded = base64.b64encode(new_content.encode()).decode()

    data = {
        "message": "update csv via streamlit",
        "content": encoded,
        "sha": response["sha"],
        "branch": BRANCH
    }

    r = requests.put(url, headers=headers, json=data)

    if r.status_code == 200:
        st.success("Row added and saved to GitHub!")