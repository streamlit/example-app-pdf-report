import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generator")

st.write(
    "This app shows you how you can use Streamlit make a PDF generator app in just a few lines of code!"
)


st.write("Here's the template we'll be using:")

st.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


st.write("### Fill in the data...")
st.write("")
form = st.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit 🎈", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 5, 2)
submit = form.form_submit_button("Generate PDF")


if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/5",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    st.write("### And here's the diploma!")
    st.write(html, unsafe_allow_html=True)
    st.write("")
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )