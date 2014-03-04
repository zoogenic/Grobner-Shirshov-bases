/**
 * @file main.cpp
 * @date Feb 28, 2014
 * @author zoogenic
 */

// STL
#include <iostream>

// THIS
#include "A5/Generators.h"

int main()
{
    A5::Generators v = A5::Generators::a2;
    std::cout << static_cast<std::underlying_type<A5::Generators>::type>(v) << std::endl;
}
