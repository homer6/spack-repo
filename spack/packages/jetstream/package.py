from spack.package import *


class Jetstream(CMakePackage):
    """Jetstream is a general application framework in modern C++ that provides
    features like Kafka integration, HTTP services, database clients, and more."""

    homepage = "https://github.com/homer6/jetstream"
    url      = "https://github.com/homer6/jetstream/archive/refs/tags/v0.1.0.tar.gz"
    git      = "https://github.com/homer6/jetstream.git"

    # Since there's no specific version mentioned, we'll use the main branch
    version('main', branch='master')

    # Dependencies based on the build instructions
    depends_on('cmake', type='build')
    depends_on('cppkafka')
    depends_on('boost@1.65.0:+system+filesystem')
    depends_on('libpqxx')
    depends_on('aws-sdk-cpp')
    depends_on('cpp-httplib')


    """
        -DCPPHTTPLIB_OPENSSL_SUPPORT
    -DCPPHTTPLIB_ZLIB_SUPPORT
    """

    variant('cpphttplib_openssl_support', default=True, description='Enable OpenSSL support for cpp-httplib')
    variant('cpphttplib_zlib_support', default=True, description='Enable Zlib support for cpp-httplib')



    depends_on('openssl', when='+cpphttplib_openssl_support')
    depends_on('zlib', when='+cpphttplib_zlib_support')

    # def cmake_args(self):
    #     args = [
    #         self.define('CMAKE_BUILD_TYPE', 'Release'),
    #         # self.define('LIBPQ_INCLUDE_DIRS', self.spec['libpqxx'].prefix.include),
    #         # self.define('LIBPQ_LIBRARIES', self.spec['libpqxx'].libs.directories[0]),
    #         # self.define('LIBPQXX_INCLUDE_DIRS', self.spec['libpqxx'].prefix.include),
    #         # self.define('LIBPQXX_LIBRARIES', self.spec['libpqxx'].libs.directories[0]),
    #         # self.define('CPPKAFKA_INCLUDE_DIRS', self.spec['cppkafka'].prefix.include),
    #         # self.define('CPPKAFKA_LIBRARIES', self.spec['cppkafka'].libs.directories[0]),
    #         # self.define('RDKAFKA_INCLUDE_DIRS', self.spec['librdkafka'].prefix.include),
    #         # self.define('RDKAFKA_LIBRARIES', self.spec['librdkafka'].libs.directories[0]),
    #         # self.define('OPENSSL_INCLUDE_DIR', self.spec['openssl'].prefix.include),
    #         # self.define('OPENSSL_LIBRARIES', self.spec['openssl'].libs.directories[0]),
    #         # self.define('BOOST_INCLUDE_DIRS', self.spec['boost'].prefix.include),
    #         # self.define('BOOST_LIBRARIES', self.spec['boost'].libs.directories[0]),
    #         # self.define('AWS_SDK_CPP_INCLUDE_DIRS', self.spec['aws-sdk-cpp'].prefix.include),
    #         # #self.define('AWS_SDK_CPP_LIBRARIES', self.spec['aws-sdk-cpp'].libs.directories[0])

    #         # self.define('CPP_HTTPLIB_INCLUDE_DIRS', self.spec['cpp-httplib'].prefix.include),
    #         # #self.define('CPP_HTTPLIB_LIBRARIES', self.spec['cpp-httplib'].libs.directories[0]),

    #         self.define('CPPHTTPLIB_OPENSSL_SUPPORT', self.spec.satisfies('+cpphttplib_openssl_support')),
    #         self.define('CPPHTTPLIB_ZLIB_SUPPORT', self.spec.satisfies('+cpphttplib_zlib_support'))
    #     ]

    #     # aws_lib_dir = self.spec['aws-sdk-cpp'].prefix.lib
    #     # args.append(self.define('AWS_SDK_CPP_LIBRARIES', aws_lib_dir))

    #     # cpp_httplib_lib_dir = self.spec['cpp-httplib'].prefix.lib
    #     # args.append(self.define('CPP_HTTPLIB_LIBRARIES', cpp_httplib_lib_dir))

    #     # args.append(self.define('JETSTREAM_LIBS', 
    #     #     f"{self.spec['librdkafka'].libs.joined(';')};{self.spec['openssl'].libs.joined(';')};{self.spec['cppkafka'].libs.joined(';')};{self.spec['boost'].libs.joined(';')};{self.spec['libpqxx'].libs.joined(';')}"
    #     # ))

    #     # for dep in ['librdkafka', 'openssl', 'cppkafka', 'boost', 'libpqxx']:
    #     #     args.append(self.define('JETSTREAM_INCLUDE_DIRS', self.spec[dep].prefix.include))



    #     # add all of the include dirs to JETSTREAM_INCLUDE_DIRS
    #     for dep in self.spec.dependencies():
    #         args.append(self.define('JETSTREAM_INCLUDE_DIRS', self.spec[dep].prefix.include))

    #     # add all of the lib dirs to JETSTREAM_LIBS
    #     for dep in self.spec.dependencies():
    #         args.append(self.define('JETSTREAM_LIBS', self.spec[dep].prefix.lib))

    def cmake_args(self):
        args = [
            self.define('CMAKE_BUILD_TYPE', 'Release'),
            self.define('CPPHTTPLIB_OPENSSL_SUPPORT', self.spec.satisfies('+cpphttplib_openssl_support')),
            self.define('CPPHTTPLIB_ZLIB_SUPPORT', self.spec.satisfies('+cpphttplib_zlib_support'))
        ]

        import os

        # Collect all include directories
        include_dirs = []
        for dep in self.spec.dependencies():
            if os.path.isdir(self.spec[dep.name].prefix.include):
                include_dirs.append(self.spec[dep.name].prefix.include)
        
        # Join all include directories with semicolons for CMake list
        if include_dirs:
            args.append(self.define('JETSTREAM_INCLUDE_DIRS', ';'.join(include_dirs)))
        
        # Collect all library directories
        lib_dirs = []
        for dep in self.spec.dependencies():
            if os.path.isdir(self.spec[dep.name].prefix.lib):
                lib_dirs.append(self.spec[dep.name].prefix.lib)
        
        # Join all library directories with semicolons for CMake list
        if lib_dirs:
            args.append(self.define('JETSTREAM_LIBS', ';'.join(lib_dirs)))
        
        return args


    license = 'MIT'