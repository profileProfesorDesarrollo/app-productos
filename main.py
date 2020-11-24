# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from aplication import aplication
from utils import utils
import pandas as pd
import sys


def strip_spaces(a_str_with_spaces):
        return a_str_with_spaces.replace('\t', '')

def importData( fileName):
    products = pd.read_csv(fileName+".csv",";", converters={'nombre': strip_spaces})
    return products

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    app = aplication()

  

    if (len(sys.argv) == 2  and sys.argv[1] == "-h"):

        HelpMenu = open("help.txt", 'r')    
        print(HelpMenu.read() )
        HelpMenu.close()
        sys.exit()

    dataFileName = "productos"
    if (len(sys.argv) == 2):
        products = importData(sys.argv[1])


    app.saveDataInFile(dataFileName, products)
    # Import the productos.csv data: products
    option = 0
    while(option != 3):
        app.printMenu()
        option = int(input("Introduce una opción"))
        option = utils.switch_option(utils,option)
        if(option != 0):
            option(utils,app)