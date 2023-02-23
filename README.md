# Calix AP Network Scheduler 

### Supported (tested) systems
* Calix router running EXOS 
* Mac
* Linux

```text
This script can be installed on your system and run from crontab.
Just make sure to specify the full path to the script or add the
path location to the PATH env.
```

### Basic crontab configuration
```sh 
PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/Users/DevGW/bin
0 0 * * 1-5 apToggleControl.py > /dev/null 2>&1
0 10 * * 1-5 apToggleControl.py > /dev/null 2>&1
```