from setuptools import setup, find_packages
from os import path, remove
from setuptools import setup
from setuptools.command.install import install
import bz2
from indian_pincode_details import __version__

DESCRIPTION = "A package for retrieving a list of details based on a given pincode."


root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, "README.md")) as f:
    long_description = f.read()


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def decompress(self):
        source_file = 'indian_pincode_details/pincodes.bz2'
        destination_file = 'indian_pincode_details/pincodes.json'
        tarbz2contents = bz2.decompress(open(source_file, 'rb').read())
        fh = open(destination_file, "wb")
        fh.write(tarbz2contents)
        fh.close()

    def run(self):
        install.run(self)

        self.decompress()


setup(
    name="indian_pincode_details",
    version=__version__,
    url="https://github.com/kpsaurus/indian-pincode-details/",
    author="Krishna Prasad K",
    author_email="contact@kprasad.dev",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    keywords=[
        "python",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
