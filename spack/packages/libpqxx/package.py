from spack.package import *


class Libpqxx(CMakePackage):
    """The official C++ client API for PostgreSQL."""

    homepage = "https://github.com/jtv/libpqxx/"
    url      = "https://github.com/jtv/libpqxx/archive/refs/tags/7.10.0.tar.gz"
    git      = "https://github.com/jtv/libpqxx.git"

    version('7.10.0', sha256='d588bca36357eda8bcafd5bc1f95df1afe613fdc70c80e426fc89eecb828fc3e')

    variant('shared', default=True, description='Build shared libraries')
    variant('static', default=True, description='Build static libraries')
    variant('docs', default=False, description='Build documentation')

    depends_on('cmake@3.12:', type='build')
    depends_on('postgresql+client_only')
    depends_on('doxygen', type='build', when='+docs')
    depends_on('python', type='build')

    license = 'BSD-3-Clause'

    def cmake_args(self):
        args = [
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
            self.define_from_variant('BUILD_STATIC_LIBS', 'static'),
            self.define_from_variant('BUILD_DOC', 'docs'),
            self.define('SKIP_POSTGRES_INSTALL', True),
        ]
        return args
