cmake_minimum_required(VERSION 2.8.7)

project(test_CppConfHelloWorld CXX)

set(${PROJECT_NAME}_SRC
        main.cpp
        TestHello.cpp
)

add_executable(${PROJECT_NAME} ${${PROJECT_NAME}_SRC})

target_link_libraries(${PROJECT_NAME}
	CppConfHelloWorld
	${CONAN_LIBS}
)

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)

add_test(NAME ${PROJECT_NAME}
COMMAND ${PROJECT_NAME})
