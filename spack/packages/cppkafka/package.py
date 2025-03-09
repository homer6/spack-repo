from spack.package import *


class Cppkafka(CMakePackage):
    """cppkafka is a high level C++ wrapper for rdkafka, aiming to allow 
    using rdkafka in a simple, less error prone way."""

    homepage = "https://github.com/mfontanini/cppkafka"
    url      = "https://github.com/mfontanini/cppkafka/archive/refs/tags/v0.4.1.tar.gz"
    git      = "https://github.com/mfontanini/cppkafka.git"

    # Add versions - check the repository for latest releases
    version('0.4.1', sha256='45770ae0404cb9ba73d659618c51cd55b574c66ed3c7b148360222fb524b0ff7')
    #version('master', branch='master')

    # Dependencies
    depends_on('cmake@3.9.2:', type='build')
    depends_on('librdkafka@0.11.4:')  # For message header support
    depends_on('boost')  # For boost::optional

    # CMake options as variants
    variant('shared', default=True, description='Build shared libraries')
    variant('tests', default=False, description='Build tests')
    variant('examples', default=False, description='Build examples')
    variant('boost_static', default=True, description='Link with Boost static libraries')
    variant('boost_mt', default=True, description='Use Boost multi-threaded libraries')
    variant('rdkafka_static', default=False, description='Link to Rdkafka static library')

    def cmake_args(self):
        args = [
            self.define_from_variant('CPPKAFKA_BUILD_SHARED', 'shared'),
            self.define_from_variant('CPPKAFKA_DISABLE_TESTS', 'tests'),
            self.define_from_variant('CPPKAFKA_DISABLE_EXAMPLES', 'examples'),
            self.define_from_variant('CPPKAFKA_BOOST_STATIC_LIBS', 'boost_static'),
            self.define_from_variant('CPPKAFKA_BOOST_USE_MULTITHREADED', 'boost_mt'),
            self.define_from_variant('CPPKAFKA_RDKAFKA_STATIC_LIB', 'rdkafka_static'),
        ]
        return args

    license = 'BSD-2-Clause'