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
    std::cout << sizeof(A5::Generators) / sizeof(A5::Generators[0]) << std::endl;
}
