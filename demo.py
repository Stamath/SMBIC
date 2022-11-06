#PACKAGES######################################
import os
import numpy as np
import timeit
import random
import sys
# set random seed #########################################
seed = 123
########### main ##########################
# the number of nodes #####################
N= 1200
#the true number of communities###############
K0= 3
# underling distribution ###################
clusters_distribution=np.ones((K0,))*1/K0
# the out-in ratio parameter###############
beta=0.15
# the network density #######################
rho= np.sqrt(1/N)
# the maximum candidate of K ########################
Kmax=10
# the candidta set of communities
mathcalK=np.arange(1,Kmax+1)

# SM-BIC for SBM ############################
# insert the path of functions ####################
sys.path.insert(0,'/SMBIC/Functions')
# import required functions############################
from SPARSE_SBM import SPARSE_SBM
from SMBIC_sbm import SMBIC_sbm
from Evaluation import Evaluation
# generate a network from sbm ############################
Data_SBM= SPARSE_SBM(N,clusters_distribution,rho,beta)
# label vector ############################
labels= Data_SBM[0]
# adjacency matrix############################
A= Data_SBM[1]
print('the edge density is', np.sum(A)/(N*(N-1)))
# the subsample size ############################
n= int(np.log(N)/rho)
# model selection for SBM #################
SMBIC_Results= SMBIC_sbm(A,mathcalK,n)
SMBIC_HAT_K= SMBIC_Results[0]
SMBIC_CPU_time = SMBIC_Results[1]
print("The selected number of communities of SBM is", SMBIC_HAT_K)
print("The computational time is ", SMBIC_CPU_time)


#######SM-BIC for DCSBM#############################
# import required packages 
from DCSBM import DCSBM
from SMBIC_dcsbm import SMBIC_dcsbm
# the degree parameters#########################
alpha=0.4
# create the heterogeneity paramter vector 
alpha_vec=np.empty((N,))
for i in range(0,N):
    index=np.random.choice(3,1, replace=True,p= np.array([alpha, (1-alpha)/2,(1-alpha)/2]))
    if index==0:
        alpha_vec[i]= np.random.uniform(3/5,7/5,1)
    if index==1:
        alpha_vec[i]= 1/3
    if index==2:
        alpha_vec[i]= 5/3

Data_DCSBM= DCSBM( N,clusters_distribution,rho,beta,alpha_vec,del_0d = False)
labels= Data_DCSBM[0]
A= Data_DCSBM[1]
print('the edge density is', np.sum(A)/(N*(N-1)))

# model selection for DCSBM #################
SMBIC_Results= SMBIC_dcsbm(A,mathcalK,n)
SMBIC_HAT_K = SMBIC_Results[0]
SMBIC_CPU_time  = SMBIC_Results[1]

print("The selected number of communities of dcsbm is", SMBIC_HAT_K)
print("The computational time is ", SMBIC_CPU_time)



            










