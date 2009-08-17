#!/usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of simpserial.
#
# simpserial - A very simple tool to get data from serial ports
# Copyright (c) 2009 Fabian Affolter <fabian@bernewireless.net>
#
# simpserial is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# simpserial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import glob
import os
from distutils.core import setup

# read the version from the pysms main program
simpserial_version = os.popen( "cat bin/simpserial |grep ^__version__.*=|cut -d\\\" -f2").read().strip()

# files to install
inst_images   = [ 'data/simpserial.png' ]
inst_icons    = [ 'data/simpserial_icon.png' ]
inst_share    = [ 'data/simpserial.glade' ]
inst_menu     = [ 'data/simpserial.desktop' ]

data_files = [
  ('share/simpserial/images',   inst_images),
  ('share/simpserial',          inst_share),
  ('share/applications',   inst_menu),
  ('share/pixmaps',        inst_icons),
]

setup(
        name             = 'simpserial',
        version          = simpserial_version,
        description      = 'A very simple tool to get data from serial ports.',
        author           = 'Fabian Affolter',
        author_email     = 'fabian@bernewireless.net',
        url              = 'http://wiki.github.com/fabaff/simpserial',
        license          = 'GPLv3+',

        package_dir      = { '': 'src' },
        packages         = [ 'simpserial' ],

        scripts          = [ 'bin/simpserial' ],
        data_files       = data_files
     )
     
     
