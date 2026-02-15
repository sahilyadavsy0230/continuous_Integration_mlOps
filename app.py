import streamlit as st

st.title('Simple Calculator')
st.write('enter a valuer for cube,square and fifth power')

n=st.number_input('Enter a Integer',step=1,value=1)

square=n**2
cube=n**3
fifth=n**5

st.write(f'the square of num {n} is {square}')
st.write(f'the cube of num {n} is {cube}')
st.write(f'the fifth power of num {n} is {fifth}')
