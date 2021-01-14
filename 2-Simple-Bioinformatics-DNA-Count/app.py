import pandas as pd
import streamlit as st
import altair as alt

st.write("""

# Simple Bioinformatics DNA Count

This app counts the nucleotide composition of query DNA

***

""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('Input (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count')

# print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

dict_seq = DNA_nucleotide_count(sequence)
dict_seq

# print text
st.subheader('2. Print Text')
st.write('There are ' + str(dict_seq['A']) + ' adenine (A)')
st.write('There are ' + str(dict_seq['T']) + ' thymine (T)')
st.write('There are ' + str(dict_seq['G']) + ' guanine (G)')
st.write('There are ' + str(dict_seq['C']) + ' cytosine (C)')

# display dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(dict_seq, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# display bar chart using altair
st.subheader('4. Display Bar Chart')
bchart = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
bchart = bchart.properties(
    width=alt.Step(80)
)

st.write(bchart)