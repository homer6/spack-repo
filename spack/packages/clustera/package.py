from spack.package import *


class Clustera(CMakePackage):
    """Clustera streaming substrate."""

    homepage = "https://github.com/homer6/clustera"
    url      = "https://github.com/homer6/clustera/archive/refs/tags/v0.1.0.tar.gz"
    git      = "https://github.com/homer6/clustera.git"

    version('main', branch='master')

    depends_on('cmake', type='build')
    depends_on('cppkafka')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
        ]

        import os

        # Collect all include directories
        include_dirs = []
        for dep in self.spec.dependencies():
            if os.path.isdir(self.spec[dep.name].prefix.include):
                include_dirs.append(self.spec[dep.name].prefix.include)
        
        # Join all include directories with semicolons for CMake list
        if include_dirs:
            args.append(self.define('CLUSTERA_INCLUDE_DIRS', ';'.join(include_dirs)))
        
        # Collect all library directories
        lib_dirs = []
        for dep in self.spec.dependencies():
            if os.path.isdir(self.spec[dep.name].prefix.lib):
                lib_dirs.append(self.spec[dep.name].prefix.lib)
        
        # Join all library directories with semicolons for CMake list
        if lib_dirs:
            args.append(self.define('CLUSTERA_LIBS', ';'.join(lib_dirs)))
        
        return args


    license = 'MIT'