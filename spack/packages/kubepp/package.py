from spack.package import *


class Kubepp(CMakePackage):
    """A modern C++ wrapper around the official Kubernetes C client."""

    homepage = "https://github.com/homer6/kubepp"
    url      = "https://github.com/homer6/kubepp/archive/refs/tags/v0.1.0.tar.gz"
    git      = "https://github.com/homer6/kubepp.git"

    version('0.1.0', sha256='4da8014aafdd31d3645bc4231f30776ac4701d9d07860406c1e6ab9dfe188dd7')
    #version('main', branch='main')

    depends_on('cmake', type='build')
    depends_on('kubernetes-c')
    depends_on('spdlog')
    depends_on('fmt')
    depends_on('nlohmann-json')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define('BUILD_SHARED_LIBS', 'ON'),
        ]
        return args

    license = 'MIT'
