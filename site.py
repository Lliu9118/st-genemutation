import requests
import streamlit as st
import array as ary
import pandas as pd
import altair as alt


st.set_page_config(page_title="My Webpage", page_icon=":skull:", layout="wide")
a = ary.array('i',[5])




data1ACC26 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944', 'ENSG00000217128', 'ENSG00000232505', 'ENSG00000254521', 'ENSG00000259224', 'ENSG00000269460'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data2ACC25 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944', 'ENSG00000217128', 'ENSG00000232505', 'ENSG00000254521', 'ENSG00000259224'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data3ACC24 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944', 'ENSG00000217128', 'ENSG00000232505', 'ENSG00000254521'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data4ACC23 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944', 'ENSG00000217128', 'ENSG00000232505'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data5ACC22 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944', 'ENSG00000217128'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data6ACC21 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711', 'ENSG00000214944'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data7ACC20 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969', 'ENSG00000214711'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data8ACC19 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604', 'ENSG00000204969'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data9ACC18 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513', 'ENSG00000204604'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data10ACC17 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890', 'ENSG00000204513'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data11ACC16 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468', 'ENSG00000198890'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data12ACC15 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963', 'ENSG00000197468'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data13ACC14 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558', 'ENSG00000196963'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data14ACC13 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293', 'ENSG00000188558'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data15ACC12 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953', 'ENSG00000188293'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data16ACC11 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527', 'ENSG00000187953'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data17ACC10 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372', 'ENSG00000187527'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data18ACC9 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567', 'ENSG00000187372'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data19ACC8 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520', 'ENSG00000185567'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data20ACC7 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434', 'ENSG00000183520'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data21ACC6 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752', 'ENSG00000183434'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5] ,})
data22ACC5 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143', 'ENSG00000182752'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5, 0.5] ,})
data23ACC4 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433', 'ENSG00000181143'] ,
'Asian_p': [0.5, 0.5, 0.5, 0.5] ,})
data24ACC3 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163', 'ENSG00000180433'] ,
'Asian_p': [0.5, 0.5, 0.5] ,})
data25ACC2 = pd.DataFrame({'Gene': ['ENSG00000177380', 'ENSG00000179163'] ,
'Asian_p': [0.5, 0.5] ,})
data26ACC1 = pd.DataFrame({'Gene': ['ENSG00000177380'] ,
'Asian_p': [0.5] ,})


with st.container():
    st.title("The Gene Mutation Interactive Tool")
    #st.subheader("Helping to go further in studies on race and cancer")
with st.container():
    #st.download_button(
        #label="Download data as CSV",
    #data=csv,
    #file_name='miRNA_outputs.csv',
    #mime='text/csv',
         #)
    with st.container():
        st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Goal")
        st.write("##")
        st.write("In past research on the correlation between race and the frequency of cancer within those races, researchers lacked an efficient and simple way to gain access to the most prevalent cancerous genes by race. Our interactive tool strives to assist the further research on the topic of cancer and race. With a few clicks, researchers of the future will be able to easily gain access to the most prevalent genes within affected patients.")
  
    option = st.selectbox(
        'Which cancer type would you like to view?',
        ('THYM', 'UCEC', 'UCS', 'UVM', 'ACC', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LAML', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA',))
    st.write('You selected:', option)
    option2 = st.selectbox(
        'Which race would you like to view?',
        ('Asian', 'White', 'Black',))
    st.write('You selected:', option2)
    color = st.select_slider(
        'Select the amount of genes you would like to view.',
        options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"])
    
    st.write('You have selected', color, 'gene(s).')

if option == 'ACC' and option2 == 'Asian' and color == '26':
        st.write(alt.Chart(data1ACC26).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '25':
        st.write(alt.Chart(data2ACC25).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '24':
        st.write(alt.Chart(data3ACC24).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '23':
        st.write(alt.Chart(data4ACC23).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '22':
        st.write(alt.Chart(data5ACC22).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '21':
        st.write(alt.Chart(data6ACC21).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '20':
        st.write(alt.Chart(data7ACC20).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '19':
        st.write(alt.Chart(data8ACC19).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '18':
        st.write(alt.Chart(data9ACC18).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '17':
        st.write(alt.Chart(data10ACC17).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '16':
        st.write(alt.Chart(data11ACC16).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '15':
        st.write(alt.Chart(data12ACC15).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '14':
        st.write(alt.Chart(data13ACC14).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '13':
        st.write(alt.Chart(data14ACC13).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '12':
        st.write(alt.Chart(data15ACC12).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '11':
        st.write(alt.Chart(data16ACC11).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '10':
        st.write(alt.Chart(data17ACC10).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '9':
        st.write(alt.Chart(data18ACC9).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '8':
        st.write(alt.Chart(data19ACC8).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '7':
        st.write(alt.Chart(data20ACC7).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '6':
        st.write(alt.Chart(data21ACC6).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '5':
        st.write(alt.Chart(data22ACC5).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '4':
        st.write(alt.Chart(data23ACC4).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '3':
        st.write(alt.Chart(data24ACC3).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '2':
        st.write(alt.Chart(data25ACC2).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
if option == 'ACC' and option2 == 'Asian' and color == '1':
        st.write(data26ACC1)
        st.write(alt.Chart(data26ACC1).mark_bar().encode(
           x=alt.X('Gene', sort=None),
           y='Asian_p', 
        ))
