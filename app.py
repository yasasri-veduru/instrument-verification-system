import streamlit as st
from database import create_database, add_application, get_applications, approve_application
from certificate import generate_certificate_hash, generate_qr_code

create_database()

st.title("SIH26036 - Verification System")
st.write("Submit a new verification application.")

with st.form("application_form"):

    applicant_name = st.text_input("Applicant Name")
    instrument_type = st.text_input("Instrument Type")
    instrument_id = st.text_input("Instrument ID")
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        if applicant_name and instrument_type and instrument_id:
            add_application(
                applicant_name,
                instrument_type,
                instrument_id
            )
            st.success("Application submitted successfully!")
        else:
            st.error("Please fill in all fields.")

st.subheader("Officer Dashboard")

applications = get_applications()
for application in applications:

    application_id = application[0]
    applicant_name = application[1]
    instrument_type = application[2]
    instrument_id = application[3]
    status = application[4]
    st.write(
        f"Application ID: {application_id} | "
        f"Applicant: {applicant_name} | "
        f"Instrument: {instrument_type} | "
        f"Instrument ID: {instrument_id} | "
        f"Status: {status}"
    )

    if status == "Pending":
        if st.button("Approve", key=f"approve_{application_id}"):
            approve_application(application_id)
            st.success(f"Application {application_id} approved!")
            st.rerun()
    if status == "Approved":
        if st.button(
            "Generate Certificate",
            key=f"certificate_{application_id}"
        ):

            certificate_hash = generate_certificate_hash(
                application_id,
                applicant_name,
                instrument_type,
                instrument_id
            )
            qr_file = generate_qr_code(certificate_hash)

            st.success("Certificate generated!")
            st.write("Certificate Hash:")
            st.code(certificate_hash) 
            st.write("QR Code:")
            st.image(qr_file)           