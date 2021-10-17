#if !defined(TRIANGLE_H)
#define TRIANGLE_H

#include <algorithm>
#include <cmath>
#include <set>
#include <stdexcept>
#include <vector>

namespace triangle {
    enum flavor {
        equilateral,
        isosceles,
        scalene
    };
    
    inline flavor kind(double a, double b, double c)
    {   
        if(a == 0 || b == 0 || c == 0) throw std::domain_error{"A side cannot be zero"};

        std::vector<double> sides{a, b, c};
        std::sort(begin(sides), end(sides));

        if(sides[2] > sides[1] + sides[0])throw std::domain_error{"illegal triangle"};
        
        std::set<double> sidesUnique{a,b,c};
        if(sidesUnique.size() == 1) return equilateral;
        if(sidesUnique.size() == 2) return isosceles;

        return scalene; 
    }
}  // namespace triangle

#endif // TRIANGLE_H