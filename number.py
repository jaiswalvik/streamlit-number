import streamlit as st

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number3 = st.number_input('Insert third number')
highest = 0
if number1 > number2 and number1 > number3:
	highest = number1
elif number2 > number3 and number2 > number1:
	  highest = number2
elif number3 > number1 and number3 > number2:
	  highest = number3  	 
st.write('Highest of 3 numbers', highest)
