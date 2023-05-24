import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

current_datetime = datetime.now()

# Extract date and time components
current_date = str(current_datetime.date())
current_time = str(current_datetime.time())
# Fetch the service account key JSON file from Firebase Console
cred = credentials.Certificate(r"serviceAccount.json")

# # Initialize the Firebase app
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://smartdustbin-nuv-default-rtdb.firebaseio.com/'
# })

# Reference to the root of the database
ref = db.reference('/complaints')

st.set_page_config(
        page_title="complaint portal mini project",
        page_icon="house_buildings",
        layout='centered',
    )



def main():
    st.title('VMC complaint Submission')

    # Input fields
    area = st.text_input('Area')
    area=area.lower()
    area=area.capitalize()
    dustbin_id = st.text_input('Dustbin ID')
    pincode = st.text_input('Pincode')
    subject = st.text_input('Subject')

    # Submit button
    if st.button('Submit'):
        # Push the data to Firebase
        submission = {
            'area':area,
            'dustbin_id': dustbin_id,
            'pincode': pincode,
            'subject': subject,
            'date':current_date,
            'time': current_time
        }
        ref.child('complaints').child(area).child(dustbin_id).set(submission)
        st.success('Data submitted successfully!')

if __name__ == '__main__':
    main()



