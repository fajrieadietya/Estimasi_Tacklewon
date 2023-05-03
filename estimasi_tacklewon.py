import pickle
import streamlit as st

model = pickle.load(open('estimasi_tacklewon.sav', 'rb'))

st.title('Estimasi Tackle yang dimenangi Defender di Laliga')

balls_recoverd = st.number_input('Input Jumlah Merebut Bola')
t_won = st.number_input('Input jumlah Tekel berhasil')
t_lost = st.number_input('Input jumlah Tekel Gagal')
clearance_attempted = st.number_input('Input Jumlah Sapuan Bola')
match_played = st.number_input('Input Jumlah Bermain')


predict = ''

if st.button('Estimasi Tackle Won'):
    predict = model.predict(
        [[balls_recoverd, t_won, t_lost, clearance_attempted, match_played]]
    )
    st.write ('Estimasi Jumlah Tackle won dalam pertandingan UCL :', predict)