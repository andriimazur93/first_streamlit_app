import streamlit
import pandas as pd


streamlit.title('Some fancy streamlit app')

# read data
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# display the table on the page
streamlit.dataframe(fruits_to_show)


streamlit.title('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
