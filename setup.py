#!/usr/bin/env python
#
# #  ,ggg,         ,gg                              ,ggg, ,ggg,_,ggg,                                                     
# dP""Y8a       ,8P                ,dPYb,        dP""Y8dP""Y88P""Y8b                                               I8   
# Yb, `88       d8'                IP'`Yb        Yb, `88'  `88'  `88                                               I8   
#  `"  88       88                 I8  8I         `"  88    88    88                                            88888888
#      88       88                 I8  8'             88    88    88                                               I8   
#      I8       8I,ggg,   ,gggggg, I8 dP      ,gggg,gg88    88    88   ,gggg,gg  ,ggg,,ggg,   ,ggg,   ,ggg,,ggg,   I8   
#      `8,     ,8i8" "8i  dP""""8I I8dP   88gdP"  "Y8I88    88    88  dP"  "Y8I ,8" "8P" "8, i8" "8i ,8" "8P" "8,  I8   
#       Y8,   ,8PI8, ,8I ,8'    8I I8P    8Ii8'    ,8I88    88    88 i8'    ,8I I8   8I   8I I8, ,8I I8   8I   8I ,I8,  
#        Yb,_,dP `YbadP',dP     Y8,d8b,  ,8,d8,   ,d8b88    88    Y8,d8,   ,d8b,dP   8I   Yb,`YbadP',dP   8I   Yb,d88b, 
#         "Y8P" 888P"Y888P      `Y8P'"Y88P"P"Y8888P"`Y88    88    `YP"Y8888P"`Y8P'   8I   `Y888P"Y888P'   8I   `Y8P""Y8 
#
#                                                    VerbaManent tts

import os
import subprocess
import sys
from packaging.version import Version

import numpy
import setuptools.command.build_py
import setuptools.command.develop
#from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

python_version = sys.version.split()[0]
if Version(python_version) < Version("3.9"):
    raise RuntimeError("VerbaManent requires python >= 3.9" "but your Python version is {}".format(sys.version))


cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "VERSION")) as fin:
    version = fin.read().strip()


class build_py(setuptools.command.build_py.build_py):  # pylint: disable=too-many-ancestors
    def run(self):
        setuptools.command.build_py.build_py.run(self)


class develop(setuptools.command.develop.develop):
    def run(self):
        setuptools.command.develop.develop.run(self)


package_data = ["verbamanent/server/templates/*"]


def pip_install(package_name):
    subprocess.call([sys.executable, "-m", "pip", "install", package_name])


requirements = open(os.path.join(cwd, "requirements.txt"), "r").readlines()
with open(os.path.join(cwd, "requirements.notebooks.txt"), "r") as f:
    requirements_notebooks = f.readlines()
with open(os.path.join(cwd, "requirements.dev.txt"), "r") as f:
    requirements_dev = f.readlines()
with open(os.path.join(cwd, "requirements.ja.txt"), "r") as f:
    requirements_ja = f.readlines()
requirements_all = requirements_dev + requirements_notebooks + requirements_ja

with open("README.md", "r", encoding="utf-8") as readme_file:
    README = readme_file.read()

exts = [
    Extension(
        name="tts.tts.utils.monotonic_align.core",
        sources=["tts/tts/utils/monotonic_align/core.pyx"],
    )
]
setup(
    name="verbamanent",
    version=version,
    url="https://github.com/michele-giordano/verbamanent",
    author="Michele Giordano",
    description="VerbaManent - Advanced Text-to-Speech",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MPL-2.0",
    # cython
    #include_dirs=numpy.get_include(),
    #ext_modules=cythonize(exts, language_level=3),
    # ext_modules=find_cython_extensions(),
    # package
    include_package_data=True,
    packages=find_packages(where=".", include=["verbamanent","verbamanent.*"], exclude=["*.tests", "*tests.*", "tests.*", "*tests", "tests"]),
    package_data={
        "verbamanent": [
            "VERSION",
        ]
    },
    project_urls={
        "Documentation": "https://github.com/giordebug/verbamanent/wiki",
        "Repository": "https://github.com/giordebug/verbamanent",
    },
    cmdclass={
        "build_py": build_py,
        "develop": develop,
        # 'build_ext': build_ext
    },
    install_requires=requirements,
    extras_require={
        "all": requirements_all,
        "dev": requirements_dev,
        "notebooks": requirements_notebooks,
        "ja": requirements_ja,
    },
    python_requires=">=3.9.0",
    entry_points={"console_scripts": ["verbamanent=verbamanent.bin.synthesize:main", "verbamanent-server = verbamanent.server.server:main"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    zip_safe=False,
)

if __name__ == "__main__":
    pkgs = find_packages(where=".")
    print("Pacchetti trovati da setuptools:", pkgs)
