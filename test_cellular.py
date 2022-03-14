from cellularAutomata import *

"""testing fucntions"""


def test_initial_generation():
    state_even = generate_initial_state(16)
    state_odd = generate_initial_state(17)
    assert set(state_even) == {'.','0'} and set(state_odd) == {'.','0'}
    assert len(state_even) == 16
    assert len(state_odd) == 17

def test_generation_single_alive():
    state = generate_initial_state(25)
    num_of_0 = sum(1 for i in state if i == '0')
    assert num_of_0 == 1

def test_evolve_state():
    state = generate_initial_state(13)
    new_state = evolve_state(state, rule30)
    assert len(state) == len(new_state)
    assert set(new_state) == {'.','0'}

def test_circular_borders():
    assert '00...0' == evolve_state('0.....', rule30)
    assert '0...00' == evolve_state('.....0', rule30)

def test_rule30():
    length = 21
    nstep = 10
    rule = rule30
    sim = simulation(length, nstep, rule)
    assert '00..0....0.0000.00..0' == sim[-1]