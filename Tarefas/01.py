"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

st.write('# MD15-Tarefa02 - Códigos')

st.write('### 01- Dataframe:')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
#---------------------------
st.write('### 02- Dataframe + numpy')

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
#---------------------------
st.write('### 03- Style Dataframe + numpy ')

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
#---------------------------
st.write('### 04- Plot a map ')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#---------------------------
st.write('### 05- Widgets ')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
#---------------------------
st.write('### 06- Use checkboxes to show/hide data ')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#---------------------------
st.write('### 07- Use a selectbox for options ')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

#---------------------------
st.write('### 08- Show progress ')

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(5):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
#---------------------------
st.write('### 09- Examples of using Session State ')

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
#---------------------------
st.write('### 10- Formulário ')
with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.number_input('Número')
   my_text = st.text_input('texto')
   my_text_area = st.text_area('ltexto area')
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_text)
st.write(my_text_area)
st.write(my_color)

#---------------------------
st.write('### 11- Soma ')
col1,col2 = st.columns([1,2])
col1.title('Sum:')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

if submit:
    col2.title(f'{a+b:.2f}')

#---------------------------
st.write('### 12- Dataframe vazio ')

df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)
#---------------------------
st.write('### 13- Seleciona a coluna e exibe value_counts  ')
df_tips = sns.load_dataset('tips')
st.write(df_tips.head(2))
tip_coluna = df_tips.columns

tip_coluna_select = st.selectbox('Coluna',tip_coluna) 

st.write(df_tips[tip_coluna_select].value_counts())


#---------------------------
st.write('### 14- Gráfico linha ')


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)
#---------------------------
st.write('### 15- Gráfico Histograma ')

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
#---------------------------
st.write('### 16- Gráfico Barra ')


df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

#---------------------------
st.write('### 17- Gráfico de área ')

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

#---------------------------
st.write('### 18- Mudar cor ')
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

#---------------------------
st.write('### 19- Botão download um arquivo em csv ')


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(df_tips)

st.download_button(
    label="Download dataframe CSV",
    data=csv,
    file_name="df_tips.csv",
    mime="text/csv",
)


#---------------------------
st.write('### 20- histograma de dataframe gorjetas')


df20 = df_tips
coluna_data = st.selectbox('Coluna dataframe TIPs',df20.columns)
fig, ax = plt.subplots()
ax.hist(df20[coluna_data])
st.pyplot(fig)

#---------------------------
