from aplication import aplication
import sys

class utils:
    
    def list(self,app):
        app.list()

    def search(self,app):
        app.search()

    def exit(self,app):
        sys.exit()

    def switch_option(sellf,argument):
        switcher = {
            1: utils.list,
            2: utils.search,
            3: utils.exit,
        }
        return switcher.get(argument, 0)