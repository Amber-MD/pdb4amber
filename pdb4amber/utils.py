import os
import subprocess
from contextlib import contextmanager
import tempfile
from shutil import rmtree


def easy_call(command, *args, **kwargs):
    try:
        output = subprocess.check_output(
            command, *args, stderr=subprocess.STDOUT, **kwargs)
        return output.decode()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.output.decode())


@contextmanager
def tempfolder():
    """run everything in temp folder
  """
    my_temp = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(my_temp)
    yield
    os.chdir(cwd)
    rmtree(my_temp)


def amberbin(program_str):
    amberhome = os.environ.get('AMBERHOME', '')
    program = os.path.join(amberhome, 'bin', program_str)
    if os.path.exists(program):
        return program
    else:
        return ''


def which(program):
    from distutils.spawn import find_executable
    return find_executable(program)


def get_amber_compatible_resnames():
    import parmed as pmd

    amberhome = os.getenv('AMBERHOME')
    if amberhome is None:
        return set()
    else:
        lib_dir = os.path.join(amberhome, 'dat', 'leap', 'lib')
        lib_files = ['RNA.lib']

        residue_set = set()
        for fname in lib_files:
            abs_fname = os.path.join(lib_dir, fname)
            if os.path.exists(abs_fname):
                residue_set.update(set(pmd.load_file(abs_fname)))
        return residue_set
