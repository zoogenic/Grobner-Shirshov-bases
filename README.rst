Grobner-Shirshov-bases
======================

A C++ library for calculating Grobner-Shirshov bases for semigroups

* The project is developing under Eclipse CDT (Kepler)
* GCC 4.8.1
* GoogleTest 1.6.0

  - ...\\gtest-1.6.0\\include\\gtest\\gtest.h ::
  
     added after include guard
      #if !defined(_VARIADIC_MAX)
        #define _VARIADIC_MAX    10
      #endif
  
  
  - ...\\gtest-1.6.0\\src\\gtest_main.cc ::
     added first row::
     #define _VARIADIC_MAX      10
* GoogleTest symlinks

   ...\\GrSh-GTest\\Libs\\gtest.lib
   
   ...\\GrSh-GTest\\Libs\\gtestd.lib
   
   ...\\GrSh-GTest\\GTest\\ [ = path_to_gtest\\gtest-1.6.0\\include\\gtest\\ ]
   

  
