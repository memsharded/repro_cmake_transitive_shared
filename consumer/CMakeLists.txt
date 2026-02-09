
cmake_minimum_required(VERSION 4.2)
project(consumer CXX)

find_package(foobar CONFIG REQUIRED)

add_library(consumer SHARED src/consumer.cpp)
target_include_directories(consumer PUBLIC include)
target_link_libraries(consumer PRIVATE foobar::foobar) # foobar_LIBRARIES is foobar::foobar
set_target_properties(consumer PROPERTIES PUBLIC_HEADER "include/consumer.h")
install(TARGETS consumer)

add_executable(my_app src/my_app.cpp)
target_link_libraries(my_app PRIVATE consumer)
