#include <vector>

using namespace std;

vector<int> insertionSort(int n, vector<int> arr) {
    for (int i = 1; i < n; i++) {
        int swapElement = arr[i];
        int j = i - 1;

        // 2 3 4 4
        // 2 3 3 4
        // 2 2 3 4
        while (j >= 0 && swapElement < arr[j]) {
            arr[j + 1] = arr[j];
            --j;
        }
        // 1 2 3 4
        arr[j + 1] = swapElement;
    }

    return arr;
}
