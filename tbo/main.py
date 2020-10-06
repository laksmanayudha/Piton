# import modul dfa yang merupakan kumpulan fungsi dari mesin dfa
from dfa import dfa_result, isStringValid, input_string

# varibel data merupakan kumpulan informasi dari menu yang digunakan oleh mesin dfa
data = [
    {
        'name':'L1',
        'description':'L1 adalah himpunan semua string yang mengandung substring 101',
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
        'name':'L2',
        'description':'L2 adalah himpunan semua string yang mengandung prefiks 101',
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
        'name':'L3',
        'description':'L3 adalah himpunan semua string yang mengandung sufiks 101',
        'initialState' : 'q0',
        'finalState' : ['q3'],
        'allState' : ['q0', 'q1', 'q2', 'q3', 'q4'],
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
                '0':'q4',
                '1':'q1'
            },
            'q4':{
                '0':'q0',
                '1':'q3'
            }
        }
    },
    {
        'name':'L4',
        'description':'L4 adalah himpunan semua string yang mengandung jumlah simbol 0 genap',
        'initialState' : 'q0',
        'finalState' : ['q0'],
        'allState' : ['q0', 'q1'],
        'transitions':{
            'q0':{
                '0':'q1',
                '1':'q0'
            },
            'q1':{
                '0':'q0',
                '1':'q1'
            }
        }
    },
    {
        'name':'L5',
        'description':'L5 adalah himpunan semua string yang mengandung jumlah simbol 1 ganjil',
        'initialState' : 'q0',
        'finalState' : ['q1'],
        'allState' : ['q0', 'q1'],
        'transitions':{
            'q0':{
                '0':'q0',
                '1':'q1'
            },
            'q1':{
                '0':'q1',
                '1':'q0'
            }
        }
    },
    {
        'name':'Input Lagi',
        'description':'input string baru'
    },
    {
        'name':'Selesai',
        'description':'Selesai'
    }
    
]


# program utama
lanjut = True
string = input_string()

#menu
while(lanjut):
    #print menu
    print('\nString :', string)
    print('Pilih Menu :')
    for i, v in enumerate(data):
        print(i+1, v['description'], sep='. ')
        
    # memilih menu
    menu = int(input('Pilih Menu : '))
    
    # eksekusi pilihan menu
    if menu > 0 and menu <= len(data):
        if data[menu-1]['name'] == 'Input Lagi':
            string = input_string()
        elif data[menu-1]['name'] == 'Selesai':
            print(data[menu-1]['description'])
            lanjut = False
        else:
            #print deskripsi modul
            print('\n')
            print(data[menu-1]['description'])
            
            # inisiasi initial state, final state, dan transitions
            initialState = data[menu-1]['initialState']
            finalState = data[menu-1]['finalState']
            transitions = data[menu-1]['transitions']

            # cari hasil dfa
            isAccepted, hasil = dfa_result(initialState, string, finalState, transitions)

            # tampilkan hasil dfa
            if isAccepted:
                print('string diterima dengan final state adalah ',hasil)
            else:
                print('string tidak diterima dengan state akhir adalah',hasil)
    else:
        print('Menu tidak tersedia. Mohon input menu kembali..')
        