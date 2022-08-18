README
======

This is Asus Python GPIO python library for Tinkerboards. It is a fork of https://github.com/TinkerBoard/gpio_lib_python.git that uses poetry project manager and has been modified to recognise the Tinker Board S R2.0.

Build
-----

.. code-block:: console

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
   $ sudo wget -P /usr/local/share/ca-certificates/cacert.org http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt
   $ sudo update-ca-certificates
   $ curl https://sh.rustup.rs -sSf | sh
   # This is an interactive installer and will download and install all the necessary rust packages.
   # Set your PATH to point to the installed rustc binary.
   $ curl -sSL https://install.python-poetry.org | python3 -

More Informaion
---------------

Send an email to scorpio_chang@asus.com

The poetry fork was created by kwrazi@gmailcom

