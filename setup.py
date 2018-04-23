from setuptools import find_packages, setup

setup(
    name='urlargs',
    version='0.3',
    url='https://github.com/scampion/urlargs',
    license='BSD',
    author='Sebastien Campion',
    author_email='sebastien.campion@inria.fr',
    description='Notebook Extension to load url args in python environment',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
