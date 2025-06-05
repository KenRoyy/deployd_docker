import streamlit as st
import pandas as pd
import altair as alt
import os
import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report





def main():
    df = pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")
    pr = df.profile_report()
    st_profile_report(pr)


if __name__ == "__main__":
    st.set_page_config(page_title="Dashborad Fianciero", page_icon="🎈", layout="wide")
    main()