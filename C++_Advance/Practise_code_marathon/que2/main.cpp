#include<vector>
#include<functional>
#include"functionalities.h"
#include<algorithm>
#include<iostream>

int main(){

    // 1. creating a vector of numbers
    std::vector<int> vec = {1,2,3,4,5,6,7,7,8,9};

    //creating vector of all funcs
    std::vector<std::function<void(std::vector<int>)>> funcs = {printOddNumbers, printCountDivisibleBy4, sumLargestAndSecondLargest, printMinimumElement};
    
    // calling all operations
    operations(funcs, vec);
    
    return 0;
}