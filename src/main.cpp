/**
 * @file main.cpp
 * @date Feb 28, 2014
 * @author zoogenic
 */

// STL
#include <iostream>

#include "Groups/a5.h"

int main()
{
    Groups::A5 v = Groups::A5::a1;
    std::cout << static_cast<std::underlying_type<Groups::A5>::type>(v) << std::endl;
}
