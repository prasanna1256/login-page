import streamlit as st
import sqlite3 as aq
conn = aq.connect("example.db")
c = conn.cursor()
def create_user(usename,password):

    c.execute('''CREATE TABLE IF NOT EXISTS mydata (id INTEGER PRIMARY KEY,username TEXT,password TEXT);''')
    conn.commit()
def add_user(username,password):
    c.execute('''INSERT INTO mydata(username,password) VALUES (?,?);''', (username,password))
    conn.commit()
def authenticate(username,password):
    c.execute('''SELECT * FROM mydata WHERE username = ? AND password = ?;''', (username, password))
    user =c.fetchall()
    if user:
        return True
    else:
        return False
def menu():
    menu=['home','sign up','login']
    choice=st.sidebar.selectbox("menu",menu)
    if choice=="home":
        st.subheader("this is home page")
    elif choice=="sign up":
        st.subheader("SignUp")

        new_username=st.sidebar.text_input("username")
        new_password=st.sidebar.text_input("password",type="password")

        create_user(new_username,new_password)
        if st.sidebar.button("sign up"):
            
            add_user(new_username,new_password)
            st.sidebar.success("you are registered successfully")
            st.sidebar.info("goto to the login menu in menu")
    elif choice == "login":
        st.subheader("Login")
        username = st.sidebar.text_input("username")
        password = st.sidebar.text_input("password", type="password")
        if st.sidebar.button("login"):
            user1 = authenticate(username,password)
            if user1:
                st.sidebar.success("Logged in as: " + username)
            else:
                st.sidebar.error("Authentication failed. Please check your username and password.")


menu()