def dfa (state, str, finalState, transitions):
    hasil = deltaTopi(state, str, transitions)
    if hasil in finalState:
        return [True, hasil]
    else:
        return [False, hasil]

def delta (state, a, transitions):
    # definisikan transition sesuai dengan modul yang dipilih
    transitions = transitions

    # kembalikan nilai state  dari transition yang sesuai
    return transitions[state][a]

def deltaTopi (state, str, transitions):

    # cek epsilon
    # lakukan delta topi hingga x sama dengan epsilon, jika belum lakukan rekursif
    # fungsi deltaTopi() mengembalikan state yang dipilih oleh fungsi delta()
    # kemudian update nilai dari state,  yang selanjutnya dijadikan parameter untuk menentukan state selanjutnya oleh fungsi delta()
    if str != '':
        # memecah string
        # a = char terakhir
        # x = sisa string
        x = str[:-1]
        a = str[-1]
        state = deltaTopi(state, x, transitions)
    else:
        return state

    # memanggil fungsi delta untuk memilih state sesuai transitionsnya 
    # lalu kembalikan nilai state tersebut ke fungsi yang memanggilnya
    return delta(state, a, transitions)

def input_string():
    string = input('ketik string :')
    print('String anda adalah ', string)
    return string

moduls = [
    {
        'namaModul':'L1',
        'deskripsi':'L1 adalah himpunan semua string yang mengandung substring 101',
        'initialState' : 'q0',
        'finalState' : ['q3'],
        'allState' : ['q0', 'q1', 'q2', 'q3'],
        'transitions':{
            'q0':{
                '0':'q0',
                '1':'q1'
            },
            'q1':{
                '0':'q2',
                '1':'q1'
            },
            'q2':{
                '0':'q0',
                '1':'q3'
            },
            'q3':{
                '0':'q3',
                '1':'q3'
            }
        }
    },
    {
        'namaModul':'L2',
        'deskripsi':'L2 adalah himpunan semua string yang mengandung prefiks 101',
        'initialState' : 'q0',
        'finalState' : ['q4'],
        'allState' : ['q0', 'q1', 'q2', 'q3', 'q4'],
        'transitions':{
            'q0':{
                '0':'q3',
                '1':'q1'
            },
            'q1':{
                '0':'q2',
                '1':'q3'
            },
            'q2':{
                '0':'q3',
                '1':'q4'
            },
            'q3':{
                '0':'q3',
                '1':'q3'
            },
            'q4':{
                '0':'q4',
                '1':'q4'
            }
        }
    },
    {
        'namaModul':'Input Lagi',
        'deskripsi':'input string baru!'
    },
    {
        'namaModul':'Selesai',
        'deskripsi':'Program telah berakhir..'
    }
    
]


# program utama
lanjut = True
string = input_string()
#menu
while(lanjut):
    #print menu
    print('\nPilih Modul')
    for i, v in enumerate(moduls):
        print(i+1, v['namaModul'], sep='. ')
        
    #pilih menu
    menu = int(input('Pilih Menu : '))
    
    if menu <= 0 or menu > len(moduls):
        print('Menu tidak tersedia. Mohon input menu kembali..')
    elif moduls[menu-1]['namaModul'] == 'Input Lagi':
        string = input_string()
    elif moduls[menu-1]['namaModul'] == 'Selesai':
        print(moduls[menu-1]['deskripsi'])
        lanjut = False
    else:
        #deskripsi
        print(moduls[menu-1]['deskripsi'])
        
        # memulai dfa
        initialState = moduls[menu-1]['initialState']
        finalState = moduls[menu-1]['finalState']
        transitions = moduls[menu-1]['transitions']
        isAccepted, hasil = dfa(initialState, string, finalState, transitions)
        if isAccepted:
            print('string diterima dengan final state adalah ',hasil)
        else:
            print('string tidak diterima dengan state akhir adalah',hasil)