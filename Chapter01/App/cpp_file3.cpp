#include <iostream> 
#include <string>
using namespace std;
int main() {
	int arr[5] = { 7, 14, 77, 140, 1414 };  // Define array.
	if (arr[0] == 7) {                      // If statement construction.
		cout << arr[0] << '\n';             // Print the result if true
    }                                       // with new line.
    for (int s = 2; arr[s]; arr[s++]) {     // For statement construction.
		if (arr[s] <= 1414){                // if/else construction.
			cout << arr[s-1] << '\n';
		}
		else { 
			break;                          // Break the loop for.
		}
	}
}
