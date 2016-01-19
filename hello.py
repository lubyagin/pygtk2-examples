# -*- coding: utf-8 -*-
# Examples:
# C:\Python27\Lib\site-packages\gtk-2.0\tests\pygtk\
# http://www.pygtk.org/pygtk2tutorial/examples/helloworld.py
# GTK2 Downloads:
# http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.24/pygtk-all-in-one-2.24.2.win32-py2.7.msi

import pygtk
pygtk.require('2.0')
import gobject

import atk
import pango
import gtk
import gtk.gdk

try:
    import gtk.glade
except ImportError:
    print ('* gtk.glade is not available.')

gobject.threads_init()

class HelloWorld:

  def destroy(self, widget, data=None):
    print "destroy signal occurred"
    gtk.main_quit()

  def __init__(self):
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.connect("destroy", self.destroy)
    self.window.set_border_width(10)
    self.button = gtk.Button("Hello World")
    self.window.add(self.button)
    self.button.show()
    self.window.show()

  def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
    gtk.main()

if __name__ == "__main__":
  hello = HelloWorld()
  hello.main()
