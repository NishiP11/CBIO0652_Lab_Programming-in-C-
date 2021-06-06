#include <iostream>
using namespace std;

int main() 
{
    int exponent;
    float base, result = 1;

    cout << "Enter base:  ";
    cin >> base;
    cout << "Enter exponent:  ";
    cin>> exponent;


    while (exponent != 0) {
        result *= base;
        --exponent;
    }

    cout << "Power of given number= "<< result;
    
    return 0;
}
