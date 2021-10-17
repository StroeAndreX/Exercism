#include <iostream>
#include <string>
#include <algorithm>

#if !defined(REVERSE_STRING_H)
#define REVERSE_STRING_H

namespace reverse_string {
    
    inline std::string reverse_string(std::string str) {
        std::reverse(std::begin(str), std::end(str));
        return str;
    }
}  // namespace reverse_string

#endif // REVERSE_STRING_H