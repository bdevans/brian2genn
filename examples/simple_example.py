from brian2 import *
import brian2genn

prefs.core.default_float_dtype = np.float32

set_device('genn', directory='simple_example', use_GPU=False)
BrianLogger.log_level_debug()
N = 10000
tau = 10*ms
Iin = 0.11/ms 
eqs = '''
dV/dt = -V/tau + Iin : 1
'''
G = NeuronGroup(N, eqs, threshold='V>1', reset='V=0', refractory=5 * ms)

run(10*ms)
