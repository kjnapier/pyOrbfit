import os
from setuptools import setup, Extension
import sys
import sysconfig
import glob

import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

suffix = sysconfig.get_config_var('EXT_SUFFIX')
if suffix is None:
    suffix = ".so"

extra_compile_args = ['-O3', '-fPIC', '-std=gnu++2a', '-march=native']

if sys.platform == 'darwin':
    from distutils import sysconfig
    vars = sysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-shared')
    extra_link_args = ['-Wl,-install_name,@rpath/_pyOrbfit' + suffix]
    extra_compile_args = ['-O3', '-fPIC', '-std=c99', '-march=native']
    

_pyOrbfit = Extension('_pyOrbfit',
                                sources=['src/pyOrbfit.i', 
                                         'src/fit_radec.c',
                                         'src/orbfit1.c', 
                                         'src/nrutil.c', 
                                         'src/ephem_earth.c', 
                                         'src/aeiderivs.c', 
                                         'src/gasdev.c', 
                                         'src/abg_to_xyz.c', 
                                         'src/gaussj.c',
                                         'src/orbfit2.c', 
                                         'src/mrqmin_orbit.c', 
                                         'src/abg_to_aei.c', 
                                         'src/ludcmp.c', 
                                         'src/dms.c', 
                                         'src/covsrt.c', 
                                         'src/ran1.c',  
                                         'src/lubksb.c', 
                                         'src/transforms.c', 
                                         'src/mrqcof_orbit.c'],
                                include_dirs=[numpy.get_include()],
                                language='c',
                                extra_compile_args=extra_compile_args,
                                extra_link_args=extra_link_args
                                )

data_files = []
dirs = ['pyOrbfit/data/*']
for dir in dirs:
   for filename in glob.glob(dir):
      if os.path.isfile(filename):
         data_files.append(filename)

setup(
    name='pyOrbfit',
    version='1.0.0',
    description='Orbit fitting.',
    author='Kevin J. Napier',
    author_email='kjnapier@umich.edu',
    packages=['pyOrbfit'],
    package_data={'pyOrbfit.data': ['*']}, 
    data_files=data_files,
    include_package_data=True,
    ext_modules=[_pyOrbfit],
    zip_safe=False
)