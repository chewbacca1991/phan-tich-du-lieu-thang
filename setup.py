from setuptools import setup

setup(
    name='phan-tich-du-lieu-thang',
    version='0.1',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-Cors',
        'pandas',
        'matplotlib',
        'reportlab',
    ],
    author='Your Name',  # Add your name as the package author
    description='A package for monthly data analysis'  # Provide a short description of the package
)
