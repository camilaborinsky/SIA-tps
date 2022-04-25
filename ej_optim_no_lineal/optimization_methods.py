optimization_methods = {'GD', 'GC', 'ADAM'}

from scipy.optimize import minimize
from functions import ErrorWrapper, error
from autograd.misc.optimizers import adam
import numdifftools as nd

from individual import Individual
def minimize_gd(ind: Individual, expected_output, reagents):
   
    return minimize(error, ind.genotype, args=(expected_output, reagents), method='BFGS')
    
def minimize_cg(ind: Individual, expected_output, reagents):
    return minimize(error, ind.genotype, args=(expected_output, reagents), method='CG')

def minimize_adam(ind:Individual, expected_output, reagents):
    wrapper = ErrorWrapper(reagents, expected_output)
    return adam(nd.Gradient(wrapper.apply_function),ind.genotype,step_size=0.80085)