/**
 * @file main.cpp
 * @date Feb 28, 2014
 * @author zoogenic
 */

// STL
#include <iostream>
#include <algorithm> // std::copy
#include <iterator>  // std::ostream_iterator

// THIS
#include "A5/Generators.h"
#include "Types.h"

int main()
{
//    std::cout << sizeof(A5::Generators) / sizeof(A5::Generators[0]) << std::endl;

    Types::Monom<A5::Elements> monom =
    {   A5::Elements::a1
    ,   A5::Elements::a2
    ,   A5::Elements::a3
    ,   A5::Elements::a4
    ,   A5::Elements::a0
    };
//    std::transform(monom.begin(), monom.end()
//    ,   std::ostream_iterator<std::underlying_type<A5::Elements>::type>(std::cout, " ")
//    ,   [&](A5::Elements &_el) -> std::underlying_type<A5::Elements>::type
//        {
//            return std::underlying_type<A5::Elements>::type(_el);
//        }
//    );

    std::copy(monom.begin(), monom.end(), std::ostream_iterator<A5::Elements>(std::cout, " "));
//    for (auto i : monom)
//    {
//        std::cout << i << std::endl;
//    }
}
