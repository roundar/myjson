from distutils.core import setup

setup(
    name='myjson',
    version='0.0.1',
    url='https://github.com/roundar/myjson',
    packages=['myjson'],
    license='WTFPL',
    author='roundar',
    author_email='roundar.github@gmail.com',
    description='API wrapper for myjson',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'myjson = myjson.__main__:main',
        ]
    },
)