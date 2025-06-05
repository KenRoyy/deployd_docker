import streamlit as st
import pandas as pd
import altair as alt
import os
import streamlit as st
from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group





def main():
    page = page_group("p")
    page.show()


if __name__ == "__main__":
    st.set_page_config(page_title="Dashborad Fianciero", page_icon="🎈", layout="wide")
    main()