###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import sys, os, cgitb
from pytonik import Version, Config, Log
cgitb.enable()
url = os.environ['REQUEST_URI']
log_msg = Log.Log()


class Router:
    def __init__(self):
        urlstr = str(url)
        self.uri = urlstr.split('/')

        Conf = Config.Config()
        Conf.add(self.env())

        self.controllers = Conf.get('default_controllers')
        self.actions = Conf.get('default_actions')
        self.languages = Conf.get('default_languages')
        self.routes = Conf.get('default_routes')
        self.methodprefix = ""
        self.params = ""



        #if "?" in self.uri:

            #uri_paths = urlstr.split("?")
            #path_array = uri_paths[0]
        #else:
            #uri_paths = urlstr.split('/')
            #path_array = uri_paths[0]

        uri_paths = urlstr.split('/')

        pathparts_array = uri_paths


        pathparts_paramarray = os.environ["QUERY_STRING"]

        pathparts_paramarrayOut = dict()
        if pathparts_paramarray != '':
            pairs = pathparts_paramarray.split('&')

            pathparts_paramarray = pairs

            for i in pairs:

                name, value = i.split('=', 2)

                pathparts_paramarray = {name: value}

                if name in pathparts_paramarray:

                    pathparts_paramarray[name] = value

                else:
                    pathparts_paramarray[name] = [pathparts_paramarray[name], value]

                pathparts_paramarrayOut.setdefault(name, value)



        else:
            pathparts_paramarrayOut = ""

        path_parts = pathparts_array


        if len(path_parts):

            #print(routes.keys())

            if Version.PYVERSION_MA < 3:
                path_parts = filter(None, path_parts)
            else:
                path_parts = list(filter(None, path_parts))



            routes = Conf.get('route')

            if list(set(path_parts).intersection(routes.keys())):

                for s in path_parts:

                    if s in routes:
                        self.routes = s

                        if self.routes in routes:
                            self.methodprefix = routes[self.routes]
                        else:
                            self.methodprefix = ""

                        #path_parts.append(path_parts.pop(-1))


            languages = Conf.get('languages')


            if list(set(path_parts).intersection(languages.keys())):

                for s in path_parts:
                    if s in languages:
                        self.languages = s
                        path_parts.append(path_parts.pop(-1))


            controllers = Conf.get('default_controllers')
            if controllers:

                i = 0
                path_parts = list(filter(None, path_parts))

                for s in path_parts:

                    if s is not self.languages:
                        i += 1

                        if i == 1:
                            self.controllers = s
                            path_parts.append(path_parts.pop(-1))
                    ++i


            action = Conf.get('default_actions')
            if action:
                i = 0
                for s in path_parts:
                    if s is not self.controllers and s is not self.languages:
                        i += 1
                        if i == 1:
                            self.actions = s
                            path_parts.append(path_parts.pop(-1))
                        ++i

            from .Core import Helpers
            h = Helpers
            list_params = []
            if pathparts_paramarray == None or pathparts_paramarray == "" :
                for s in path_parts:

                    if s is not self.controllers and s is not self.actions and s is not self.languages:
                        list_params.append(s)
                        path_parts.append(path_parts.pop(-1))

                self.params = Helpers.covert_list_dict(list_params)

            else:

                self.params = pathparts_paramarray
                path_parts.append(path_parts.pop(-1))



        return None

    def getUri(self):
        return self.uri

    def getControllers(self):

        return self.controllers

    def getAction(self):
        return self.actions

    def getParams(self):

        return self.params

    def getRoutes(self):

        return self.routes

    def getMethodPrefix(self):
        return self.methodprefix

    def getLanguages(self):


        return self.languages

    def env(self):

        import os

        host = os.path.dirname(os.getcwd())
        DS = str("/")

        envpath = host + DS + ".env"
        if os.path.isfile(envpath) == True:
            f = open(envpath, "r")
            return f.read()

        else:
            return ".env file not found"

