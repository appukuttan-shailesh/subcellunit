try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='subcellunit',
    version='0.1',
    author='Shailesh Appukuttan',
    author_email='shailesh.appukuttan@unic.cnrs-gif.fr',
    packages=['subcellunit',
              'subcellunit.capabilities',
              'subcellunit.tests',
              'subcellunit.scores',
              'subcellunit.plots'],
    url='https://github.com/appukuttan-shailesh/subcellunit',
    download_url = 'https://github.com/appukuttan-shailesh/morphounit/archive/0.2.tar.gz', 
    keywords = ['morphology', 'structure', 'circuit', 'testing', 'validation framework'],
    license='MIT',
    description='A SciUnit library for data-driven testing of subcellular features.',
    long_description="",
    install_requires=['neo','elephant','sciunit>=0.1.5.2',],
    dependency_links = ['git+http://github.com/neuralensemble/python-neo.git#egg=neo-0.4.0dev',
                        'https://github.com/scidash/sciunit/tarball/dev']
)
