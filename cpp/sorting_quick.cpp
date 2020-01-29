#include <vector>
using namespace std;

vector<int> quickSort(vector<int> arr) {
    if (arr.size() <= 1) {
        return arr;
    }

    int indexElemForSwap = arr.size() - 1;

    int pivotElement = arr[indexElemForSwap];
    int lastLowerElementPosition = -1;
    for (int i = 0; i < arr.size() - 1; i++) {
        if (arr[i] < pivotElement) {
            lastLowerElementPosition++;
            swap(arr[i], arr[lastLowerElementPosition]);
        }
    }

    // 1, 3, 9, 8, 2, 7, 5
    // 1, 3, 2, 8, 9, 7, 5
    // lowerElementsCount == 2
    lastLowerElementPosition++;
    swap(arr[indexElemForSwap], arr[lastLowerElementPosition]);
    // 1, 3, 2, 5, 9, 7, 8

    auto leftSorted = quickSort(vector<int>(arr.begin(), arr.begin() + lastLowerElementPosition));
    auto rightSorted = quickSort(vector<int>(arr.begin() + lastLowerElementPosition + 1, arr.end()));

    vector<int> result;
    result.reserve(arr.size());
    result.insert(result.end(), leftSorted.begin(), leftSorted.end());
    result.push_back(pivotElement);
    result.insert(result.end(), rightSorted.begin(), rightSorted.end());

    return result;
}
