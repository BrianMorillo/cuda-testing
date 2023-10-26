from numba import jit, cuda 
import numpy as np 
from timeit import default_timer as timer   

# Array Length
N = 99999999 
  
# normal function to run on cpu 
def pow_arr(a):                                 
    for i in range(N): 
            a[i] = a[i]*a[i]
  
# function optimized to run on gpu  
@jit(target_backend='cuda')                          
def pow_arr2(a): 
    for i in range(N): 
            a[i] = a[i]*a[i]
        
if __name__=="__main__": 
    a = np.random.randint(0, 255, size=N)
      
    start = timer() 
    pow_arr(a) 
    print("without GPU:", timer()-start)     
      
    start = timer() 
    pow_arr2(a) 
    print("with GPU:", timer()-start)     