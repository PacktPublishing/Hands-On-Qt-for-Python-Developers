#include <iostream>
using namespace std;
class Result {                      // Declare the class of the printing result.
    public:                         // Accessible from anywhere where the object is visible.
        static void print(int i);   // A static function of the class
                                    // is only one common variable  
                                    // for all objects of the same 
                                    // class, this function is not 
};                                  // different from one object to another.
void Result::print(int i) {         // (::) specifies that have same
                                    // scope properties as if this function 
    cout << i << '\n';              // definition was directly included
                                    // within the class definition.
}
class Class1 {                      // Declare the first class.
    protected:                      // Accessible from the same class and
                                    // derived classes.
        int x, y, z;
    public:                         // Accessible from anywhere where
                                    // the object is visible.
        Class1(int a, int b, int c): x(a), y(b), z(c) {}
};
class Class2: public Class1, public Result {
                                    // Inheritance of the derived Class2 base classes: Class1, Result.
    public:                         // Accessible from anywhere where the object is visible.
        Class2(int a, int b, int c): Class1(a, b, c) {} 
                                    // Parameters of the base class.
        int result() {
            return x*y*z;           // return value
        }
};
int main () {
    Class2 c2(7, 7, 7);             // c2 object of the Class2.
    c2.print(c2.result());          // Call the object c2 to print the result.
    Class2::print(c2.result());     // Call Class to print the result.
    return 0;
}
