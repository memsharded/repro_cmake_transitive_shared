
cmake_minimum_required(VERSION 4.2)
project(foobar CXX)

add_library(foo SHARED src/foo.cpp)
target_include_directories(foo PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
set_target_properties(foo PROPERTIES PUBLIC_HEADER "include/foo.h")

add_library(bar SHARED src/bar.cpp)
target_include_directories(bar PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
set_target_properties(bar PROPERTIES PUBLIC_HEADER "include/bar.h")
target_link_libraries(bar PRIVATE foo)

add_library(foobar INTERFACE)
target_link_libraries(foobar INTERFACE bar foo)

install(TARGETS foo bar foobar EXPORT foobarConfig)
export(TARGETS foo bar foobar
    NAMESPACE foobar::
    FILE "${CMAKE_CURRENT_BINARY_DIR}/foobarConfig.cmake"
)
install(EXPORT foobarConfig
    DESTINATION "foobar/cmake"
    NAMESPACE foobar::
)
