from __future__ import print_function
from __future__ import division
#coding: utf-8
import numpy as np
Pa = 0.018 #无症状感染者比例(比例)
eps_1 = 250 # 潜伏期时长(30min)
eps_1_d = 5.2 # 潜伏期时长(day)
d = 0.15 #自然死亡率(比例)
t = 672 # 康复时间(30min)
t_d = 14 # 康复时间(day)
d_hospital = 0.04#医院死亡率(比例)
t_hospital = 614 #医院康复时间(30min)
t_hospital_d = 12.8 #医院康复时间(day)
R_0 = 2.68 #基本传染数
r_a = 0.6 #无症状感染者传染系数(比例)
r_L = 1.0 #潜伏期传染系数(比例)
theta = 0 #收治率(30min)
eps = 1/eps_1 #平均潜伏期转化率(30min)
beta = R_0/ (r_L * eps_1_d + (Pa * r_a + (1- Pa)) * t_d) #I传染系数(day)
beta = np.power(1+beta,1/48)-1#I传染系数(30min)
L_I = eps * (1 - Pa)#L->I(30min)
L_Ia = eps * Pa # L->Ia(30min)
I_D = d / t #I->d(30min)
I_R = ((1 - d)/(t_d - d))/48 #I->R(30min)
I_h = 0 #I->h(30min),可调参数
Ia_R = 1 / t #Ia->R(30min)
Ih_D = d_hospital / t_hospital #Ih->D(30min)
Ih_R = ((1 - d_hospital)/ (t_hospital_d - d_hospital))/48 #Ih->R(30min)
beds_num_per_region = 200 #每个区域医院床位数
'''
    id： '0-xxx'
    susceptible:正常人
    latent：潜伏期人数
    infected：感染且有症状人数
    infected_asymptomatic:无症状感染者人数
    death:死亡数
    in_hospital:住院人数
    recovered：治愈人数
'''
class node :
    def __init__ (self,id ):
        self.id = id
        self.susceptible = 0
        self.infected = 0
        self.death = 0
        self.in_hospital = 0
        self.infected_asymptomatic = 0
        self.recovered = 0
        self.latent = 0            
    def set_susceptible(self,susceptible):
        self.susceptible = susceptible
    def set_latent(self,latent):
        self.latent = latent
    def set_infected(self,infected):
        self.infected = infected
    def set_infected_asymptomatic(self,infected_asymptomatic):
        self.infected_asymptomatic = infected_asymptomatic
    def set_death(self,death):
        self.death = death
    def set_in_hospital(self,in_hospital):
        self.in_hospital = in_hospital
    def set_recovered(self,recovered):
        self.recovered = recovered
    def step(self):
        if(self.susceptible+self.latent+self.infected+self.infected_asymptomatic+self.in_hospital+self.recovered>0):
            lambda_j = ((self.infected + self.infected_asymptomatic * r_a + self.latent * r_L) / (self.susceptible+self.latent+self.infected+self.infected_asymptomatic+self.in_hospital+self.recovered)) * beta
            susceptible_to_latent,__ = np.random.multinomial(self.susceptible,[lambda_j, 1])
            self.susceptible -= susceptible_to_latent
            self.latent += susceptible_to_latent

            latent_to_infected,latent_to_Ia,__ = np.random.multinomial(self.latent,[L_I, L_Ia, 1]) 
            self.infected += latent_to_infected
            self.infected_asymptomatic += latent_to_Ia
            self.latent -= (latent_to_Ia + latent_to_infected)

            infected_to_death,infected_to_recovered,__ = np.random.multinomial(self.infected,[I_D,I_R,1])
            self.death += infected_to_death
            self.recovered += infected_to_recovered
            self.infected -= (infected_to_death + infected_to_recovered)

            Ia_to_recovered , __ = np.random.multinomial(self.infected_asymptomatic,[Ia_R,1])
            self.recovered += Ia_to_recovered
            self.infected_asymptomatic -= Ia_to_recovered

            in_hospital_to_death, in_hospital_to_recovered,__ = np.random.multinomial(self.in_hospital,[Ih_D,Ih_R,1])
            self.death += in_hospital_to_death
            self.recovered += in_hospital_to_recovered
            self.in_hospital -= (in_hospital_to_death + in_hospital_to_recovered)
'''
            if(self.in_hospital<beds_num_per_region):
                I_to_in_hospital , __ = np.random.multinomial(self.infected,[I_h,1])
                if(I_to_in_hospital>(beds_num_per_region-self.in_hospital)):
                    I_to_in_hospital=beds_num_per_region-self.in_hospital
                self.in_hospital+=I_to_in_hospital
                self.infected-=I_to_in_hospital
'''