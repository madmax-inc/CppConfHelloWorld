cmake_minimum_required(VERSION 2.8)
project(CppConfHelloWorld CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SRC_LIST src/hello.cpp include/hello.hpp)
include_directories(include)
add_library(${PROJECT_NAME} ${SRC_LIST})

if (NOT CONAN_EXPORTED)
	enable_testing()
	add_subdirectory(test_package)
endif()
