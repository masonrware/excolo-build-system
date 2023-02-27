from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules = cythonize("excolo.pyx", 
                            language_level=3,
                            build_dir="build")
)

