from generator import generator
from prim import prim_n2, prim_mlogn
from kruskal import kruskal
from matplotlib.pyplot import plt 
from tqdm import tqdm 

def main():
    # This function should measure the efficiency of implemented algorithms
    # go through different values of n (eg: 10, 100, 1000, 10000) and for each n:
    # repeat >= 10 times:
    # 1. generate  random graph of size n
    # 2. run kruskal and prim on all those graphs
    # 3. measure the running time and average each (prim's and kruskal's)
    # 4. plot the results of running time vs n. There should be three curves:
    #       one for Kruskal, one for Prim's in O(n^2), and one for Prim's in O(m \log n)
    
    # additional:
    # vary the density and perform similar tests
    
    # USE tqdm to have a progress bar for the different graphs
    pass 

if __name__ == '__main__':
    main()