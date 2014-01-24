import fabric.api as fa
import fabric.contrib as fc
import os
import shutil
try:
    import custom_settings as cs
except ImportError:
    setup_settings()
    import custom_settings as cs

fa.env.hosts = [cs.host]
fa.env.user = cs.user

def print2remote(inputfile):
    """
    Prints a file on the client machine from the server

    Parameters
    ----------
    inputfile: str
        The local filename of the file which is to be printed
    """
    if fc.files.exists(cs.temp_storage):
        pass
    else:
        fa.run('mkdir ' + cs.temp_storage)
    fa.put(inputfile, cs.temp_storage)
    inputfile_base = os.path.basename(inputfile)
    fa.run('lpr ' + os.path.join(cs.temp_storage, inputfile_base))
    fa.run('rm ' + os.path.join(cs.temp_storage, inputfile_base))

def scan_from_remote(inputfile):
    """
    Scans a file from a scanner attachd to the server. 

    The scan is initiated by the client. Saves the file on the client machine.

    Parameters
    ----------
    inputfile: str
        The local (to the client) filename of the file which is produced by the
        scanner
    """
    return

def setup_settings():
    """
    Copies the default_settings.py file to the current directory
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    default_settings_path = os.path.join(current_dir, 
                                         'config/default_settings.py')
    custom_settings_path = os.path.join(current_dir,
                                        'custom_settings.py')
    shutil.copy(default_settings_path, custom_settings_path)
