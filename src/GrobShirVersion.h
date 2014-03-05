/**
 * @file CurrencyUpdaterVersion.h
 */

#ifndef GROBSHIRVERSION_H_
#define GROBSHIRVERSION_H_

// C++
#include <string>

namespace GrobShir
{
namespace Version
{

/** @return Возвращает название проекта */
std::string getProjectName();

/** @return Возвращает описание проекта */
std::string getProjectDescription();

/** @return Возвращает номер мажорной версии */
std::string getMajor();

/** @return Возвращает номер минорной версии */
std::string getMinor();

/** @return Возвращает номер патча */
std::string getPatch();

/** @return Возвращает номер ревизии */
std::string getRevision();

/** @return Возвращает информацию о проекте */
std::string getString();

} // namespace Version
} // namespace GrobShir

#endif /* GROBSHIRVERSION_H_ */
