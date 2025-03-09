from spack.package import *


class KubernetesC(CMakePackage):
    """Kubernetes Client Library for C"""

    homepage = "https://github.com/homer6/kubernetes-c"
    url      = "https://github.com/homer6/kubernetes-c/archive/refs/tags/v0.9.0-b.tar.gz"
    git      = "https://github.com/homer6/kubernetes-c.git"

    
    version('0.9.0-b', sha256='3e58f73a1038a94a30ccb6602c09c3f1ae59479dd1e602482666c6da7c3bbea1', preferred=True)
    version('0.9.0-a', sha256='5bb420ce7362875b164e8af94a59abdbbb35b11f612c300ca33d839c7b28ef4d')
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

    license = 'Apache-2.0'