import streamlit as st
import sys

sys.path.append('Streamlit')

def create_iterative_image():
    # Create columns for each row in the matrix (9 rows in total)
    cols = st.columns(5)

    # Display images in a 9x5 matrix layout

    for j in range(9):  # 9 rows
        for i in range(5):  # 5 columns
            with cols[i]:
                index = i + j * 5
                if index < 43:
                    st.image(f'./page_content/images/{index}.jpg', use_column_width=True)
                else:
                    pass

def create_main_pg():
    # Create page
    st.set_page_config(page_title='Traffic Signs Classes Examples', page_icon=':car:', layout = 'wide')
    
    with open('./page_content/02_Signs_Classes.txt') as file:
        page_content = file.read()

    st.markdown(page_content, unsafe_allow_html=True)

    create_iterative_image()


create_main_pg()


