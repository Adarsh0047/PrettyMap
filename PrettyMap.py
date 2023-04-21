import streamlit as st
from prettymaps import plot
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from PIL import Image
import os
st.title("Pretty Maps Application")

st.sidebar.title("Input")
form = st.sidebar.form("my_form")
place = form.text_area("Enter the place that you want to see the map")
circle = form.checkbox("Circle")
rad = form.slider("Radius", 1000, 10000, 2000, 100)
p_name = form.text_input("Title of figure:")
submit = form.form_submit_button("Submit")
if submit:
    try:
        with st.spinner(f'Building a map of {p_name}.. Hold On...'):
                fig, ax = plt.subplots(figsize = (13, 13))
                figure = plot(
                    place,
                    circle = circle,
                    radius = rad,
                    ax=ax
                )
                fig.patch.set_facecolor('#F2F4CB')
                ax.set_title(
                p_name,
                fontproperties = FontProperties(
                
                    size = 50
                )
                )
                plt.savefig(f"{p_name}.jpeg", dpi=600)
                # figure.savefig(f"{p_name}.jpg")
                figure = Image.open(f"{p_name}.jpeg")
                st.image(figure)
                with open(f"{p_name}.jpeg", "rb") as file:
                    st.download_button("Download Map",
                                data=file,
                                file_name=f"{p_name}.jpeg",
                                mime="image/png")
                files = os.listdir(os.curdir)
                for item in files:
                    if item.endswith(".jpeg"):
                        os.remove(os.path.join(os.curdir, item))
    except:
        st.warning("The place that you typed does not exist or the format is wrong")
else:
    st.info("Enter a place")
