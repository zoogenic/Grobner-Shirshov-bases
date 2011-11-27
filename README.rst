Grobner-Shirshov-bases
======================

A C++ library for calculating Grobner-Shirshov bases for semigroups

1. The project is developing under MSVC 11.
2. Boost 1.48.0
3. GoogleTest 1.6.0
  3.1 ...\\gtest-1.6.0\\include\\gtest\\gtest.h 
  added after include guard::
  
    #if !defined(_VARIADIC_MAX)
      #define _VARIADIC_MAX    10
    #endif
  
  3.2 ...\\gtest-1.6.0\\src\\gtest_main.cc
  added first row::
  
    #define _VARIADIC_MAX      10

4. GoogleTest symlinks

   ...\\GrSh-GTest\\Libs\\gtest.lib
   
   ...\\GrSh-GTest\\Libs\\gtestd.lib
   
   ...\\GrSh-GTest\\GTest\\ [ = path_to_gtest\\gtest-1.6.0\\include\\gtest\\ ]
