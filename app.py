import requests
import streamlit as st
from datetime import datetime
import pandas as pd
import time
# from time import sleep


st.title("FRAUD DETECTION")
 
st.subheader("Enter the details of the transaction")

# args = ["name", "amount", "location", "time", "category", "merchant", "product"]
timestamp = datetime.now() #datetime.timestamp( datetime.now() )
name        = st.text_input("Name"      )#,  "Enter your Name"    )
amount      = st.text_input("Amount"    )#,  "Enter the Amount"   )
location    = st.text_input("Location"  )#,  "Enter your Location")
category    = st.text_input("Category"  )#,  "Enter the Category" )
merchant    = st.text_input("Merchant"  )#,  "Enter your Merchant")
prod        = st.text_input("Product"   )#,  "Enter The product"  )

if(st.button('Submit')):
    with st.spinner('Wait for it...'):
        time.sleep(0.5)
        data = {
            "name"      :   str(name        ),
            "amount"    :   int(amount      ),
            "location"  :   str(location    ),
            "time"      :   str(timestamp   ),
            "category"  :   str(category    ),
            "merchant"  :   str(merchant    ),
            "product"   :   str(prod        ) 
        }

        # api call
#         url = "http://127.0.0.1:5000/"
        url = "https://ftbc.herokuapp.com/"
        print(data)
        response = requests.get(url + "demo", data)
        response = response.json()
        status = response['status']
        print("satuss:", status)
        if status == 101:
            response = response['data']
            if response['fraud'] == 1:
                fraud = "-Decline"
                st.error("Fraud Detected")
            else:
                fraud = "+Accepted"
                st.success("Safe Transaction")
            # st.metric(label="Fraud Score", value=response['fraud_score'], delta=fraud)
            st.progress( response['fraud_score'] )
            response_df = pd.DataFrame(response.items(), columns=['Attribute', 'Value'])
            st.table(response_df)
            st.markdown("Response in JSON Format:")
            st.json(response)
        else:
            st.error("ERROR")
