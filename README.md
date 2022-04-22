# Distributed-Computing-Assignment-2

Assignment : Two-phase Commit (2PC) Protocol using MPI. 

The assignment tested on : 
```
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

I designed two functions : 
1. Coordinater : Rank 0 is the coordinator which coordinates all the actions. At the same time, Rank 0 is acting as a participant.  
2. Participant : All the nodes are acting as a participant and Voting. 

#Requirements: 
``` 
apt install openmpi-bin 
```
#Using pip
```
pip install mpi4py 
```

# To compile : 
``` mpiexec python3 pa2.py 4 ``` 

is running 4 nodes and Rank 0 is the Coordinator. 
