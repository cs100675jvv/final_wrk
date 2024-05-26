from setuptools import setup

setup(
    name='catdog-bot',
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'click',
        'rich',
        'pycryptodome',
        'prompt_toolkit'
    ],
    packages=[
        '_classes',
        '_function',
        '_decorator'

    ],
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        catdog-bot=main:main
    ''',
    python_requires='>=3.0',
)
