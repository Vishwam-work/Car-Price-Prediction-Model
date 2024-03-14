import base64
import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

from streamlit_lottie import st_lottie
st.set_page_config(page_title="Car Prediction",page_icon="img/icon.png",layout="wide")
import requests

model = pk.load(open('model.pkl','rb'))
with st.container():
    st.subheader("Hi My name is Vishwam Solanki  ")
    st.title("Car Price Pridiction App")
    st.write("Choose the Different Factors and Pidict the Price of the your dream car")



db = pd.read_csv('Cardetails.csv')
# get brand Name
def get_brand_name(car_name):
  car_name = car_name.split(' ')[0]
  return car_name.strip()

db['name'] = db['name'].apply(get_brand_name)

name=st.selectbox("Select Car Brand",db['name'].unique())
year=st.slider("Select Manufacture Year ",1994,2024)
km_driven=st.slider("Select Kilometer driven ",11,200000)

fuel=st.selectbox("Fuel Type",db['fuel'].unique())
seller_type=st.selectbox("Type of Seller",db['seller_type'].unique())
mileage=st.slider("Car Milage",10,40)
owner=st.selectbox("Type of Owner",db['owner'].unique())
engine=st.slider("Engine Capacity",700,5000)

max_power=st.slider("Max Power",0,200)
transmission=st.selectbox("Type of Transmission",db['transmission'].unique())
seats=st.slider("No od Seats",2,10)


if st.button("Predict"):
  input_data=pd.DataFrame([[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
  st.write(input_data)
  input_data['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5],inplace=True)
  input_data['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace=True)
  input_data['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace=True)
  input_data['transmission'].replace(['Manual',"Automatic"],[1,2],inplace=True)
  input_data['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai' ,'Toyota' ,'Ford' ,'Renault' ,'Mahindra',
 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi',
 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar','Land' ,'MG' ,'Volvo', 'Daewoo',
 'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu' ,'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)
  
  car_price = model.predict(input_data)

  st.write("Car Price is going to be "+str(int(car_price))+" INR.")
