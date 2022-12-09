import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# made up data

chip_type = ["", "X1", "X2", "X3", "X4"]

chip_version = {
    "" : [""],
    "X1" : ["", "x1_1", "x1_2", "x1_3", "x1_4"], 
    "X2" : ["", "x2_1", "x2_2", "x2_3", "x2_4"],
    "X3" : ["", "x3_1", "x3_2", "x3_3", "x3_4"], 
    "X4" : ["", "x4_1", "x4_2", "x4_3", "x4_4"]
}


chip_data = {
    "chip_name" : ["X1", "X1", "X1", "X1", "X2", "X2", "X2", "X2", "X3", "X3", "X3", "X3", "X4", "X4", "X4", "X4"],
    "chip_version" : ["x1_1", "x1_2", "x1_3", "x1_4", "x2_1", "x2_2", "x2_3", "x2_4", "x3_1", "x3_2", "x3_3", "x3_4", "x4_1", "x4_2", "x4_3", "x4_4"], 
    "bandwidth" : [np.random.randint(1000,2000) for _ in range(16)]
}

chip_info = pd.DataFrame(chip_data)

operations = ["design-import", "etch", "bond", "drill", "test"]
chip_operation = {
    "Arm" : ["design-import", "etch", "bond", "drill", "test"],
    "Intel" : ["design-import", "drill", "test"],
    "Nvidia" : ["design-import", "etch", "bond", "drill", "test"]
    }

DATA_PATH = "web\data\cn.csv"

@st.cache
def load_data(nrows):
    df = pd.read_csv(DATA_PATH, nrows=nrows)
    return df

def main_page():
    st.set_page_config(page_title="Main Demo", page_icon="📈")
    st.sidebar.header("Main Demo")
    
    img = Image.open("web\img\chip_img.jpg")
    st.image(img)
    st.title("\"Title\"")

    st.markdown(
        """
        ## ***Who is this platform for***?
        ***With the help of Smart contract, High speed internet and Cloud manufacturing systems, we provide a platform where chip consumers (with ability of basic circuit design) can send their request of chip
        manufacturing and even make real-time scheduling over the machines of those plants.***
                
        """
    )
    
    # Load 300 rows of data into the dataframe.
    data = load_data(300)
    
    s3, s4 = st.columns((1,2))
    
    s3.header("***Our Plants***")
    s3.markdown("***Our plants are all over the country. We are able provide you with the most efficient solution!***")
    plant_img = Image.open("web\img\plant.jpg")
    s4.image(plant_img)
    st.markdown(
        """
        ### ***Are ALL OVER the country***!!

        """
    )
    st.map(data)
    s5, s6 = st.columns((2,1))
    machine_img = Image.open("web\img\machine.jpeg")
    s5.image(machine_img)
    
    s6.header("***Our Machines***")
    s6.markdown("***Customize your chipset with all the machines we provide!***")
    st.header("***Our Products***")

    s1, s2 = st.columns((1,1))

    selected_chip_type = s1.selectbox(
        'Chip name',
        chip_type)

    selected_chip_ver = s2.selectbox(
        'Chip version',
        chip_version[selected_chip_type])

    if selected_chip_type == "":
        st.write(chip_info)
    else:
        if selected_chip_ver == "":
            st.write(chip_info.loc[chip_info['chip_name'] == selected_chip_type])
        else:
            st.write(chip_info.loc[(chip_info['chip_name'] == selected_chip_type) & (chip_info['chip_version'] == selected_chip_ver)])
            

if __name__ == "__main__":
    main_page()