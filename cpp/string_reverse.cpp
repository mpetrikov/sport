#pragma once
#include <string>

std::string reverseString(std::string str) {
	int length = str.length();
	for (int i = 0; i < length / 2; i++) {
		std::swap(str[i], str[length - i - 1]);
	}

	return str;
}