#include <vector>
#include <algorithm>

using namespace std;

vector<int> countingSort(vector<int> arr) {
    //int max = INT_MIN;
    //int min = INT_MAX;
    //for_each(arr.begin(), arr.end(), [&](int x) {
    //    if (x > max) max = x;
    //    if (x < min) min = x;
    //});

    // arr
    // 9 7 1 5 3 1 5

    vector<int> sortArray;
    sortArray.resize(100);
    fill(sortArray.begin(), sortArray.end(), 0);
    for (auto e : arr) {
        sortArray[e] += 1;
    }
    // 0 2 0 1 0 2 0 1 0 1 

    vector<int> result;
    for (int i = 0; i < sortArray.size(); i++) {
        int count = sortArray[i];

        if (count > 0) {
            for (int j = 0; j < count; j++) {
                result.push_back(i);
            }
        }
    }
    // 1 1 3 5 5 7 9

    return result;
}
