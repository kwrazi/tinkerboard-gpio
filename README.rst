README
======

This is a Python GPIO library for Asus Tinkerboards. 

It is a fork of https://github.com/TinkerBoard/gpio_lib_python.git that uses poetry project manager and has been modified to recognise the Tinker Board S R2.0.

This package provides a class to control the GPIO on a ASUS.

Note that this module is unsuitable for real-time or timing critical applications.  This is because you
can not predict when Python will be busy garbage collecting.  It also runs under the Linux kernel which
is not suitable for real time applications - it is multitasking O/S and another process may be given
priority over the CPU, causing jitter in your program.  If you are after true real-time performance and
predictability, buy yourself an Arduino http://www.arduino.cc !

Note that the current release does not support SPI, I2C, hardware PWM or serial functionality on 
the ASUS yet.
This is planned for the near future - watch this space!  One-wire functionality is also planned.

Although hardware PWM is not available yet, software PWM is available to use on all channels.

For examples and documentation, visit http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

Build
-----

.. code-block:: console

   $ sudo apt-get install python-dev python2.7-dev python3-dev
   $ poetry build

The wheel package inside ``dist`` directory should have been created and can be installed using pip.

.. code-block:: console

   $ python3 -m pip install dist/inkerboard_gpio-0.1.0-*.whl

Simple Python Program
---------------------

.. code-block:: python

   import ASUS.GPIO as GPIO
   
   GPIO.setmode(GPIO.ASUS)
   GPIO.setup(17, GPIO.OUT)
   GPIO.output(17, GPIO.HIGH)

Issues
------

Out-dated CA Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~

Poetry isn't available on Tinkerboard's default apt repositories so you will need to install it as described in https://python-poetry.org/docs/master/. However, the curl command may fail since the ca-certificates installed on Linaro are too old and will need updating. To update, you will need to run ``update-ca-certificates`` as no new dpkg is available. This will fail due to the old certificates. Hence, to install

.. code-block:: console

   $ sudo mkdir -pv /usr/local/share/ca-certificates/cacert.org
   $ sudo wget -P /usr/local/share/ca-certificates/cacert.org \
       http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt
   $ sudo update-ca-certificates
   $ curl https://sh.rustup.rs -sSf | sh
   # This is an interactive installer and will download and install all the necessary rust packages.
   # Set your PATH to point to the installed rustc binary.
   $ curl -sSL https://install.python-poetry.org | python3 -

More Informaion
---------------

Send an email to scorpio_chang@asus.com

The poetry fork was created by kwrazi@gmailcom

