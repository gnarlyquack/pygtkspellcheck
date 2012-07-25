# -*- coding:utf-8 -*-
#
# Copyright (C) 2012, Maximilian Köhl <linuxmaxi@googlemail.com>
# Copyright (C) 2012, Carlos Jenkins <carlos@jenkins.co.cr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from distutils.core import setup

try:
    from sphinx.setup_command import BuildDoc
    cmdclass = {'build_sphinx': BuildDoc}
except ImportError as e:
    print(e)
    print('Unable to import Sphinx custom command. Documentation build will ' +
          'be unavailable. Install python-sphinx to solve this.')
    cmdclass = {}

sys.path.append('./src/')
import gtkspellcheck as m

setup(name=m.__short_name__,
      version=m.__version__,
      description=m.__desc_long__,
      long_description=m.__desc_long__,
      author=m.__authors__,
      author_email=m.__emails__,
      url=m.__website__,
      license='GPLv3+',
      package_dir={'': 'src'},
      packages=['gtkspellcheck', 'pylocales'],
      package_data={'pylocales' : ['locales.db']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: X11 Applications :: Gnome',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: MacOS :: MacOS X', # Should work on MacOS X I think...
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Localization'],
      cmdclass=cmdclass)