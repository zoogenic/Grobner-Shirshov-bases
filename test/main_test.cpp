/**
 * @file main_test.cpp
 * @date Mar 6, 2014
 * @author zoogenic
 */

// THIS
#include "A5/Generators.h"

// GTEST
#include <gtest/gtest.h>

//TEST(A5SizeTest, PositiveNos)
//{
//    ASSERT_EQ(5, sizeof(A5::Generators) / sizeof(A5::Generators[0]));
//}
//
//TEST(A5SizeTest, NegativeNos)
//{
//    ASSERT_EQ(6, sizeof(A5::Generators) / sizeof(A5::Generators[0]));
//}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

