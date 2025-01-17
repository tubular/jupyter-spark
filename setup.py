from setuptools import find_packages, setup

setup(
    name='jupyter-spark',
    version='0.4.0-dev1',
    setup_requires=['setuptools_scm'],
    description='Jupyter Notebook extension for Apache Spark integration',
    author='Mozilla Firefox Data Platform',
    author_email='fx-data-platform@mozilla.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='MPL2',
    install_requires=[
        'ipython >= 4',
        'jupyter',
        'notebook >= 4.2',
        'beautifulsoup4',
        'widgetsnbextension',
    ],
    url='https://github.com/mozilla/jupyter-spark',
    zip_safe=False,
)
