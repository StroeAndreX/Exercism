#if !defined(TWO_FER_H)
#define TWO_FER_H
#include <string> 

namespace two_fer
{
    inline std::string two_fer(std::string name = "")
    {
        return name != "" ? "One for " + name + ", one for me." : "One for you, one for me."; 
    } 
} // namespace two_fer

#endif //TWO_FER_H
