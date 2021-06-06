#include <iostream>
using namespace std;
 
int main() {
    char op;
    float num1, num2;
     
    cout << "Enter an arithemetic operator(+ - * /): ";
    cin >> op;
    cout <<"Enter 1st numbers= ";
    cin >> num1; 
    cout<<"Enter 2nd number= ";
    cin>> num2;
 
    switch(op) {
        case '+': 
                cout<<"Addition of two number: " << num1 << " + " << num2 << " = " << num1+num2;
                break;
        case '-':
                cout <<"Subtraction of two number: "<< num1 << " - " << num2 << " = " << num1+num2;
                break;
        case '*':
                cout <<"Multiplication of two number: " <<num1 << " * " << num2 << " = " << num1*num2;
                break;
        case '/':
                cout <<"Divide of two number: " <<num1 << " / " << num2 << " = " << num1/num2;
                break;
        default: 
                printf("ERROR: Unsupported Operation");
    }
     
    return 0;
}