#!/usr/bin/env python

from distutils.core import setup
from distutils.command.sdist import sdist
from distutils.command.install_data import install_data
from distutils.command.build_scripts import build_scripts
from glob import glob
import os

########################################################################
# Had to overwrite the prunefile_list method of sdist to not
# remove automatically the RCS/CVS directory from the distribution.
########################################################################

class modified_sdist(sdist):
    def prune_file_list(self):
        """
        Prune off branches that might slip into the file list as created
        by 'read_template()', but really don't belong there:
          * the build tree (typically 'build')
          * the release tree itself (only an issue if we ran 'sdist
            previously with --keep-temp, or it aborted)
        """
        build = self.get_finalized_command('build')
        base_dir = self.distribution.get_fullname()
        self.filelist.exclude_pattern(None, prefix=build.build_base)
        self.filelist.exclude_pattern(None, prefix=base_dir)

class modified_install_data(install_data):

    def run(self):
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)
    
class modified_build_scripts(build_scripts):
    
    def copy_scripts(self):
        #print "scripts:" , self.scripts
        ## copy runPmv.py to runPmv, inserting "#!python" line at the beginning 
        for script in self.scripts:
            fnew = open(script, "w")
            forig = open(script+".py", "r")
            txt = forig.readlines()
            forig.close()
            fnew.write("#!/usr/bin/env python2.4\n")
            fnew.writelines(txt)
            fnew.close()
        build_scripts.copy_scripts(self)

        
########################################################################
# list of the python packages to be included in this distribution.
# sdist doesn't go recursively into subpackages so they need to be
# explicitaly listed.
# From these packages only the python modules will be taken
packages = ['Pmv', 'Pmv/Tests','Pmv/VisionInterface',
            'Pmv/Icons', 'Pmv/Tests/Data', 'Pmv/doc',
            'Pmv/VisionInterface/Tests',
            'Pmv/VisionInterface/Tests/Data',
            'Pmv/Tests/Data/clouds',
            'Pmv/scenarioInterface',
            'Pmv/scenarioInterface/Tests',
            'Pmv/hostappInterface',
            'Pmv/hostappInterface/Chimera',
            'Pmv/hostappInterface/Template',
            'Pmv/hostappInterface/cinema4d_dev',
            'Pmv/hostappInterface/cinema4d_dev/plugin',
            'Pmv/hostappInterface/blender',
            'Pmv/hostappInterface/blender/plugin',
            'Pmv/hostappInterface/blender/test',
            'Pmv/hostappInterface/demo',
            'Pmv/hostappInterface/cinema4d',
            'Pmv/hostappInterface/cinema4d/plugin',
            'Pmv/hostappInterface/cinema4d/test',
            'Pmv/hostappInterface/autodeskmaya',
            'Pmv/hostappInterface/autodeskmaya/plugin',
            'Pmv/hostappInterface/extension',
            'Pmv/hostappInterface/extension/testAF',
            'Pmv/hostappInterface/extension/Modeller',
            'Pmv/hostappInterface/houdini',
            'Pmv/styles']

# list of the python modules which are not part of a package
py_modules = ['Pmv/bin/runPmv',
              'Pmv/Macros/changeFontMac',
              'Pmv/Macros/contourMac',
              'Pmv/Macros/DejaVuMac',
              'Pmv/Macros/distanceMac',
              'Pmv/Macros/editMac',
              'Pmv/Macros/exposureMac',
              'Pmv/Macros/msmsMac',
              'Pmv/Tests/Data/littleScript',
              'Pmv/Tests/Data/withLog',
              'Pmv/Tests/Data/rw256_map',
              ]

# list of the files that are not python packages but are included in the
# distribution and need to be installed at the proper place  by distutils.
# The list in MANIFEST.in lists is needed for including those files in
# the distribution, data_files in setup.py is needed to install them
# at the right place.
data_files = []
## for dir in ['Pmv','Pmv/data','Pmv/bin', 'Pmv/bin/CVS',
##             'Pmv/data/CVS','Pmv/CVS', 'Pmv/Tests/CVS',
##             'Pmv/VisionInterface/CVS','Pmv/Icons','Pmv/Icons/CVS',
##             'Pmv/Macros/CVS','Pmv/Tests/Data', 'Pmv/Tests/Data/CVS']:
##     files = []
##     for f in glob(os.path.join(dir, '*')):
##         if f[-3:] != '.py' and f[-4:-1] != '.py' and os.path.isfile(f):
##             files.append(f)
##     data_files.append((dir, files))

def getDataFiles(file_list, directory, names):
    fs = []
    for name in names:
        ext = os.path.splitext(name)[1]
        #print directory, name, ext, len(ext)
        if ext !=".py" and ext !=".pyc":
            fullname = os.path.join(directory,name)
            if not os.path.isdir(fullname):
                fs.append(fullname)
    if len(fs):
        file_list.append((directory, fs))

os.path.walk("Pmv", getDataFiles, data_files)

# description of what is going to be included in the distribution and
# installed.
from version import VERSION
setup (name = 'Pmv',
       version = VERSION,
       description = "Python-based Molecular Viewer",
       author = 'Molecular Graphics Laboratory',
       author_email = 'sanner@scripps.edu',
       download_url = 'http://www.scripps.edu/~sanner/software/packager.html',
       url = 'http://www.scripps.edu/~sanner/software/pmv/webpmv.html',
       packages = packages,
       py_modules = py_modules,
       data_files = data_files,
       scripts = ['Pmv/bin/runPmv'],
       cmdclass = {'sdist': modified_sdist,
                   'install_data': modified_install_data,
                   'build_scripts': modified_build_scripts
                   },
       )
