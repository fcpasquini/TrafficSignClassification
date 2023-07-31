import streamlit as st

class StreamlitApp:
    def __init__(self, port="", config="", page_title="Traffic Sign", page_icon=":car:", subheader="Traffic Sign Classification"):
        
        self.port = port
        self.config = config
        self.page_title = page_title
        self.page_icon = page_icon
        self.subheader = subheader

        self.create_main_pg()

    def create_iterative_image(self):
        # Create columns for each row in the matrix (9 rows in total)
        cols = st.columns(5)

        # Display images in a 9x5 matrix layout

        for i in range(5):  # 5 columns
            with cols[i]:
                index = i
                if index < 6:
                    st.image(f'./page_content/images/{index}.jpg', use_column_width=True)
                else:
                    pass

    def create_main_pg(self):
        # Create page
        st.set_page_config(page_title=self.page_title, page_icon=self.page_icon, layout = 'wide')
        
        with open('./page_content/welcome.txt') as file:
            page_content = file.read()

        #page_content = self.encapsulate_in_css(page_content, '/css/main.css')

        st.markdown(page_content, unsafe_allow_html=True)

        self.create_iterative_image()

if __name__ == "__main__":
    st_app = StreamlitApp()
