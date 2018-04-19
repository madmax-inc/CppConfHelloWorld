#include "hello.hpp"

std::ostream &hello::foo(std::ostream &stream) {
    stream << "Hello, world!";
    return stream;
}
