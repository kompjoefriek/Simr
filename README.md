# Simr


Simr is a simulation runner written in Python 3

### Dependencies  
- [psutil](https://pythonhosted.org/psutil/)

#### Windows only!  
- [\_curses](http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses)

#### Note:  
64bit installer will probably not find your 64bit python install !  
Use the 32bit installers, or execute the following command as administrator instead:
```
reg copy HKLM\SOFTWARE\Python HKLM\SOFTWARE\Wow6432Node\Python /s
```

### Examples  
![example 1](github/Simr_1.png)

![example 2](github/Simr_2.png)

### Todo  
- Custom priority of process?
- Interactive interface? (see curses branch)