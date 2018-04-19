from conans import ConanFile, CMake, tools


class CppconfhelloworldConan(ConanFile):
    name = "CppConfHelloWorld"
    version = "0.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Cppconfhelloworld here>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "catch2/2.2.2@bincrafters/stable"
    exports_sources = "main.cpp"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
