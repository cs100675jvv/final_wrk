from setuptools import setup

setup(
    name='assistantbot',
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
        assistantbot=main:main
    ''',
    python_requires='>=3.0',
)
