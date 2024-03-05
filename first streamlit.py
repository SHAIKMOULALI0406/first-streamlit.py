import streamlit as st
st.title("First Streamlit project")
st.header("Going to create web page")
st.subheader("Going to create an job application web page")
st.text("write about yourself in 200 words")
st.subheader("job profile")
st.write('job description :')
st.info('Python developers can work in various industries, including web development, data science, artificial intelligence, machine learning, scientific computing, and more. They may also specialize in specific frameworks or libraries such as Django, Flask, NumPy, pandas, TensorFlow, or PyTorch, depending on the requirements of their projects. Overall, Python developers play a crucial role in building innovative and efficient software solutions across different domains.')
st.write('click on apply to apply for this role :')
st.button('Apply')

st.write("Select Gender :")
radio_button = st.radio('select:',('male','female','trans'))
if(radio_button == 'male'):
    st.write("you're a male")
elif(radio_button == 'female'):
    st.write("you're a female")
elif(radio_button == 'trans'):
    st.write("you're an trans")

st.subheader('Education')
st.selectbox("Education Qualification :",['B.sc','M.sc','MCA','B.tech','M.tech'])

st.subheader('Skills')
st.multiselect("Data science:",['python','data analyist','machine learning','deep learning','AI','NLP','DJANGO','pandas','Data visualization','matplot lib'])

st.subheader("Knowledge")
st.write('submit you are level in each skill')
st.write('python')
st.slider('select the level :',1,10,step = 1)


st.date_input('Date')
st.time_input('Time')

st.button('Submit')


