# Postr, a Flickr Uploader
#
# Copyright (C) 2006-2008 Ross Burton <ross@burtonini.com>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301 USA

import gtk
from gettext import gettext as _

class ErrorDialog(gtk.MessageDialog):
    def __init__(self, parent=None):
        gtk.MessageDialog.__init__(self, flags=gtk.DIALOG_DESTROY_WITH_PARENT,
                                   type=gtk.MESSAGE_ERROR,
                                   buttons=gtk.BUTTONS_OK,
                                   parent=parent,
                                   message_format=_("An error occurred"))
        self.connect("response", lambda dialog, response: dialog.destroy())

    def set_from_failure (self, failure):
        print failure
        # TODO: format nicer
        self.format_secondary_text (str (failure.value))

    def set_from_exception (self, exception):
        print exception
        # TODO: format nicer
        self.format_secondary_text (str (exception))

    def set_from_string(self, message):
        # TODO: format nicer
        self.format_secondary_text (message)
