import fabric.api as fa
import fabric.contrib as fc
import fabric.operations as fo
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

def scan_from_remote(resolution=300, color='Color', img_format='tiff',
                     destination=os.path.join(os.environ['HOME'], 'Downloads')):
    """
    Scans a file from a scanner attachd to the server. 

    The scan is initiated by the client. Saves the file on the client machine.

    Keyword Parameters
    ----------
    resolution: int or str
        The resolution at which we scan the image. This can be 'auto', 150, 300,
        or 600. By default it is at 300.

    color: str
        Whether we scan in color or in grayscale. The possible choices are
        'auto', 'Color', or 'Gray'.

    img_format: str
        Whether we format the resulting picture in pnm or tiff. The only options
        are therefore logically 'pnm' or 'tiff'.

    destination :str
        Where we plan to store the scanned image on our local machine.
    """
    if fc.files.exists(cs.temp_storage):
        pass
    else:
        fa.run('mkdir ' + cs.temp_storage)

    img_path = os.path.join(cs.temp_storage, 'img.{0}'.format(img_format))
    fa.run('scanimage --resolution {0} --mode {1} --format {2} > {3}'.
           format(resolution, color, img_format, img_path))

    if os.path.isdir(destination):
        destination_file = os.path.join(destination, 
                                        'img.{0}'.format(img_format))
        nonconflict_destination = find_nonconflicting_name(destination_file)
    else:
        nonconflict_destination = find_nonconflicting_name(destination)

    print(destination)
    print(nonconflict_destination)
    fo.get(img_path, nonconflict_destination)
    fa.run('rm ' + img_path)

def find_nonconflicting_name(filename, counter=0):
    """
    Append a number as large as necessary to a filename in order to make sure
    that this filename does not conflict with any other files.
    """
    filename_parts = filename.split('.')
    try_nonconflicting_name = (filename_parts[0] + str(counter) + '.' +
                               '.'.join(filename_parts[1:]))

    if not os.path.isfile(filename):
        return filename
    elif not os.path.isfile(try_nonconflicting_name):
        return try_nonconflicting_name
    else:
        return find_nonconflicting_name(filename, counter + 1)

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
