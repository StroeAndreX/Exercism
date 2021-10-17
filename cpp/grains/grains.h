#if !defined(GRAINS_H)
#define GRAINS_H
#include <iostream>       
#include <limits>

namespace grains {
    inline std::uint64_t square(std::size_t grains)
    {
        return std::uint64_t(1) << --grains; // Left Shift operator 
    }

    inline unsigned long long total()
    {
        return std::numeric_limits<std::uint64_t>::max(); /// uInt64_t max value
    }
}  // namespace grains

#endif // GRAINS_H