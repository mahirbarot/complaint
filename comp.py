import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file from Firebase Console
cred = credentials.Certificate(r"serviceAccount.json")

# Initialize the Firebase app
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://smartdustbin-nuv-default-rtdb.firebaseio.com/'
# })

# Reference to the root of the database
ref = db.reference('/complaints')

st.set_page_config(
        page_title="mini project",
        page_icon="house_buildings",
        layout='centered',
    )



def main():
    st.title('Firebase Submission')

    # Input fields
    area = st.text_input('Area')
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
            'subject': subject
        }
        ref.child('complaints').child(area).child(dustbin_id).push(submission)
        st.success('Data submitted successfully!')

if __name__ == '__main__':
    main()
