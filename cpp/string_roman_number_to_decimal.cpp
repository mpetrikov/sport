#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, int> romanDecimalMap {
    make_pair('I', 1),
    make_pair('V', 5),
    make_pair('X', 10),
    make_pair('L', 50),
    make_pair('C', 100),
    make_pair('D', 500),
    make_pair('M', 1000),
};

int solution(string roman) {
    int result = 0;

    int romanLength = roman.length();
    for (int i = 0; i < romanLength; i++) {
        //check, next number is bigger that current
        if (i < romanLength - 1 && romanDecimalMap[roman[i]] < romanDecimalMap[roman[i + 1]]) {
            result += romanDecimalMap[roman[i + 1]] - romanDecimalMap[roman[i]];
            i++;
        } else {
            result += romanDecimalMap[roman[i]];
        }
    }

    return result;
}
