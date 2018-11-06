
# coding: utf-8

#!/usr/bin/env python
from setuptools import setup

#import sys
import versioneer


DISTNAME = 'QPlot'
DESCRIPTION = "Quantamatics,Inc Port for Plotly"
LONG_DESCRIPTION = """NA"""
MAINTAINER = 'Quantamatics,Inc'
AUTHOR = 'Quantamatics Inc'
AUTHOR_EMAIL = 'mshaalan@quantamatics.com'
URL = "https://github.com/Quantamatics/QPlot/"
LICENSE = "NA"

#VERSION = "0.0.10"


packages=['plotly',
          'plotly/api',
          'plotly/api/v1',
          'plotly/api/v2',
          'plotly/dashboard_objs',
          'plotly/plotly',
          'plotly/plotly/chunked_requests',
          'plotly/figure_factory',
          'plotly/graph_objs',
          'plotly/grid_objs',
          'plotly/widgets',
          'plotly/offline',
          'plotly/matplotlylib',
          'plotly/matplotlylib/mplexporter',
          'plotly/matplotlylib/mplexporter/renderers']

package_data={'plotly': ['package_data/*']}

classifiers = ['Development Status :: 4 - Beta',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Intended Audience :: Science/Research',
               'Topic :: Scientific/Engineering :: Mathematics',
               'Operating System :: OS Independent']

install_reqs = [
    'ipython>=3.2.3',
    'numpy>=1.8.0',
    'pandas>=0.18.0, <0.20.0',
    'scipy>=0.17.0',
    'configparser>=3.0.0',
    'python-dateutil>=2.6.0',
    'pydatastream>=0.4.6',
    'pymssql>=2.1.3',
    'sqlalchemy>=1.0.17',
#    'versioneer>=0.18'

# plotly requires as follow
    'decorator>=4.0.6',
    'nbformat>=4.2',
    'pytz',
    'requests',
    'six',
    'uuid']




if __name__ == "__main__":
    
    setup(
        name=DISTNAME,
#        version=VERSION,
#       Versioneer
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
#    
        maintainer=MAINTAINER,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        long_description=LONG_DESCRIPTION,
        packages=packages,
        package_data=package_data,
        classifiers=classifiers,
        install_requires=install_reqs
    )

