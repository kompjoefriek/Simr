# Simr [![Build Status](https://app.travis-ci.com/kompjoefriek/Simr.svg?branch=master)](https://app.travis-ci.com/github/kompjoefriek/Simr) [![codecov](https://codecov.io/gh/kompjoefriek/Simr/branch/master/graph/badge.svg)](https://codecov.io/gh/kompjoefriek/Simr) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkompjoefriek%2FSimr.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkompjoefriek%2FSimr?ref=badge_shield)


Simr is a simulation runner written in Python 3, but is backwards compatible with Python 2 (see Travis-ci build status).

### Dependencies  
- [psutil](https://pypi.org/project/psutil/)
- [windows_curses](https://pypi.org/project/windows-curses/)

### Examples  
![example 1](github/Simr_1.png)

![example 2](github/Simr_2.png)

### Predefined variables:

- **%DATE%** Date when Simr started in format: %Y%m%d (e.g. 20170420)
- **%TIME%** Time when Simr started in format: %H%M%S (e.g. 163058)

For format details, see [time.strftime](https://docs.python.org/2/library/time.html#time.strftime)

### Todo  
- [ ] Custom priority of process?
- [ ] Interactive interface? (see curses branch)
- [ ] Custom Date or Time format?


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkompjoefriek%2FSimr.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkompjoefriek%2FSimr?ref=badge_large)