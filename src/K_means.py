from cmath import sqrt
from itertools import islice
from itertools import groupby 
class K_means:

    def __init__(self, data, k,rand):
        self.data = data
        self.k =k
        self.rand=[1,4]
        self.centroids={}

      
    def start(self):
        self.definecentroids()
       

    def definecentroids(self):

        self.centroids
        for (key, value) in self.data.items():
            for i in self.rand:
                if key == str(i) :
                    self.centroids[key]=value

        self.obtainclusters()
        

    def obtainclusters(self):

        resumed_data = []
        data = iter(self.data.items())

        for i in range(1,self.k):
            resumed_data.append(dict(islice(data, len(self.data) // self.k)))
        
        resumed_data.append(dict(data))
        
        m=[]
        for resume in resumed_data:
            for i in range(2):
                clus=0
                for dic in resume:
                    clus=clus+(float(resume[dic][i]))
                clus=(1/len(resume))*(clus)
                m.append(clus)
                # print(m)
        
  

        menor=[]
        for i in range(len(resumed_data)):
            lis= list(self.centroids.values())[i]
            resum =list(resumed_data[i].values())
            for j in resum:
                print("lis",lis)
                print("j",j)
                d=(sqrt(pow(abs(float(lis[0])-float(j[0])),exp=2)+pow(abs(float(lis[1])-float(j[1])),exp=2))).real
                menor.append(d)
                print(d)
            res = [min(val) for keys, val in groupby(menor, key = lambda x: x != 0) if keys != 0]
            print(res)



                

               
        

            

                

    