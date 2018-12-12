cmake_minimum_required(VERSION 2.8)
project(build_systems)

set(CMAKE_CXX_STANDARD 11)


set(SOURCES_LIST "B/main.cpp")

add_subdirectory("A")
include_directories(".")

add_executable(bot ${SOURCES_LIST})
target_link_libraries(bot lib)
