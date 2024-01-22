# **CPE 322: Assignment 0**
**Design 6 -**
*This is the first assignment for CPE 322.*
> **My name is Ella DiSanti**
1. I am a 3/4 computer engineering major.
2. In addition to a CPE major, I am also pursuing a math minor.
3. On campus, I am involved with SWE, Stevens Orchestra, and the school musical.

---

> **Some more information about me:**
- I am from a small town about 30 minutes north of Pittsburgh, PA. 
- I love music! I play the flute, piano, and guitar, and I try to be as involved with music on campus as possible.
- I like to read. My favorite book that I've read recently is called *The Nightingale* by **Kristen Hannah**. ![bookcover](https://github.com/edisanti/Design-6/assets/122648382/96582e38-0633-494a-b398-a10e044200dc)
- I love to spend time outdoors! I like to ski🎿, hike🌲🥾, and go camping🏕️.
- This is one of my favorite songs: [Vienna by Billy Joel](https://youtu.be/wccRif2DaGs?si=bwRwhdobdd0gJAHO).

> Below is one of the first labs we did in CPE 390:
`#include <iostream>
#include <iomanip>
#include <cmath>
#include <bitset>
using namespace std;

// int
int gcd(int a, int b){
    int start = 0;
    int end = 0;
    int ans = 0;

    if (a<b){
        start = b;
        end = a;
    }
    else if (b>a){
        start = a;
        end = b;
    }
    else{
        start = a;
        end = b;
    }
    for(int i = 1; i <= start; i++){
        if (start%i == 0 && end%i == 0){
            ans = i;
        }
    }
    return ans;
}


bool isPrime(int a){
    for (int i = 2; i < a; i++){
        if(a%i == 0 && a!=i){
            return false;
            break;
        }
    }
    return true;
}

int countPrimes(int a, int b){
    int prime = 0;
    for (int i = a; i <= b; i++){
        if(isPrime(i)==1 && i!=1){
            prime++;
        }
    }
    return prime;
}

// float
float sum_forward(int n){
    float sum = 0;
    for (float n = 1; n <= 100; n++){
        sum += 1/n;
    }
    return sum;
}

float sum_backward(int n){
    float sum = 0;
    for (float n = 100; n >= 1; n--){
        sum += 1/n;
    }
    return sum;
}

double hypot(double a, double b){
    float x = sqrt(pow(a, 2) + pow(b, 2));
    return x;
}

// array
float mean(float x[], int n){
    float sum = 0;
    for (int i = 0; i < n; i++){
        sum += float(x[i]);
    }
    return float(sum/n);
}

void double_each(int a[], int n){
    for (int i = 0; i < n; i++){
        a[i] *= 2;
    }
}

int prod(int x[], int n){
    int prod = 1;
    for (int i = 0; i < n; i++){
        prod *= x[i];
    }
    return prod;
}


int main() {
    //------------------------integer part
    cout << "part 1 output:" << endl;
    cout << "gcd(12, 18)=" << gcd(12, 18) << endl;
    cout << "gcd(1025, 3025)=" << gcd(1025, 3025) << endl;
    cout << "isPrime(5)=" << isPrime(5) << endl;
    cout << "isPrime(9)=" << isPrime(9) << endl;
    cout << "isPrime(1001)=" << isPrime(1001) << endl;
    cout << "isPrime(2601)=" << isPrime(2601) << endl;
    cout << "isPrime(1013)=" << isPrime(1013) << endl;
    cout << "countPrimes(1,100): " << countPrimes(1, 100) << endl;
    cout << "countPrimes(1,10000): " << countPrimes(1, 10000) << endl;
    
    //------------------------floating point number part
    cout << "part 2 output:" << endl;
    float ans_1 = sum_forward(100);
    float ans_2 = sum_backward(100);
    cout << setprecision(8)<< ans_1 << endl;
    cout << setprecision(8) << ans_2 << endl;
    cout << "hypot(3,4)=" << hypot(3, 4) << endl; // should print 5
    cout << "hypot(4,5)=" << hypot(4, 5) << endl;
    //------------------------array part
    cout << "part 3 output:" << endl;
    float x[] = {10, 20, 30, 40, 50, 60};
    int n = sizeof(x)/sizeof(float);
    cout << mean(x, n) << endl; // should print 35
    float y[] = {1.0, 2.0, 3.0, 4.0};
    cout << mean(y, sizeof(y)/sizeof(float)) << endl; // should print 2.5
    int z[] = {10, 20, 30, 40, 50, 60};
    int z_len = sizeof(z)/sizeof(int);
    double_each(z, z_len);
    for (int i = 0; i < z_len; i++) {
        cout << z[i] << ",";
    }
    cout << endl;
    int a[] = {3, 4, 1, 2, -2};
    cout << prod(a, sizeof(a)/sizeof(int)) << endl;
    int b[] = {2, 4, 8, -2, -4};
    cout << prod(b, sizeof(b)/sizeof(int)) << endl;
    
    return 0;
}`
  


