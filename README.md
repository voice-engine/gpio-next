GPIO NEXT
=========
[![](https://img.shields.io/pypi/v/gpio-next.svg)](https://pypi.org/project/gpio-next/)


This is a python ctypes binding for [libgpiod](https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/).

It's time to switch from the GPIO sysfs interface to gpiod to the linux GPIO character device (gpiod, stands for GPIO device)

>Since linux 4.8 the GPIO sysfs interface is deprecated. User space should use
the character device instead. This library encapsulates the ioctl calls and
data structures behind a straightforward API.

from [kernel.org](https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/)

## Requirements
+ libgpiod1

## Install
```
sudo apt install libgpiod1
pip install gpio-next
```


## Usage
1. turn on/off an LED

```python
import time
from gpio_next import Output

LED = Output(64, default_value=0)
for i in range(10):
    LED.write(i & 1)
    time.sleep(1)
```

2. detect button events

```python
from gpio_next import Input

button = Input(203)

for i in range(10):
    print(button.wait())
    print(button.read())
```
