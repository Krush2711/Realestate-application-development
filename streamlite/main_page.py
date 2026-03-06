import streamlit as st 
import pickle
import numpy as np 
import pandas as pd 


with open('../pipeline.pkl', 'rb') as f :
    pipeline= pickle.load(f)

with open('../df.pkl', 'rb') as fd:
    df = pickle.load(fd)   

list = sorted(df['sector'].unique().tolist())

st.title("Real Estate Price Predictor !!") 
st.header("Enter Property Details of Gurgaon") 

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    property_type = st.selectbox('Property Type', ['House','Flat']).lower()
with col2:
    sector = st.selectbox('Sector', list)
    
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    bedRoom =float(st.slider("Number of bedroom you are looking for : ", 1, 10))
with col2:
    bathroom =float(st.slider("Number of bathroom you are looking for : ", 1, 10))


st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    balcony = st.selectbox('Number of balcony you are looking for :', ['1', '2' , '3', '3+'])
with col2:
   agePossession = st.selectbox('Age of property :', ['New Property', 'Relatively New', 'Old Property', 'Moderately Old', 'Under Construction'])

st.markdown("---")
built_up_area =float(st.number_input('Area in Sq. ft. you are willing to buy :'))

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    store_room =float( st.checkbox("Want store room ? "))
with col2:
   servant_room =float( st.checkbox("Want servent room ? "))

st.markdown("---")
col1, col2 , col3 = st.columns(3)
with col1:
    luxury_category = st.selectbox('Select luxury type you want : ', ['Low', 'High', 'Medium'])   
with col2:
    furnishing_type = st.selectbox('Select furnishing type you want : ', ['unfurnished', 'semifurnished', 'furnished'])
with col3:
    floor_category = st.selectbox('Select floor you want : ', ['Low Floor', 'Mid Floor', 'High Floor'])
    
st.markdown("---")

data = [[property_type, sector, bedRoom, bathroom, balcony, agePossession, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

one_df = pd.DataFrame(data, columns=columns)

st.write(one_df)



if st.button("Predict Price"):
    price =np.expm1(pipeline.predict(one_df))[0]

    st.success(
    f"💰 Estimated Price Range: ₹{price-0.10:.2f} Cr — ₹{price+0.10:.2f} Cr"
)