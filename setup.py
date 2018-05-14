from setuptools import find_packages, setup

with open('lit/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='lit',
    version=version,
    description='Litecoin made easy.',
    long_description=open('README.rst', 'r').read(),
    author='yak',
    author_email='yak@fastmail.com',
    maintainer='yak',
    maintainer_email='yak@fastmail.com',
    url='https://github.com/blockterms/lit',
    download_url='https://github.com/blockterms/lit',
    license='MIT',

    keywords=(
        'litecoin',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
    ),

    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),

    install_requires=('coincurve>=4.3.0', 'requests'),
    extras_require={
        'cli': ('appdirs', 'click', 'privy', 'tinydb'),
        'cache': ('lmdb', ),
    },
    tests_require=['pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': (
            'lit = lit.cli:lit',
        ),
    },
)
