# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 26/11/2019.

class pagination:

    def __getattr__(self, item):
        return item
    def __init__(self, *args, **kwargs):
        return None

    @staticmethod
    def number(total = 0, page = 0, url='/', cl=[]):
	
	
        content = '<ul class="{cl}">'.format(cl=cl[0])
    
        sr = int(total / 1)

        first_link = True
    
        if int(total) > 0:

            countpagesstr = list()

            if (int(page) > 0):

                content += '<li class="{cl}"><a class="{cl1}"  href="{url}/1" title="First">&laquo;</a></li>'.format(url=url, cl=cl[1], cl1=cl[2])  # first link
                previous_link = 1 if abs(1 - page) == 0 else abs(1 - page)


                content += '<li class="{cl}"><a  class="{cl1}" href="{url}/{previous_link}" data-page="{previous_link}" title="Previous">&lt;</a></li>'.format(
                    url=url, previous_link=previous_link, cl=cl[1], cl1=cl[2])

                for c in range(1, int(total + 1)):

                    if (page != c):

                        content += '<li  class="{cl}"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                           c=str(c), cl=cl[1], cl1=cl[2])

                    elif (page == c):
                        content += '<li  class="{cl} active"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                                 c=str(
                                                                                                                     c), cl=cl[1], cl1=cl[2])


                    elif (page == total):
                        content += '<li  class="{cl} active"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                                 c=str(
                                                                                                                     c), cl=cl[1], cl1=cl[2])

                    else:
                        content += '<li  class="{cl} active"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                                 c=str(
                                                                                                                     c), cl=cl[1], cl1=cl[2])

            else:

                for c in range(1, int(total + 1)):
                    if (c == 1):

                        content += '<li  class="{cl} active"><a  class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                                 c=str(
                                                                                                                     c),  cl=cl[1])


                    else:

                        content += '<li  class="{cl}"><a class="{cl1} href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                           c=str(c), cl=cl[1])

            if (page < total):
                next_link = int(page) + 1
                content += '<li class="{cl}"><a class="{cl1}" href="{url}/{next_link}" title="Next">&gt;</a></li>'.format(url=url,
                                                                                               next_link=next_link, cl=cl[1], cl1=cl[2])  # first link

                content += '<li  class="{cl}" ><a  class="{cl1}" href="{url}/{next_link}" data-page="{next_link}" title="Last">&raquo;</a></li>'. \
                    format(url=url, next_link=next_link, cl=cl[1], cl1=cl[2])
    
        content += '</ul>'
        if content is not None:
            return content
        else:
            return ""


    @staticmethod
    def alphabet(total = 0, page = '', url='/', cl=[]):
            
        alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
        content = '<ul class="{cl}">'.format(cl=cl[0])
        
        if int(total) > 0:
                for c in alphabet_list:
                    if (page != c):
                        content = '<li class="{cl}"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url, c=str(c), cl=cl[1], cl1=cl[2])																					   
                    elif (page == c):
                        content = '<li class="{cl} active"><a class="{cl1}" href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url, c=str(c), cl=cl[1], cl1=cl[2])
                    
        content += '</ul>'
        if content is not None:
            return content
        else:
            return ""
    
    @staticmethod
    def next_previous(total = 0, page = 0, url='/', cl=[]):

         content = '<ul class="{cl}">'.format(cl=cl[0])


         if int(total) > 0:


            if (int(page) > 0):

                content += '<li class="{cl}"><a class="{cl1}"  href="{url}/1" title="First">&laquo;</a></li>'.format(url=url, cl=cl[1], cl1=cl[2])  # first link
                previous_link = 1 if abs(1 - page) == 0 else abs(1 - page)


                content += '<li class="{cl}"><a  class="{cl1}" href="{url}/{previous_link}" data-page="{previous_link}" title="Previous">&lt;</a></li>'.format(
                        url=url, previous_link=previous_link, cl=cl[1], cl1=cl[2])
                
            if (page < total):
                next_link = int(page) + 1
                content += '<li class="{cl}"><a class="{cl1}" href="{url}/{next_link}" title="Next">&gt;</a></li>'.format(url=url,
                                                                                                next_link=next_link, cl=cl[1], cl1=cl[2])  # first link

                content += '<li  class="{cl}" ><a  class="{cl1}" href="{url}/{next_link}" data-page="{next_link}" title="Last">&raquo;</a></li>'. \
                        format(url=url, next_link=next_link, cl=cl[1], cl1=cl[2])
                        
         content += '</ul>'

         if content is not None:
            return content
         else:
            return ""