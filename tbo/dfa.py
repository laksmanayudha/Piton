class Dfa:

    # constructor, inisiasi objek mesin dfa
    def __init__(self, initialState, string, finalState, transitions):
        self.initialState = initialState
        self.string = string
        self.finalState = finalState
        self.transitions = transitions
    
    # -----------------------------------------------------------------------------------
    # method result digunakan untuk mencari hasil dfa
    def result (self):
    
        # mendapatkan hasil dari dfa, method deltaTopi mengembalikan state
        hasil = self.deltaTopi(self.initialState, self.string)

        # cek apabila state hasil termasuk ke dalam final state
        if hasil in self.finalState:
            return [True, hasil]
        else:
            return [False, hasil]
        
    # -----------------------------------------------------------------------------------
    # method delta digunakan untuk mencari state sesuai transition
    def delta (self, state, a):
        # definisikan transitions sesuai dengan modul yang dipilih
        transitions = self.transitions

        # kembalikan nilai state  dari transition yang sesuai
        return transitions[state][a]

    # -----------------------------------------------------------------------------------
    # method deltaTopi digunakan untuk meng-ekstensi dari transition
    def deltaTopi (self, state, string):

        # cek epsilon
        if string != '':
            # memecah string
            # a = char terakhir
            # x = sisa string
            x = string[:-1]
            a = string[-1]

            # rekursif method
            # lakukan delta topi hingga x sama dengan epsilon, jika belum lakukan rekursif
            # method deltaTopi() mengembalikan state yang dipilih oleh method delta()
            # kemudian update nilai dari state,  yang selanjutnya dijadikan parameter untuk menentukan state selanjutnya oleh method delta()
            state = self.deltaTopi(state, x)
        else:
            # jika string sudah epsilon maka kembalikan nilai state (initial state)
            return state

        # memanggil method delta untuk memilih state sesuai transitionsnya 
        # lalu kembalikan nilai state tersebut ke method yang memanggilnya
        return self.delta(state, a)




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