#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
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

import sys
import os

import gtk
import gtk.glade
import time 
import string
import shutil
import pygtk
import ConfigParser

app_name      = 'simpserial to get data from serial ports'
app_version   = 'unknown' # will be set in main() call
app_authors   = [ 'Fabian Affolter <fabian@bernewireless.net' ]
app_copyright = 'Copyright (c) 2009 Fabian Affolter'
app_website   = 'http://wiki.github.com/fabaff/simpserial'

glade_dir    =  '/usr/share/simpserial/'
icon_dir     =  '/usr/share/pysms/images/simpserial.png'
conf_dir     =   os.path.join( os.path.expanduser('~'), '.simpserial' )

settings     =   ConfigParser.ConfigParser()

class simpserial:
	"""This is the SimpSerial application"""
	
	def __init__( self ): 
		# Set the Glade file
		self.gladefile = os.path.join(glade_dir, 'simpserial.glade')
		self.wTree = gtk.glade.XML( self.gladefile, "mainWindow" ) 

		# Create our dictionary and connect it
        dic = { "on_mainWindow_destroy" :                  self.quit, 
                "on_quit_activate" :                       self.quit, 
                "on_import_activate" :                     self.on_import_activate, 
                "on_export_activate" :                     self.on_export_activate, 
                "on_cut_activate" :                        self.on_cut_activate, 
                "on_copy_activate" :                       self.on_copy_activate, 
                "on_paste_activate" :                      self.on_paste_activate, 
                "on_preferences_activate" :                self.on_preferences_activate, 
                "on_information_activate" :                self.on_information_activate, 
                "on_about_activate" :                      self.on_about_activate, 
                "on_key_press" :                           self.on_key_press, 
                "on_button_clear_clicked" :                self.on_button_clear_clicked, 
                "on_button_send_clicked" :                 self.on_button_send_clicked, 
                "on_button_addressbook_toggled" :          self.on_button_addressbook_toggled, 
                "on_button_add_addressbook_clicked":       self.on_button_add_addressbook_clicked, 
                "on_button_delete_addressbook_clicked":    self.on_button_delete_addressbook_clicked, 
                "on_treeview_addressbook_row_activated" :  self.on_addressbook_row_activated     
              }
        self.wTree.signal_autoconnect( dic )

        ## Check the user directory
        #if not os.path.isdir( conf_dir ):
            #os.mkdir( conf_dir )
        
        # Read the settings
        settings.read( settingsfile )
        
        # If the config file is non-existent, ConfigParser.read() simply
        # ignores it. So let's check if it has or sections or not
        if  settings.sections() == []:
            settings.add_section( 'Application' )
            settings.set( 'Application', 'last used', '0' )
            settings.set( 'Application', 'user number', '')
            settings.add_section( 'Providers' )
            settings.set( 'Providers', 'orange', ',' )
            settings.set( 'Providers', 'swisscom', ',' )
            settings.set( 'Providers', 'eth', ',' )
            settings.set( 'Providers', 'schoolnet', ',' )

        # Connect to widgets
        self.main_window = self.wTree.get_widget( "mainWindow" )
        self.msg = self.wTree.get_widget( "textview_message" )
        self.msgbuffer = self.msg.get_buffer()
        self.num_chars = self.wTree.get_widget( "label_numchars" )
        self.num_sms = self.wTree.get_widget( "label_numsms" )
        self.statusbar = self.wTree.get_widget( "statusbar" )
        self.progressbar = self.wTree.get_widget( "progressbar" )
        self.receivernumber = self.wTree.get_widget( "entry_receiver" )
        self.affirmation = self.wTree.get_widget( "check_confirmation" )
        self.cb_main = self.wTree.get_widget( "combo_mainprovider" )
        self.addressbook = self.wTree.get_widget( "hbox_addressbook" )
        self.button_addressbook = self.wTree.get_widget( "button_addressbook" )
        

	#def quit( self, *args ):
		## Save settings   
		#sfile = open( settingsfile, 'w' )
		#settings.write( sfile )
		#sfile.close()

        
        #print "Exit now ..."
        #gtk.main_quit()


	#def set_icon( self ):
		#icon = self.get_icon('simpserial')
		#self.main_window.set_icon( icon )

    #def get_icon( self, entry, size=24 ):
        #path = icon_dir
        #if path == None:
            #pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, size, size)
            #pb.fill(0x00000000)
        #else:
            #try:
                #pb = gtk.gdk.pixbuf_new_from_file_at_size(path, size, size)
            #except:
                #pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, size, size)
                #pb.fill(0x00000000)
        #return pb


def main( __version__ = None ):
    global app_version
    
    app_version = __version__
    simpserial = simpSerial()

    simpserial.set_icon()
    gtk.main()

#if __name__ == "__main__":
    #print _("Please do not call simpserial.py directly. Instead, call the simpserial binary.")
    #sys.exit( -1)
