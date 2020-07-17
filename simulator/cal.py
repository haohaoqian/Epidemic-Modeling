

import os
import json
import time
import argparse
import numpy as np



class cal:
    
    def total_nums(self,nodes):
        ret = {}  
        ret['infected'] = 0
        ret['susceptible'] = 0
        ret['death'] = 0
        ret['recovered'] = 0
        ret['asymptomatic'] = 0
        ret['latent'] = 0
        for k in nodes:
            ret['infected'] += k.infected
            ret['susceptible'] += k.susceptible
            ret['death'] += k.death
            ret['recovered'] += k.recovered
            ret['asymptomatic'] += k.infected_asymptomatic
            ret['latent'] += k.latent
        self.nums = ret
        self.total_population = self.nums['infected'] + self.nums["susceptible"] + self.nums['death'] + self.nums['recovered'] + self.nums['asymptomatic']
    def __init__(self,nodes):
        pass