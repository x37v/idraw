'''
Automatically generated dumb wrapper to call axidrawinternal.axidraw_svg_reorder.axidraw_svg_reorder as an inkscape extension.
To regenerate, run python bin/generatewrappers.py
'''
import logging

from lxml import etree

from plot_utils_import import from_dependency_import
axidraw_svg_reorder = from_dependency_import('axidrawinternal.axidraw_svg_reorder')
exit_status = from_dependency_import('ink_extensions_utils.exit_status')
message = from_dependency_import('ink_extensions_utils.message')

root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)
root_logger.addHandler(message.UserMessageHandler()) # to stderr/inkscape "has received additional data" window
# consider adding a handler to send logs to extension-errors.log?

if __name__ == '__main__':
    conf = None
    e = None # effect
    try:
        from importlib import import_module
        conf = import_module("notamodule")
        e = axidraw_svg_reorder.ReorderEffect(params=conf, default_logging=False)
    except ImportError as ie:
        if "notamodule" == "notamodule":
            # assuming everything is going well, this just means there is no config or logging assigned in the generatewrappers.py script
            e = axidraw_svg_reorder.ReorderEffect()
        else:
            raise
    exit_status.run(e.affect)
