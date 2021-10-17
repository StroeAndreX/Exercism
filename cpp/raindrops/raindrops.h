#if !defined(RAINDROPS_H)
#define RAINDROPS_H

#include <iostream>
#include <set>
#include <map>
#include <vector>

namespace raindrops {
    inline std::string convert(int raindrops)
    {
        std::map<int,std::string> sounds {{0, "Pling"}, {1, "Plang"}, {2, "Plong"}};
        std::vector<bool> values = {(raindrops % 3 == 0), (raindrops % 5 == 0), (raindrops % 7 == 0)};
        std::string returnString;

        for(int i = 0;  i < 3; i++)
        {
            if(values[i]) returnString += sounds[i];
        }

        return returnString != "" ? returnString : std::to_string(raindrops);   
    }
}  // namespace raindrops

#endif // RAINDROPS_H