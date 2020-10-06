def dfa_result (state, string, finalState, transitions):
    
    hasil = deltaTopi(state, string, transitions)

    # cek apabila state hasil termasuk ke dalam final state
    if hasil in finalState:
        return [True, hasil]
    else:
        return [False, hasil]

def delta (state, a, transitions):
    # definisikan transition sesuai dengan modul yang dipilih
    transitions = transitions

    # kembalikan nilai state  dari transition yang sesuai
    return transitions[state][a]

def deltaTopi (state, string, transitions):

    # cek epsilon
    # lakukan delta topi hingga x sama dengan epsilon, jika belum lakukan rekursif
    # fungsi deltaTopi() mengembalikan state yang dipilih oleh fungsi delta()
    # kemudian update nilai dari state,  yang selanjutnya dijadikan parameter untuk menentukan state selanjutnya oleh fungsi delta()
    if string != '':
        # memecah string
        # a = char terakhir
        # x = sisa string
        x = string[:-1]
        a = string[-1]
        state = deltaTopi(state, x, transitions)
    else:
        return state

    # memanggil fungsi delta untuk memilih state sesuai transitionsnya 
    # lalu kembalikan nilai state tersebut ke fungsi yang memanggilnya
    return delta(state, a, transitions)

def isStringValid(alphabet, string):
    for char in string:
        if char not in alphabet:
            return False
    
    return True

def input_string():
    alphabet = ['1', '0']
    while(True):
        print('\n')
        string = input('ketik string (Alphabet = {1, 0}) :')
        print('String anda adalah ', string)
        if isStringValid(alphabet, string):
            return string
        else:
            print('String yang anda masukan tidak sesuai dengan alphabet')