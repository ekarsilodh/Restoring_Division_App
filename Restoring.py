import streamlit as st
import pandas as pd

#defining page name & icon
st.set_page_config(
    page_title="Restoring Division Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
    }
)

#Font Selection
st.markdown(
    """
    <head>
        <link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Mooli' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=DancingScript' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Caveat' rel='stylesheet'>
    </head>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown(
    """
    <h1 style='text-align: center; font-family: Pacifico, sans-serif'>Restoring Division Calculator</h1>
    """,
    unsafe_allow_html=True
)


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    dt = pd.DataFrame(df)
    return dt.to_csv().encode('utf-8')


def dectobinq(num):
    a = bin(num).replace("0b","")
    if len(str(a)) < 4:
        a = str(a).zfill(4)
        return a
    else:
        return a 

def dectobinm(num):
    a = bin(num).replace("0b","")
    a = str(a).zfill(q_bit+1)
    return a
    #else:
        #return a 


#def tcomplement(neg):
    a = bin(neg).replace("0b","")
    num = str(a).zfill(4) if len(str(a)) < 4 else str(a).zfill(1 + len(str(a)))
        #print(num)
    
    lst = []
    for i in num:
        if i == '1':
            lst.append(str(0))
        elif i == '0':
            lst.append(str(1))
    b = ''.join(lst)
    complement = bin(int(b, 2) + int("1", 2)).replace("0b","")
    return complement

def tcomp(x):
    lst = [str(1) if i == '0' else str(0) for i in x]
    b = ''.join(lst)
    complement = bin(int(b, 2) + int("1", 2)).replace("0b","")
    return str(complement).zfill(len(b)) if len(str(complement)) < len(b) else str(complement)

def als(x, y):
    l1 = [i for i in x]
    l2 = [i for i in y]
    l1 += l2 
    #print(l1)
    b = ''.join(l1)
    #print(b)
    num = int(b, 2)
    num = num << 1
    c = bin(num).replace("0b","")
    #print(c)
    if l1[0] == '0':
        c = str(c).zfill(len(b))
        c = c[:-1] + "_"
        return c 
    #elif l1[0] == '1':
        z = '1' * (len(b)-len(str(c)))
        c = z + c
        return c

def sb(x, y):
    z = tcomp(y)
    #print("z=", z)
    l = bin(int(x, 2) + int(z, 2)).replace("0b","")
    if len(str(l)) < len(str(x)):
        l = str(l).zfill((len(str(x))))
        #print(l)
        return l 
    elif len(str(l)) > len(str(x)):
        l = l[-a_bit:]
        return l
    else:
        return l 

#print("\nRestoring Division Algorithm Calculator\n")

no1 = st.text_input("Enter the 1st no.")
no2 = st.text_input("Enter the 2nd no.")
if st.button("Calculate"):
    if no1 and no2:
        a = int(no1)
        b = int(no2)
        Q = dectobinq(a) #if a > 0 else tcomplement(a)
        q_bit = len(str(Q))
        Qf = Q

        M = dectobinm(b) #if b > 0 else tcomplement(b)

        #initialize the accumulator.
        A = '0' * len(str(M))
        size = len(str(Q))
        #print(size)

        #bits in A & Q
        a_bit = len(str(A))

        #print(a_bit)
        #print(q_bit)

        #adding the fictious bit to Q.
        #Qf = ficbit(Q)
        #print(Qf)
        #qf_bit = len(str(Qf))

        print(f"Q = {a} = {Qf}")
        print(f"M = {b} = {M}")
        #print(data)
        print("\n")

        data = [["Operation", "M", "A", "Q", "Size"]]
        data.append(['Initial', M, A, Q, size])
        #print(data)

        while(size!=0):
            size -= 1

            z = als(A, Q)
            A = z[:a_bit]
            Q = z[q_bit+1:]

            calc_data = ['ALS(AQ)', str(M), str(A), str(Q), '-']
            data.append(calc_data)

            A1 = sb(A, M)
            calc_data = ['A=A-M', str(M), str(A1), str(Q), '-']
            data.append(calc_data)

            if (A1[0] == '0'):
                Q = Q[:-1] + "1"
                A = A1
                calc_data = ['As sign of A +ve; Q[0]=1', str(M), str(A), str(Q), size]
                data.append(calc_data)

            elif (A1[0] == '1'):
                Q = Q[:-1] + "0"
                calc_data = ['As sign of A -ve; Q[0]=0', str(M), str(A1), str(Q), '-']
                data.append(calc_data)

                calc_data = ['Restore A', str(M), str(A), str(Q), size]
                data.append(calc_data)


        #result calculation
        l1 = [i for i in A]
        l2 = [i for i in Q]
        l1 += l2
        r_bit = a_bit + q_bit
        res_join = ''.join(l1)
        result = res_join[:r_bit]

        st.table(data)
        st.success(f"The quotient is: {Q}")
        st.success(f"The remainder is: {A}")

        csv = convert_df(data)

        st.download_button("Download CSV", data=csv, file_name='Booths.csv')
    else:
        st.error("Enter the nos!!!")

# Font Selection
st.markdown(
    """
    <head>
        <link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Mooli' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=DancingScript' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Caveat' rel='stylesheet'>
    </head>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown(
    """
    <h4 style='text-align: right; font-family: 'Roboto', cursive'; font-size: 25px>Designed & Maintained by</h4>
    <h3 style='text-align: right; font-family: 'Caveat', cursive'; font-size: 25px>Ekarsi Lodh</h3>
    <h4 style='text-align: centered; font-family: 'Dancing Script', sans-serif'; font-size: 20px>Let's Keep in Touch!</h4>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <li><a href="mailto:ekarsilodh@gmail.com">Gmail</a></li>
    <li><a href="https://www.linkedin.com/in/ekarsi-lodh" target="_blank">LinkedIn</a></li>
    """,
    unsafe_allow_html=True
)

