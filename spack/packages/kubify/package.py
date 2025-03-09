from spack.package import *


class Kubify(CMakePackage):
    """Kubify accelerates your software into Kubernetes."""

    homepage = "https://github.com/homer6/kubify"
    url      = "https://github.com/homer6/kubify/archive/refs/tags/v0.0.7.tar.gz"
    git      = "https://github.com/homer6/kubify.git"

    # Since there's no specific version mentioned, we'll use the main branch
    #version('main', branch='main')
    version('0.0.7', sha256='ee02a873fb57b1aeb4259bc5fbfb4377ef869f018dbd8c2815e3e1c45013bc9e')

    depends_on('cmake', type='build')
    depends_on('kubepp')
    depends_on('googletest', type='test')

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define('BUILD_SHARED_LIBS', 'ON'),
        ]
        return args
