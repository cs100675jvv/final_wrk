from setuptools import setup

setup(
    name='assistantbot',
    version='0.0.1',
    packages=[
        '_classes',
        '_function',
        '_decorator',
    ],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        assistantbot=main:main
    ''',
    python_requires='>=3.0',
)
