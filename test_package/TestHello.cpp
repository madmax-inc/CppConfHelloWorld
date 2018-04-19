#include <catch.hpp>
#include "hello.hpp"
#include <sstream>


TEST_CASE("Test that something will be returned") {
    std::stringstream stream;

    hello::foo(stream);


    REQUIRE(stream.str() == "Hello, world!");
}
