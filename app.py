import streamlit as st
from multiapp import MultiApp
from apps import Maps, Top5 # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Maps", Maps.app)
app.add_app("Dataframes", Top5.app)

# The main app
app.run()