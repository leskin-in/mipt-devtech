cmake_minimum_required(VERSION 2.8)
project(build_systems)

set(CMAKE_CXX_STANDARD 11)


set(SOURCES_LIST "lib.cpp")


add_library(lib ${SOURCES_LIST})

