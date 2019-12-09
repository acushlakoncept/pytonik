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
Download file Structure [Folder-Structure](https://github.com/pytonik/Folder-Structure)

### How to get started
once the file structure is created. follow the file structure above or download [Folder-Structure](https://github.com/pytonik/Folder-Structure)
create a file with a name **.htaccess**
write the below code sample

```
<IfModule mod_rewrite.c>
RewriteEngine on
RewriteRule ^$ public/
RewriteRule (.*) public/$1 [NC,L]
AddHandler cgi-script .cgi .py
Options +ExecCGI
</IfModule>
````

create a file with a name **.env** to learn how about the **.env** file check [pytonik-env]((https://github.com/pytonik/.env)
write the below code sample

```
{'route':
        {
        'default': '',
        },
'dbConnect':
         {
              'host': 'localhost',
              'database': 'pytonik-database',
              'password': 'database-password',
              'username': 'database-username',
              'port': 'database-port',
              'driver': 'MYSQLi'
         },
'languages':
{
   'en': '',
   'fr': '',
   'ef': '',
},
'SMTP':
{
    'server':   'test@server.com',
    'port':     '25',
    'username': 'test@example.com',
    'password': 'testpassword',
},
'default_actions': 'index',
'default_controllers' :'index',
'default_routes' :'index',
'default_languages':'en'
}

```

create a folder with a name **public** inside the folder, create a file with a name **index.py**
write the below code sample

```
#!/usr/local/bin/python

try:
    from pytonik import Web
except Exception as err:
    exit(err)

App = Web.App()
App.runs()
```

Inside public folder, create a file with a name **.htaccess** file 
write the below code sample
```
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.py/$1 [L]
</IfModule>
```
create a file with a name **IndexController.py** inside **Controller** folder, this will serve as a default controller. 
create a file with a name **homepage.html** inside **views** folder, views folder is were all html template will be reserved and called from.
write the below code sample

```
from pytonik import Web
m = Web.App()
def index():
    data = {
        'title': "Home",
  
    }
    m.header()
    m.views('homepage', data)
```

Learn how to use attribute tags and types in Pytonik Template Engine [Template Engine](https://github.com/pytonik/pytonik_template_engine)

Learn more on how to use pytonik MVC [MYSQL Helper](https://github.com/pytonik/pytonik_mysql_helper)

You can accomplish any task with pytonik. 
All python files (.py extension) permission should always be set to **755**

Download sample file on how to start at [SampleFolder](https://github.com/betacodings/SampleFolder)

## Contact Information: 

**Name:**  pytonik MVC

**Email:** pytonikmvc@gmail.com



Donate to support our effort while waiting for great release of pytonik framework:



Bitcoin: **3Cz8J1tvLgvGmPLPcK4XwNckruEsCvCCgX**

Litecoin: **MR9gAfzeDjTxpiNro7u2yYZasdc57oiDrY**

Bitcoin Cash: **qzaau9hu0vhjjnzu8hqjpedeemeysurqdczsk3w4kx**

Ethereum: **0xd8443c569427fBaaDb1c055ACd26b31F8a944e01**


