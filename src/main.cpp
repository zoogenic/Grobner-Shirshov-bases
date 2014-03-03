/**
 * @file main.cpp
 * @date Feb 28, 2014
 * @author zoogenic
 */

// STL
#include <iostream>

// THIS
#include "Generators/a5.h"

int main()
{
    Generators::A5 v = Generators::A5::a1;
    std::cout << static_cast<std::underlying_type<Generators::A5>::type>(v) << std::endl;
}
