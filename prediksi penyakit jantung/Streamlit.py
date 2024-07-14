import pickle 
import streamlit as st

model = pickle.load(open('heart.sav', 'rb'))

st.set_page_config(
page_title="Prediksi Sakit Jantung",
page_icon="",
)

st.markdown(
"""
# Prediksi Penyakit Jantung
  Prediksi Penyakit jantung bisa dilakukan dengan menginputkan beberapan data dibawah ini diantaranya :
"""
)

col1, col2 = st.columns(2)

with col1 :
  Age = st.number_input("Masukan Umur", 20,100,20)

with col2 :
  Sex = st.selectbox("Jenis kelamin", options=('  ' , 'Laki-Laki', 'Perempuan'))

with col1 :
  CPT = st.selectbox("Masukan Jenis Sakit dada", options=('  ', 'ATA: Atypical Angina', 'NAP: Non-Anginal Pain', 'ASY: Asymptomatic'))

with col2 :
  RestingBp = st.number_input("Masukan Jumlah Tekanan darah mmHg ", 0,200,0)

with col1 :
  choles = st.number_input(" Masukan Data Kolesterol serum ", 0, 603, 0)

with col2 :
  Fasting = st.selectbox("Masukan Kadar gula darah", options=(' ','YES' , 'NO'))

with col1 :
  RestingECG = st.selectbox("Masukan Data Electrocardiogram (ECG) istirahat", options=(' ' ,'Normal','Abnormality','LVH'))

with col2 :
  MaxHR = st.number_input("Masukan Denyut jantung maksimum", 60, 202,60)

Exercise = st.selectbox("Masukan Angina akibat olahraga", options=('  ' , 'YES' , 'NO'))

oldpeak = st.number_input("Masukan Data Oldpeak / Aktivitas Jantung Selama depresi fisik atau tes olahraga", -2.6, 6.2, 0.0)

ST_Slope = st.selectbox("Masukan Data Slope Perubahan bentuk segmen ST", options=('  ' , 'Up: upsloping' , 'Flat: flat', 'Down: downsloping'))


if (Sex == 'Perempuan'):
    Sex=0
else:
    Sex=1

if (CPT == 'ATA: Atypical Angina'):
    CPT=1
elif(CPT == 'NAP: Non-Anginal Pain'):
    CPT=2
else:
    CPT=0

if (Fasting == 'YES'):
    Fasting=1
else:
    Fasting=0

if (RestingECG == 'Normal'):
    RestingECG=1
elif(RestingECG == 'Abnormality'):
    RestingECG=2
else:
    RestingECG=0

if (Exercise == 'YES'):
    Exercise=1
else:
    Exercise=0

if (ST_Slope == 'Up: upsloping'):
    ST_Slope=2
elif(ST_Slope == 'Flat: flat'):
    ST_Slope=1
else:
    ST_Slope=0


if st.button("Prediksi penyakit sakit jantung"):
    heart_disease_predict = model.predict([[Age,Sex,CPT,RestingBp,choles,Fasting,RestingECG,MaxHR,Exercise,oldpeak,ST_Slope]])
    if(heart_disease_predict[0]==0):
        st.success("Pasien tidak terindikasi Penyakit jantung")
    else :
        st.warning("Pasien terindikasi Penyakit jantung")


