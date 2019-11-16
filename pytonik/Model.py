###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


from . import App, Log

log_msg = Log.Log()


class Model:
    def __init__(self):
        self.App = App.App()
        self.db = self.App.DB()

    def load(self, m):
        import sys, os, importlib
        host = os.path.dirname(os.getcwd())
        DS = str("/")

        paths = host + DS + 'model'
        model = paths + DS + m + ".py"
        sys.path.append(paths)
        importlib._RELOADING
        if os.path.isfile(model) == True:

            try:

                md = importlib.import_module(m)
                ob = getattr(md, m)
                if hasattr(ob(), '__call__'):
                    return ob()
                else:
                    log_msg.error("'%s' is not a callable" % m)

            except Exception as err:
                log_msg.error(err)
                self.App.header(0)
                print(str(err))
        else:
            print("Model {e} does not exist ".format(m))
            log_msg.error("Model {e} does not exist ".format(m))
