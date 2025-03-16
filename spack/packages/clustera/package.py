from spack import *
import logging

class Clustera(CMakePackage):
    """Clustera streaming substrate."""

    homepage = "https://github.com/homer6/clustera"
    url      = "https://github.com/homer6/clustera/archive/refs/tags/v0.1.0.tar.gz"
    git      = "https://github.com/homer6/clustera.git"

    version('main', branch='main')
    version('0.1.1', sha256='dc269886acdeab25d377f52e1a350c09dd316a88a91ad40fed2226e66688afec')
    version('0.1.0', sha256='6e19b96ca51c6877042532fe187f0b5bf77577ff197cca4e002ddda1144205c3')

    depends_on('cmake', type='build')
    depends_on('cppkafka')
    depends_on('googletest', type=('build', 'test'))

    variant('tests', default=True, description='Build test executables')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define_from_variant('BUILD_TESTING', 'tests')
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

    @run_after('install')
    def check_install(self):
        """Verify that test binary was installed correctly."""
        if self.spec.satisfies('+tests'):
            import os
            test_bin = os.path.join(self.prefix.bin, 'clustera_tests')
            if not os.path.isfile(test_bin):
                logging.warning(f"Test binary not found: {test_bin}")
            else:
                logging.info(f"Test binary installed successfully: {test_bin}")

    license = 'MIT'