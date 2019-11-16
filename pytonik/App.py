###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


from .Request import Request
from .Router import Router
from .Editor import HTMLeditor
from .Config import Config
from .Log import Log
from . import Lang
from . import Version
from .Core.Helpers import Helpers
from .Functions import url
import os, sys, cgi, cgitb

cgitb.enable()

log_msg = Log()

global host, u, error_page_html, error_page_class

host = os.path.dirname(os.getcwd())
DS = str("/")
u = url
error_page_html = host + DS + 'views' + DS + "404.html"
error_page_class = host + DS + 'controller' + DS + "ErrorController" + ".py"



class App(Router):


    def __init__(self, routers="", routes="", getpath="", getrouters=""):

        self.routers = routers
        self.routes = routes
        self.getpath = getpath
        self.getrouters = getrouters
        self.getDB = ""
        self.Router = Router
        self.Request = Request
        self.methodprefix = ""
        self.actions = ""
        self.controllers = ""
        self.routersc = ""
        self.dbDriver = None
        self.Config = None
        self.url = ""
        self.params = ""
        self.key = ""
        self.vpathf = ""
        self.languages = ""

    def getRouters(self):

        return self.routers

    def getPath(self):
        return self.getpath

        # @staticmethod

    def runs(self):

        env = self.env()
        # self.url = str(uri)

        self.Config = Config()
        self.Config.add(env)
        self.getrouters = self.Config.get('route')



        self.routersc = self.Router()
        self.methodprefix = self.routersc.getMethodPrefix()
        self.actions = self.routersc.getAction()
        self.controllers = self.routersc.getControllers()
        self.routers = self.routersc.getRoutes()
        self.languages = self.routersc.getLanguages()
        self.params = self.routersc.getParams()



        seperator = str("/")


        newUri = str(self.controllers) + seperator + str(self.actions)

        langs = Lang.Lang(self.languages)
        langs.loadLang()


        if newUri in self.getrouters:
            routesUri = self.getrouters[newUri].split('@')
        else:
            routesUri = []

        if len(routesUri) != 0:

            controllersClass = str(self.controllers[0].capitalize()) + str(self.controllers[1:]) + 'Controller'

            controllersMethods = str(self.methodprefix) + str(routesUri[1])

        else:

            controllersClass = str(self.controllers[0].capitalize()) + str(self.controllers[1:]) + 'Controller'

            controllersMethods = str(self.methodprefix) + str(self.actions)

        m = self.actions

        host = os.path.dirname(os.getcwd())
        DS = str("/")
        controllerpath = host + DS + 'controller'
        controllers = controllerpath + DS + controllersClass + ".py"


        if os.path.isfile(controllers) == True:
            NewClass = controllers
        else:
            NewClass = controllerpath + DS + 'IndexController.py'

        if __name__ == '__main__':
            print("")
        if os.path.isfile(NewClass) == True:

            if sys.version_info.major <= 2:
                self.strClass(controllerpath, controllersClass)
            else:
                self.strClass3(controllerpath, controllersClass)

    def DB(self):
        env = self.env()

        self.Config = Config()
        self.Config.add(env)
        self.dbDriver = self.Config.get('dbConnect')
        if self.dbDriver["driver"] == "MYSQLi":
            from .MYSQLiDB import MYSQLiDB
            self.getDB = MYSQLiDB(self.dbDriver)
            return self.getDB
        if self.dbDriver(self.SQLite) == "SQLite":
            from .SQLite import SQLite
            self.getDB = SQLite(self.dbDriver)
            return self.getDB


    def strClass(self, p=None, c=None):
        import sys, os, importlib

        try:
            sys.path.append(p)
            ms = str(self.actions)
            md = importlib.import_module(c)
            ob = self.strMethod(md, ms)
            ob()
        except Exception as err:
            log_msg.error(err)

            if os.path.isfile(error_page_class) == True:
                self.redirect(u.url().url("/error/page/404"))
                self.header(1)
            else:
                self.error_p(error_page_html, error_page_class)


                # print("")
            # print(str(err))

    def strMethod(self, c=None, m=None):
        return getattr(c, m)

    def strClass3(self, p=None, c=None):
        import sys, os, importlib
        # print(__loader__)

        try:
            sys.path.append(p)
            ms = str(self.actions)
            importlib._RELOADING
            md = importlib.import_module(c, ms)
            ob = self.strMethod(md, ms)
            ob()
        except Exception as err:

            log_msg.error(err)

            if os.path.isfile(error_page_class) == True:
                self.redirect(u.url().url("/error/page/404"))
                self.header(1)
            else:
                self.error_p(error_page_html, error_page_class)



    def importClass(self, path, c):
        import glob, importlib, inspect, os, sys
        sys.path.append(path)
        current_dir = os.path.join(path)

        current_module_name = os.path.splitext(os.path.basename(current_dir))[0]

        for file in glob.glob(os.path.join(current_dir + "/*.py")):

            name = os.path.splitext(os.path.basename(file))[0]

            # Ignore __ files
            if name.startswith("__"):
                continue
            if name == c:

                try:

                    module = importlib.import_module("." + name, package=current_module_name)
                    for member in dir(module):
                        print(member)
                        handler_class = getattr(module, member)

                        # if handler_class and inspect.isclass(handler_class):
                        # print(member)

                except Exception as err:
                    log_msg.error(err)

        return None
        # do something with the member named ``member``

    # @staticmethod
    def redirect(self, location='/'):
        print("Location: {location}".format(location=location))

    @staticmethod
    def header(p=0, type="text/html"):
        import sys
        pyversionmajor = sys.version_info.major
        pyversionminor = sys.version_info.minor
        if pyversionmajor <= 2 and pyversionminor <= 7:
            reload(sys)
            sys.setdefaultencoding('utf-8')
        elif pyversionmajor == 3 and pyversionminor <= 3:
            import imp
            imp.reload()

        elif pyversionmajor >= 3 and pyversionminor >= 4:
            import importlib
            importlib.reload(sys)
        print("Content-type: {type}\r\n\r\n".format(type=type))
        if p > 0:
            for x in range(p):
                print("")

    def views(self, pathf="", datag={}, datal={}):

        if pathf == "":
            pathf = self.getDefaultViewPath()



        pathfhtml = host + DS + 'views' + DS + pathf + ".html"

        if os.path.isfile(pathfhtml) == False:

            data = {}

            ##check page
            error_page_html = host + DS + 'views' + DS + "404.html"
            error_page_class = host + DS + 'controller' + DS + "ErrorController" + ".py"

            if os.path.isfile(error_page_html) == True and os.path.isfile(error_page_class) == True:
                self.vpathf = error_page_html

            else:
                try:

                    self.error_p(error_page_html, error_page_class)
                    log_msg.info("404 html file as been create")
                except Exception as err:
                    log_msg.error(err)

                return False

            self.read_html(host + DS + 'views' + DS, '404', datag)

        else:

            if os.path.isfile(pathfhtml) == True:
                self.vpathf = pathfhtml
            elif os.path.isfile(pathfpy) == True:
                self.vpathf = pathfpy

            # self.renderTemp(self.vpathf, datag, datal)
            self.read_html(host + DS + 'views' + DS, pathf, datag)

        return False

    def read_html(self, template_dir, engine, context=[]):

        html_file_path = os.path.join(template_dir, "%s.html" % engine)
        try:
            with open(html_file_path) as html_file:
                html = html_file.read()
            print(HTMLeditor.Template(html).render(**context))
        except Exception as err:
            log_msg.error(err)

    def getDefaultViewPath(self):

        router = self.Router.getRoutes()  # Routers.getRoutes()

        if router == "":
            print("")
            # return False

        controllerDirectory = Routers.getControllers()

        templateName = str(Routers.getMethodPrefix()) + str(Routers.getAction()) + '.html'

        return templateName

    def error_p(self, error_page_html, error_page_class):
        try:
            f1 = open(error_page_html, 'a+')
            f1.write("<h1>404 Not Found</h1>")
            f1.close()

            f0 = open(error_page_class, 'a+')
            f0.write("from pytonik import Web\n"
                         "m = Web.App()\n"
                         ""
                         "def index():\n"
                            "   m.header(0)\n"
                            "   data = {'title': 'pytonik MVC'}\n"
                            "   m.views('404', data)\n"
                     ""
                        "\ndef page():\n"
                            "   m.header(0)\n"
                            "   data = {'title': 'pytonik MVC'}\n"
                            "   m.views('404', data)\n"
                            "")
            f0.close()
        except Exception as err:
            log_msg.error(err)

    def loadmodule(self):
        import glob, importlib, inspect, os, sys
        # sys.path.append(pl)

        path_1 = os.path.dirname(__file__)+ str("/") +str("Functions")
        path_2 = os.path.dirname(os.getcwd()) + str("/") + "model"
        listpath = [path_1, path_2]
        i = 0
        lclass = {}

        for pl in listpath:

            current_dir = os.path.join(pl)

            current_module_name = os.path.splitext(os.path.basename(current_dir))[0]

            for file in glob.glob(os.path.join(current_dir + "/*.py")):

                name = os.path.splitext(os.path.basename(file))[0]
                i = i + 1
                # Ignore __ files
                ++i
                if name.startswith("__init__"):
                    continue
                if name is not "__init__":
                    lclass0 = {name: name}
                    lclass.update(lclass0)

        if Version.PYVERSION_MA <= 2:
            item = lclass.iteritems()
        else:
            item = lclass.items()
        result = {}
        for key, value in item:
            if value not in result.values():
                result[key] = value

        return result
