/*

  Task: Your company produces metal chains and you are a quality assurance engineer whose responsibility is to control and to improve the quality of the product. A chain can be represented as a single row of N chain elements (rings) and each ring has its STRENGTH characteristic – an ability of a particular ring to keep its shape under load.

A chain is a product of good quality if and only if the total sum of STRENGTH of chain elements in any of its part of size K is at least S.

To make a product of good quality, you can perform an augment operation in which you can choose any chain part (subchain) of size with lenght at most K rings and a real number R, and multiply STRENGTH factor of all its rings by R. For each augment operation, the subchain (you can represent it as a subarray) itself and the value of R can be chosen arbitrarily. However, the size of chosen subarray is limited by K, as it is explained above.

The task is to write greedy algorithm to find the minimum number of augment operations you need to perform in order to transform the given chain to a product of good quality.

*/

#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int n, k, s;
	fin >> n >> k >> s;

	// Read array
	vector<int> arr;
	//	arr.resize(n);
	for (int i = 0; i < n; i++) {
		int temp;
		fin >> temp;
		//arr[i] = temp;
		arr.push_back(temp);
	}


	//  Solution
	long inf = 9999999, counter = 0, i = 0;
	while (i <= arr.size() - k) {

		// Find sum on sub array
		int sum = 0;
		for (int j = i; j < i + k; j++) {
			sum += arr[j];
		}



		if (sum < s) {
			int temp_i = i + k - 1;
			int times = 0;

			while (arr[temp_i] == 0) {
				times++;
				if (times > k) {
					fout << -1;
					return 0;
				}
				temp_i--;
			}

			if (temp_i + k < arr.size()) {
				int dead_line = temp_i + k;
				for (temp_i; temp_i < dead_line; temp_i++) {
					if (arr[temp_i] != 0)
						arr[temp_i] = inf;
				}
				counter++;
			}
			else {
				counter++;
				break;
			}
		}
		i++;
	}

	fout << counter;
	return 0;
}
