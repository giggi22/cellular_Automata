rule30 = {"000": '.', "00.": '.', "0.0": '.', "...": '.',
              "0..": '0', ".00": '0', ".0.": '0', "..0": '0'} #0 alive; . dead

rule90 = {"...": "0", "..0": ".", ".0.": "0", ".00": ".",
              "0..": ".", "0.0": "0", "00.": ".", "000": "0"}

rule110 = {"...": '0', "..0": '.', ".0.": '.', ".00": '0',
               "0..": '.', "0.0": '.', "00.": '.', "000": '0'}

rule184 = {"...": ".", "..0": "0", ".0.": ".", ".00": ".",
                "0..": ".", "0.0": "0", "00.": "0", "000": "0"}

"""function that generate the initial state"""
def generate_initial_state(lenght):
    if lenght%2 == 0:
        state = '.'*int(lenght/2-1)+'0'+'.'*int(lenght/2)  #...0....
    else:
        state = '.'*int(lenght/2)+'0'+'.'*int(lenght/2)
    return state

"""function that evolve the state"""
def evolve_state(state, rule):
    new_state = ''
    for i in range(len(state)):
        cond = state[i-1]+state[i]+state[(i+1)%len(state)]
        new_state += rule[cond]
    return new_state

"""simulation"""
def simulation(length, nsteps, rule):
    initial_state = generate_initial_state(length)
    state = [initial_state]
    for i in range(nsteps):
        state.append(evolve_state(state[-1], rule))
    return state
