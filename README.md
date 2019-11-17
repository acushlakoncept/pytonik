# pytonik

[![Build Status](https://img.shields.io/pypi/v/pytonik)](https://pypi.python.org/pypi/pytonik)
[![Downloads](https://img.shields.io/pypi/dm/pytonik)](https://pypi.python.org/pypi/pytonik/)
[![Wheel](https://img.shields.io/pypi/wheel/pytonik.svg)](https://pypi.python.org/pypi/pytonik)
[![Python Version](https://img.shields.io/pypi/pyversions/pytonik)](https://pypi.python.org/pypi/pytonik)
[![License](https://img.shields.io/pypi/l/pytonik)](https://pypi.python.org/pypi/pytonik)

Model View Controller in Python
It is easy to use with an oop(Object Oriented Programming) Pattern.
It runs on multiple servers such as WINDOWS, MAC OS, LINUX.

[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://pypi.python.org/pypi/pytonik)

## How to setup
if you are running a local machine you will need to install either, wamp, xampp, lamp or mamp. 
Enable CGI on your httpd.conf file as follows:
```
<Directory "/var/www/cgi-bin">
   AllowOverride None
   Options ExecCGI
   Order allow, deny
   Allow from all
</Directory>

<Directory "/var/www/cgi-bin">
Options All
</Directory>
```


## How to install

We recommend you to install this MVC package using Command Line
```
$ pip install pytonik
```

You have to set the app file structures to be able to start your web application.
Below are the file structures:

```
 |─MypytonikFolder                            application folder 
 	|─controller
		|─ IndexController.py 
 	|─ lang
		|─ en.py
 	|─ model
 	|─ public  
		|─ asset
 	|─ views                                   
		|─ Includefolder
			|─ header.html
		|─ 404.html
		|─ page.html
│      .env
│      .htaccess


```
Download sample file on how to start at [SampleFolder](https://github.com/pytonik/SampleFolder)

You can accomplish any task with pytonik. 
All python files (.py extension) permission should always be set to **755**

## Contact Information: 

**Name:**  pytonik MVC

**Email:** pytonikmvc@gmail.com



Donate to support our effort while waiting for great release of pytonik framework:



Bitcoin: **3Cz8J1tvLgvGmPLPcK4XwNckruEsCvCCgX**

Litecoin: **MR9gAfzeDjTxpiNro7u2yYZasdc57oiDrY**

Bitcoin Cash: **qzaau9hu0vhjjnzu8hqjpedeemeysurqdczsk3w4kx**

Ethereum: **0xd8443c569427fBaaDb1c055ACd26b31F8a944e01**


