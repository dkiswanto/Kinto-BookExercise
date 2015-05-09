#include <iostream>
#include <stdio.h>
#include <ios>
#include <cstdio>

using namespace std;

int main() {
    char text[100];

    while (feof() == false) {
        gets(text);
        cout<<text<<endl;

    }



    return 0;
}
