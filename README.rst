README
======

This is Asus Python GPIO python library for Tinkerboards. It is a fork of https://github.com/TinkerBoard/gpio_lib_python.git that uses poetry project manager and has been modified to recognise the Tinker Board S R2.0.

Build
-----

.. code-block:: console

   $ poetry build

The wheel package inside ``dist`` directory should have been created and can be installed using pip.

Simple Python Program
---------------------

.. code-block:: python

   import ASUS.GPIO as GPIO
   
   GPIO.setmode(GPIO.ASUS)
   GPIO.setup(17, GPIO.OUT)
   GPIO.output(17, GPIO.HIGH)

More Informaion
---------------

Send an email to scorpio_chang@asus.com
