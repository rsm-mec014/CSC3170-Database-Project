import streamlit as st
from streamlit_option_menu import option_menu as om
from log_page import *

selected = om("CUHK CHIP DATA CENTER INTERFACE", 
                ["LOG IN", 
                'SIGN UP'], 
            menu_icon =  "None",
            icons=['house', 'text-indent-right'], 
            orientation='horizontal',
            default_index=1)
if selected == "LOG IN":
    log_in_page()
elif selected =="SIGN UP":
    sign_up_page()
