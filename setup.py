import setuptools

setuptools.setup(
    name="ModuleUltra",
    version="0.1.0",
    url="https://github.com/dcdanko/ModuleUltra",

    author="David C. Danko",
    author_email="dcdanko@gmail.com",

    description="Tools to make pipelines easier to run and distribute for large biological datasets",
    long_description=open('README.rst').read(),

    packages=['moduleultra'],
    package_dir={'moduleultra': 'moduleultra'},

    install_requires=[
        'click==6.7',
    ],

    entry_points={
        'console_scripts': [
            'moduleultra=moduleultra.cli:main'
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
