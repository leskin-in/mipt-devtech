cmake_minimum_required(VERSION 3.0)

project(MatrixAutoGeneration)

add_custom_command(
  OUTPUT array.h
  COMMAND python ${PROJECT_SOURCE_DIR}/generate_matrix.py ${PROJECT_SOURCE_DIR}/input.gptf ${PROJECT_SOURCE_DIR}/array.h
  DEPENDS generate_matrix.py input.gptf
  COMMENT "Transform grayscale picture in GPTF format to an array of values from 0 to 255"
)
add_custom_target(RunGenerator DEPENDS array.h)

set(SOURCES main.cpp)

add_executable(MatrixAutoGeneration ${SOURCES})
add_dependencies(MatrixAutoGeneration RunGenerator)

