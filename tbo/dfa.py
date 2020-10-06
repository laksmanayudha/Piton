# fungsi dfa_result digunakan untuk mencari hasil dfa
def dfa_result (state, string, finalState, transitions):
    
    # mendapatkan hasil dari dfa, fungsi deltaTopi mengembalikan state
    hasil = deltaTopi(state, string, transitions)

    # cek apabila state hasil termasuk ke dalam final state
    if hasil in finalState:
        return [True, hasil]
    else:
        return [False, hasil]


# -----------------------------------------------------------------------------------
# fungsi delta digunakan untuk mencari state sesuai transition
def delta (state, a, transitions):
    # definisikan transitions sesuai dengan modul yang dipilih
    transitions = transitions

    # kembalikan nilai state  dari transition yang sesuai
    return transitions[state][a]



# -----------------------------------------------------------------------------------
# fungsi deltaTopi digunakan untuk meng-ekstensi dari transition
def deltaTopi (state, string, transitions):

    # cek epsilon
    if string != '':
        # memecah string
        # a = char terakhir
        # x = sisa string
        x = string[:-1]
        a = string[-1]

        # rekursif fungsi
        # lakukan delta topi hingga x sama dengan epsilon, jika belum lakukan rekursif
        # fungsi deltaTopi() mengembalikan state yang dipilih oleh fungsi delta()
        # kemudian update nilai dari state,  yang selanjutnya dijadikan parameter untuk menentukan state selanjutnya oleh fungsi delta()
        state = deltaTopi(state, x, transitions)
    else:
        # jika string sudah epsilon maka kembalikan nilai state (initial state)
        return state

    # memanggil fungsi delta untuk memilih state sesuai transitionsnya 
    # lalu kembalikan nilai state tersebut ke fungsi yang memanggilnya
    return delta(state, a, transitions)



# -------------------------------------------------------------------------------------
# fungsi isStringValid berfungsi apakah input user sesuai dengan alphabet
def isStringValid(alphabet, string):
    # loop string inputan user
    for char in string:
        # jika terdapat string yang tidak ada dalam alphabet, maka string salah
        if char not in alphabet:
            return False
    
    return True #string benar



# ---------------------------------------------------------------------------------------
# fungsi input_string() berfungsi untuk menerima inputan string dari user
def input_string():
    # definisikan alphabet
    alphabet = ['1', '0']

    # loop user input
    while(True):
        print('\n')
        
        # mengambil inputan
        string = input('ketik string (Alphabet = {1, 0}) :')
        print('String anda adalah ', string)

        # cek validasi string, jika valid kembalikan string, jika tidak minta hingga inputan benar
        if isStringValid(alphabet, string):
            return string
        else:
            print('String yang anda masukan tidak sesuai dengan alphabet')