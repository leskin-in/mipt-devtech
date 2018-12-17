cmake_minimum_required(VERSION 3.0)
project(build_systems)

set(CMAKE_CXX_STANDARD 11)

find_package(Python3)
find_package(Doxygen)


add_subdirectory("A")
include_directories(".")


add_executable(bot
    B/main.cpp
    C/index.h
)

add_custom_target(generate_index_h ALL
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/C/preparing.py
    BYPRODUCTS C/index.h
    COMMENT "Generating index.h..."
)
add_dependencies(bot generate_index_h)

set(DOXYGEN_GENERATE_HTML NO)
set(DOXYGEN_GENERATE_MAN YES)
set(DOXYGEN_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/doc)
set(DOXYGEN_RECURSIVE yes)
doxygen_add_docs(generate_doc
    COMMENT "Generating documentation..."
)
add_dependencies(bot generate_doc)

target_link_libraries(bot lib)
