cmake_minimum_required (VERSION 2.8)

#-------------------------------------------------------------------------------
# Project name
#-------------------------------------------------------------------------------
set ( PROJECT GrobShir )
set ( PROJECT_DESCRIPTION "Solving Groebner-Shirshov Base application" )
set ( PROJECT_VERSION_MAJOR 0 )
set ( PROJECT_VERSION_MINOR 0 )
set ( PROJECT_VERSION_PATCH 1 )

project ( ${PROJECT} )

#-------------------------------------------------------------------------------
# Setting CMake  ( -DCMAKE_BUILD_TYPE=[Debug,Release] )
#-------------------------------------------------------------------------------
set ( CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin )
set ( CMAKE_LIBRARY_OUTPUT_DIRECTORY ../bin )
set ( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ../bin )

set ( CMAKE_CXX_FLAGS "-W -Wall -std=c++11" )
set ( CMAKE_CXX_FLAGS_DEBUG "-O0 -g3" )
set ( CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -DBOOST_DISABLE_ASSERTS" )

add_definitions ( "-D_FILE_OFFSET_BITS=64" )

#-------------------------------------------------------------------------------
# Adding executable
#-------------------------------------------------------------------------------

add_executable( ${PROJECT} src/main.cpp )