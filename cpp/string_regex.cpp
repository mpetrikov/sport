#include <string>
#include <regex>

using namespace std;

string f(string Z) {
    regex reg(("(\\w)(\\w*)(\\s|$)"));
    return regex_replace(Z, reg, "$2$1$3");
}

std::string ff(std::string str)
{
    regex rgx("([a-zA-Z]*)([^a-zA-Z]*)");
    smatch matches;

    string::const_iterator searchStart(str.cbegin());
    while (regex_search(searchStart, str.cend(), matches, rgx)) {
        if (matches[0] == "") break;

        searchStart = matches.suffix().first;
        matches[1];
        matches[2];
    }

    return "";
}
