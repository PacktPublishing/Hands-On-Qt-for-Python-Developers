#include <iostream>
#include <string>
using namespace std;                  // Variables, types, constants, and 
                                      // functions of the standard C++
                                      // library are declared within 
                                      // the std namespace.
namespace space1 {                    // First namespace.
    string func() {                   // Define function of the first 
                                      // namespace with type string.
        string str1 = " C++ ";        // Declare the string.
        return str1;                  // Function return.
    }
}
namespace space2 {                    // Second namespace.
    string func() {                   // Define function of the second
                                      // namespace with same name
                                      // as in first.
		string str2 = " Program\n";    // Declare the string.
        return str2;                  // Function return. 
	}
}
int main() {
    string newstring;                 // Declare result string.
    string newstr1 = space1::func();  // String from first namespace.
    string newstr2 = space2::func();  // String from second namespace.
    newstring = newstr1 + newstr2;    // Concatenate strings.
    cout << newstring;                // Result to the Terminal/cmd.
    return 0;                         // Program was successful. 
}
