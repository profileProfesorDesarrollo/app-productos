from aplication import aplication
import sys

class utils:
    
    def list(self,app,products):
        app.list(products)

    def search(self,app,products):
        print(app.search(input("¿Cual es el codigo del producto?\n"), products))

    def exit(self,app,products):
        sys.exit()

    def switch_option(sellf,argument):
        switcher = {
            1: utils.list,
            2: utils.search,
            3: utils.exit,
        }
        return switcher.get(argument, 0)