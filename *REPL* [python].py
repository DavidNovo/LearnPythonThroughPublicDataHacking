Python 2.7.6 (default, Sep  9 2014, 15:04:36) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> X = '43'
>>> Y = 12
>>> X + Y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> int(X)
43
>>> X + Y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> INT(X) + Y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'INT' is not defined
>>> int(X) + Y
55
>>> import urllib
>>> u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
>>> data = u.read()
>>> f =open('rt22.xml','wb')
>>> f.write(data)
>>> f.close()
>>> 
>>> 5 + 6
11
>>> 