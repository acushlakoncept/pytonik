###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import string, os
from pytonik import Hash, Log
log_msg = Log.Log()

def pagination(total_pages, page, url):
    content = '<ul class="pagination">'

    sr = int(total_pages / 1)
    first_link = True

    if int(total_pages) > 0:

        countpagesstr = list()

        if (int(page) > 0):


            content += '<li><a href="{url}/1" title="First">&laquo;</a></li>'.format(url=url)  # first link
            previous_link = abs(1 - page)

            content += '<li><a href="{url}/{previous_link}" data-page="{previous_link}" title="Previous">&lt;</a></li>'.format(
                url=url, previous_link=previous_link)

            for c in range(1, int(total_pages + 1)):

                if (page != c):

                    content += '<li  class=""><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                      c=str(c))

                elif (page == c):
                    content += '<li  class="active"><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                            c=str(
                                                                                                                c))


                elif (page == total_pages):
                    content += '<li  class="active"><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                            c=str(
                                                                                                                c))

                else:
                    content += '<li  class="active"><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                            c=str(
                                                                                                                c))

        else:

            for c in range(1, int(total_pages + 1)):
                if (c == 1):

                    content += '<li  class="active"><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                            c=str(
                                                                                                                c))


                else:

                    content += '<li  class=""><a href="{url}/{c}" title="Page{c}">{c}</a></li>'.format(url=url,
                                                                                                      c=str(c))

        if (page < total_pages):
            next_link = int(page) + 1
            content += '<li><a href="{url}/{next_link}" title="Next">&gt;</a></li>'.format(url=url,
                                                                                          next_link=next_link)  # first link

            content += '<li><a href="{url}/{next_link}" data-page="{next_link}" title="Last">&raquo;</a></li>'. \
                format(url=url, next_link=next_link)

    content += '</ul>'
    if content is not None:
        return content

def strig_tag(raw_html):

    TAG = re.sub('<[^<]+?>', '', raw_html)
    return TAG

def limit_string(data = "", length = 10, readmore = ""):
    if data is not "":
        info = (data[:int(length)] + str(readmore)) if len(data) > int(length) else data
    else:
        info = ""
    return info

def numberformat(num = int):

    if(int(num)>1000000000):
        getcount = str(int(round((num/1000000000),)))+str('T')

    elif(num>1000000):
        getcount = str(int(round((num/1000000),1)))+str('M')

    elif(num>1000):
        getcount = str(int(round((num/1000),1)))+str('K')

    else:
        getcount = str(int(round((num/1),1)))
    return getcount


def humanbytes(B):
   #Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


def file_get_contents(self, filename, use_include_path=0, context=None, offset=-1, maxlen=-1):
    if (filename.find('://') > 0):
        ret = urllib2.urlopen(filename).read()
        if (offset > 0):
            ret = ret[offset:]
        if (maxlen > 0):
            ret = ret[:maxlen]
        return ret
    else:
        fp = open(filename, 'rb')
        try:
            if (offset > 0):
                fp.seek(offset)
            ret = fp.read(maxlen)
            return ret
        except Exception as err:
            log_msg.critical(err)
        finally:
            fp.close()