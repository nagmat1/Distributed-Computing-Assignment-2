
#Nagmat Nazarov, February 28, 2022.
#CS791.1006 : Distributed Computing class. Programming Assignment 1.

from mpi4py import MPI
import sys
import hashlib
import time
import random
import argparse


VOTE_REQUEST = 1
VOTE_COMMIT = 200 
GLOBAL_COMMIT = 300 


def coordinate(comm,rank):
    vcommit = [0 for i in range(rank)] 

    try : 
        for x in range(0,rank):
            print("Rank 0 broadcasts VOTE_REQUEST to ",x)
            comm.send(VOTE_REQUEST,dest=x,tag=11)
    except Exception : 
        print(Exception)
    for x in range(0,rank):
        req = comm.recv(source=x)
        if (x == 0) and req == VOTE_REQUEST : 
            print("Received VOTE_REQUEST in {} ".format(comm.Get_rank()))
            comm.send(VOTE_COMMIT,dest=0,tag=11)
            req2 = comm.recv(source=0)
            if req2 == VOTE_COMMIT: 
                print("Received VOTE_COMMIT from {} ".format(x))
                vcommit[0]=1
        if req == VOTE_COMMIT :
            print("Received VOTE_COMMIT from {} ".format(x))
            vcommit[x] = 1;  
    b = True; 
    for x in range(0,rank): 
        b = b and vcommit[x]==1
    if b : 
        for x in range(0,rank):
            print("Rank 0 broadcasts GLOBAL_COMMIT to ",x)
            comm.send(GLOBAL_COMMIT,dest=x,tag=12)
            if x == 0 : 
                req3 = comm.recv(source=0)
                if req3 == GLOBAL_COMMIT:
                    print("Received GLOBAL_COMMIT from {} ".format(x))



def participate(comm):
    #print("In participate ",comm.Get_rank())
    req = comm.recv(source=0,tag=11)
    if req == VOTE_REQUEST :
        print("Received VOTE_REQUEST in {} ".format(comm.Get_rank()))
        comm.send(VOTE_COMMIT,dest=0,tag=11)
    req2 = comm.recv(source=0,tag=12)
    if req2 == GLOBAL_COMMIT:
        print("Received GLOBAL_COMMIT in {} ".format(comm.Get_rank()))


# Function for pruning T from system arguments
def komek():
    if len(sys.argv)>=2:
        inp = sys.argv[1]
    else :
        print("No parameter for T was included, please include T as a second parameter on console.")
        exit()

    try :
        t = int(inp)
    except ValueError:
        print('Incorrect integer : ', sys.argv[1])
        exit()

    if (t<1) or (t>10):
        print("T can't be zero, it should be a number between 1 to n=10")
        exit();
    return t

def main():
    #Begin the main program
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    name = MPI.Get_processor_name()
    #print("Rank = ",rank)
    if rank == 0 :
        print("Starting a {}-node cluster, with Rank0 as the coordinator".format(size))
        coordinate(comm,size) 
    else : 
        participate(comm)
    #sys.stdout.write(f"Process {rank} solved the puzzle in {wagt:.5f} seconds with solution = {sozlem}. \n")

if __name__ == '__main__': 
    t = komek()
    #print("Starting a {}-node cluster, with Rank0 as the coordinator".format(t))
    main()
