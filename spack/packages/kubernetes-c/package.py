from spack.package import *


class KubernetesC(CMakePackage):
    """Kubernetes Client Library for C"""

    homepage = "https://github.com/homer6/kubernetes-c"
    url      = "https://github.com/homer6/kubernetes-c/archive/refs/heads/main.zip"
    git      = "https://github.com/homer6/kubernetes-c.git"

    # Since this is a development repository without releases yet,
    # we'll use the main branch
    version('main', branch='main')

    depends_on('cmake', type='build')
    depends_on('openssl')
    depends_on('curl')
    depends_on('libwebsockets')
    depends_on('libyaml')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define('BUILD_SHARED_LIBS', 'ON'),
        ]
        return args
