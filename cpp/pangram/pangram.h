#if !defined(PANGRAM_H)
#define PANGRAM_H

#include <bitset>
#include <cctype>

namespace pangram {


    inline bool is_pangram(std::string sentence)
    {
        std::bitset<26> flags;
        for(char ch : sentence)
        {
            if(std::isalpha(ch)) flags.set(std::tolower(ch) - 'a');
        }
        return flags.all();
    }
    
}  // namespace pangram

#endif // PANGRAM_H
