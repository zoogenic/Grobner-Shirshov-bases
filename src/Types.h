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

template <typename T> using Monom = std::vector<T, std::allocator<T>>;

template <typename T> Monom<T> add(const Monom<T> &_lhs, const Monom<T> &_rhs)
{
    Monom<T> ret;
    bool isTailsMatch = *_lhs.rbegin() == *_rhs.begin();
    ret.reserve(_lhs.size() + _rhs.size() - isTailsMatch);
    ret.insert(ret.end(), _lhs.begin(), _lhs.end());
    ret.insert(ret.end(), isTailsMatch ? _rhs.begin()++ : _rhs.begin(), _rhs.end());
}

//auto my_comp = [](const std::string& left, const std::string& right) -> bool
//{
//  // whatever
//}
//
//template <typename T> using Relation = std::set<Monom<T>, >;
//
//template <typename T>
//bool operator > (const Monom &_lhs, const Monom &_rhs)
//{
//    size_t lsize = _lhs.size();
//    size_t rsize = _rhs.size();
//
//    return lsize > rsize || lsize == rsize && std::
//}

} // Types

//template <typename T>
//std::ostream &operator << (std::ostream &_os, const T &_t)
//{
//    return _os << typename std::underlying_type<T>::type(_t);
//}

#endif /* _GROBNER_SHIRSHOV_BASES__TYPES_H_ */
