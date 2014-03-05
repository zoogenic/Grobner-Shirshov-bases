/**
* @file Types.h
 * @date Mar 4, 2014
 * @author zoogenic
 */

#ifndef _GROBNER_SHIRSHOV_BASES__TYPES_H_
#define _GROBNER_SHIRSHOV_BASES__TYPES_H_

// STL
#include <vector>
#include <set>

namespace Types
{

template <typename T> using Monom = std::vector<T>;

auto my_comp = [](const std::string& left, const std::string& right) -> bool
{
  // whatever
}

template <typename T> using Relation = std::set<Monom<T>, >;

template <typename T>
bool operator > (const Monom &_lhs, const Monom &_rhs)
{
    size_t lsize = _lhs.size();
    size_t rsize = _rhs.size();

    return lsize > rsize || lsize == rsize && std::
}

} // Types

#endif /* _GROBNER_SHIRSHOV_BASES__TYPES_H_ */
