from spack.package import *


class KubernetesC(CMakePackage):
    """Kubernetes Client Library for C"""

    homepage = "https://github.com/homer6/kubernetes-c"
    url      = "https://github.com/homer6/kubernetes-c/archive/refs/tags/v0.9.0.tar.gz"
    git      = "https://github.com/homer6/kubernetes-c.git"

    version('0.9.0', sha256='633dc35051f78593d41e903b63ef58cfaaaff85a7b45047cc767ac04db449151')

    depends_on('cmake', type='build')
    depends_on('openssl')
    depends_on('curl')
    depends_on('libwebsockets')
    depends_on('libyaml')
    depends_on('uncrustify', type='build')

    root_cmakelists_dir = "kubernetes"

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define('BUILD_SHARED_LIBS', 'ON'),
        ]
        return args
