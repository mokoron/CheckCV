import streamlit as st
import Scoring


st.set_page_config(page_title="Check if your CV fits the desirable position", layout="centered", page_icon="📝",)
st.header('Check if your CV fits the desirable position :sunglasses:')

#st.title("📝 Check if your CV fits the desirable position")

model = Scoring.load_model()
with st.container():
    with st.form(key='cv_jobposition'):

        uploaded_file = st.file_uploader("Choose a CV file", type=['pdf', 'docx'])
        #cv_file = "none"
        st.write(uploaded_file.name[0][-4:])
        st.write(uploaded_file.name[0][:-4])
        job_txt = st.text_area('Enter the job description here', height=300, value="Superhero Performer for Birthday Parties and Events. \nMust be energetic and love to work with kids. \nTraining provided. \nMost events include tips and travel. \nMust be have reliable transportation. \nBackground check required. \nExcellent pay. Must be 18+ Most events will be on the weekend during the day time.")

        submitted = st.form_submit_button("Check")
        if submitted:
            with st.spinner('Calculating...'):
                #time.sleep(5)
                #st.write("run script ")
                if uploaded_file is not None:
                    if uploaded_file.name[0][-4:] == 'docx':
                        cv_file = Scoring.docxread(uploaded_file)
                        st.write("docx")
                    else:
                        #cv_file = Scoring.pdfread(uploaded_file)
                        st.write("PDF")
                else: st.write("Upload a CV to score")

                score = Scoring.similar(Scoring.embedding(cv_file), Scoring.embedding(job_txt))[0]
            st.success('Similarity score is:', score)

#st.write(cv_file)
st.markdown("[mokoron.com](http://www.mokoron.com)")