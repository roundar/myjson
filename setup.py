from distutils.core import setup

setup(
    name='myjson',
    version='1.1.0',
    description='API wrapper for myjson',
    url='https://github.com/roundar/myjson',
    download_url='https://github.com/roundar/myjson/archive/v1.1.0.tar.gz',
    packages=['myjson'],
    license='WTFPL',
    author='roundar',
    author_email='roundar.github@gmail.com',
    include_package_data=True,
    zip_safe=False,
    keywords=['json', 'myjson', 'hosted'],
    entry_points={
        'console_scripts': [
            'myjson = myjson.__main__:main',
        ]
    },
)