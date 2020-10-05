def dfa (state, str, finalState):
    hasil = deltaTopi(state, str)
    if hasil in finalState:
        return [True, hasil]
    else:
        return [False, hasil]

def delta (state, a):
    transitions = {
        'q0':{
            '0':'q1',
            '1':'q0'
        },
        'q1':{
            '0':'q1',
            '1':'q2'
        },
        'q2':{
            '0':'q2',
            '1':'q2'
        }
    }
    return transitions[state][a]

def deltaTopi (state, str):
    x = str[:-1]
    a = str[-1]
    if x != '':
        state = deltaTopi(state, x)
    return delta(state, a)


# program utama
#inisiasi
string = '1110000'
initialState = 'q0'
finalState = ['q2']
allState = ['q0', 'q1', 'q2']

# memulai dfa
isAccepted, hasil = dfa(initialState, string, finalState)
if isAccepted:
    print('string diterima denga final state adalah ',hasil)
else:
    print('string tidak diterima dengan state akhir adalah',hasil)


