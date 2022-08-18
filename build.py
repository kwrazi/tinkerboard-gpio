import os
import shutil
from distutils.command.build_ext import build_ext
from distutils.core import Distribution, Extension
from distutils.errors import (
    CCompilerError,
    DistutilsExecError,
    DistutilsPlatformError,
)


ext_modules = [
    Extension('ASUS.GPIO',
              sources=[
                'src/py_gpio.c', 
                'src/c_gpio.c',
                'src/cpuinfo.c',
                'src/event_gpio.c',
                'src/soft_pwm.c',
                'src/py_pwm.c',
                'src/common.c',
                'src/constants.c',
                'src/wiringTB.c'],
              include_dirs=['src/',],
              libraries=["m"],
              ),
]

class BuildFailed(Exception):
    pass

class ExtBuilder(build_ext):

    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise BuildFailed('File not found. Could not compile C extension.')

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            raise BuildFailed('Could not compile C extension.')
        
def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    setup_kwargs.update(
        {"ext_modules": ext_modules, 
         "cmdclass": {"build_ext": ExtBuilder}}
    )

if __name__ == '__main__':
    build({})
