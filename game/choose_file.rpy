# Copyright 2004-2019 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

init python:

    try:
        import _renpytfd
    except Exception:
        _renpytfd = None

    def choose_file(path):
        """
        Pops up a file chooser.
        """

        if path:
            default_path = path
            path = None
        else:
            try:
                default_path = os.path.dirname(os.path.abspath(config.renpy_base))
            except:
                default_path = os.path.abspath(config.renpy_base)

        if _renpytfd:
           path = _renpytfd.openFileDialog(
               __("Select message catalog"),
               default_path,
               ["*.po *.mo"],
               __("Message Catalogs (*.po,*.mo)"),
               False,
           )
        is_default = False

        # Path being None or "" means nothing was selected.
        if not path:
            path = None
        else:
            path = renpy.fsdecode(path)

        return path
