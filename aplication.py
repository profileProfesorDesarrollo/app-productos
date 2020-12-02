from faker import Faker
from datetime import datetime

from random import randrange
from datetime import timedelta
import numpy as np
import pandas as pd
import random
import sys

class aplication:
      
    def random_price(self,start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def genPriceToProduct(self, productEntity):
        faker = Faker()
        price = random.random()*10
        name = productEntity['nombre']
        cod  = productEntity['cod']
        strLine = ""+str(cod)+";"+str(name)+";"+str(price)+"\n"
        return strLine  

    def saveDataInFile(self, fileName, products):
        file = open(fileName+".csv", 'w')
        strLine = "cod;nombre;precio\n"
        file.write(strLine)
        # print(len(products))
        for i in range(0,len(products)):           
            productEntity = products.loc[i]
            productStr = self.genPriceToProduct(productEntity)
            file.write(productStr)
        file.close()
    
    def list(self, list):
        print("Listado")
        print("**************************")
        print('cod'," | ",'nombre'," | ", 'precio')
        for index, row in list.iterrows():
            print(row['cod']," | ",row['nombre']," | ", row['precio'])
    
    def search(self,search, products):
        print("Busqueda de un producto")
        print("**************************")
        return products.loc[products['cod'] == int(search)]

    def printMenu(self):
        print("**************************")
        print("* 1 - Listado            *")
        print("* 2 - Consultar          *")
        print("* 3 - Salir              *")
        print("**************************")