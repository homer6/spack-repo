from spack.package import *


class Jetstream(CMakePackage):
    """Jetstream is a general application framework in modern C++ that provides
    features like Kafka integration, HTTP services, database clients, and more."""

    homepage = "https://github.com/homer6/jetstream"
    url      = "https://github.com/homer6/jetstream/archive/refs/tags/v0.1.0.tar.gz"
    git      = "https://github.com/homer6/jetstream.git"

    # Since there's no specific version mentioned, we'll use the main branch
    version('main', branch='main')

    # Dependencies based on the build instructions
    depends_on('cmake', type='build')
    depends_on('cppkafka')
    #depends_on('libpq')
    #depends_on('libpqxx')
    depends_on('aws-sdk-cpp')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
        ]
        return args

    license = 'MIT'