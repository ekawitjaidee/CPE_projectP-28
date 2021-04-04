from Indicator import Indicator 
import random
import glob
import numpy as np
import pandas as pd

class GA():
  def initial_population(self,n):#number Population
    pop = []
    for i in range(n):
        pop.append([[random.randint(1,60),random.randint(1,60),random.randint(1,60)],0])
    return pop

  def cal_fitness_MACD(self,pop,df):
    calpop = []
    for cm in pop:

        df = Indicator().MACD(df,cm[0][0],cm[0][1],cm[0][2])
        b = df.loc[(df['MACD']>df['SIGNAL LINE'])&(df['MACD'].shift()<df['SIGNAL LINE'].shift())]['Close']
        bd = df.loc[(df['MACD']>df['SIGNAL LINE'])&(df['MACD'].shift()<df['SIGNAL LINE'].shift())].index
        s = df.loc[(df['MACD'] < df['SIGNAL LINE'])  & (df['MACD'].shift()>df['SIGNAL LINE'].shift())]['Close']
        sd = df.loc[(df['MACD'] < df['SIGNAL LINE'])  & (df['MACD'].shift()>df['SIGNAL LINE'].shift())].index
        b,bd,s,sd = b.tolist(),bd.tolist(),s.tolist(),sd.tolist()
        
        money = 10000
      
        if len(b)==0 or len(s)==0:
            calpop.append([cm[0],0])
        else:
            if bd[0]>sd[0]:
                s.pop(0)
                sd.pop(0)   
            if len(b)>len(s):
                b.pop()
                bd.pop() 

            pfmacd= []
            profitmacd = []
            for i in range(len(b)):
                pfmacd.append(((s[i]-b[i])/(b[i]))*money)
                profitmacd.append(((s[i]-b[i])/(b[i])))
            pfmacd = sum(pfmacd)
            # print(len(bd),len(sd))
            calpop.append([cm[0],pfmacd])
    return calpop

  def binarytournament(self,p):
    a = random.randint(0,len(p)-1)
    b = random.randint(0,len(p)-1)
    while a==b:
        b = random.randint(0,len(p)-1)
    
    pr1,pr2 = [],[]

    for i in range(len(p)):
        if i == a :
            pr1 = p[i]
        if i == b :  
            pr2 = p[i]
          
    if pr1[1] > pr2[1] :    
        return pr1
    else:
        return pr2


  def crossover(self,p1,p2):
    pcent = random.randint(0,len(p1[0])-1)
    newp1,newp2 = [],[]
    newp1 = p1[0][pcent:]+p2[0][:pcent]
    newp2 = p2[0][pcent:]+p1[0][:pcent]

    p1[0] ,p2[0]= newp1,newp2
    return p1,p2

  def mutation(self,o):
    Mutarate = (1/len(o[0]))*100 # mutation rate = (1/individual size) * 100 

    for i in range(len(o[0])):
      if random.randint(0,100) <= int(Mutarate):
        o[0][i] = random.randint(1,60)

    return o

  def first_generation(self,popsize,df):
    pop = GA().initial_population(popsize)
    pop = GA().cal_fitness_MACD(pop,df)
    pop = sorted(pop,key=lambda l:l[1],reverse=True)
    
    return pop

  def fit(self,pop,Maxgen,Elite,df):
    generation = 1
    popsize = len(pop)
    while generation < Maxgen:

      newpop = []
      for i in range(int(len(pop)*Elite/100)):
          newpop.append(pop[i])
          del pop[i]

      while len(newpop) < popsize:
          parent1,parent2 = GA().binarytournament(pop),GA().binarytournament(pop)
          while parent1 == parent2:
                  parent2 = GA().binarytournament(pop)
                  
          parent1,parent2 = GA().crossover(parent1,parent2)
          parent1,parent2 = GA().mutation(parent1),GA().mutation(parent2)
      
          newpop.append(parent1)
          newpop.append(parent2)
      print('Gen =',generation,'Max Fitness =',round(newpop[0][1],2),'Best Chomosome = ',newpop[0][0])
      generation += 1
      pop = newpop
      pop = GA().cal_fitness_MACD(pop,df)
      pop = sorted(pop,key=lambda l:l[1],reverse=True)
      
    return pop
