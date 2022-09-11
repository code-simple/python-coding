# import libraries
import pandas as pd
import sqlite3

# create db connection
cnn = sqlite3.connect('world_cup.db')
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///world_cup.db')

# create a variable to store the url
w_cup_url = 'https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals'

# create variable to store list of dataframes in the website
w_cup_df = pd.read_html(w_cup_url)

# create variable to store countries url
countries_url='https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

# create a variable to store list of dataframes in country site
countries_df = pd.read_html(countries_url)