#include<vector>
#include<functional>
#include"functionalities.h"
#include<algorithm>
#include<iostream>
#include<limits>

// function to print odd numbers
void printOddNumbers(std::vector<int> numbers){
    std::cout<<"Odd numbers are: ";
    std::for_each(numbers.begin(), numbers.end(), [=](int n){
        if (n%2 !=0) {std::cout<<n<<" ";}
    });
    std::cout<<std::endl;
}

// void print count of numbers divisible by 4
void printCountDivisibleBy4(std::vector<int> numbers){
    int count = 0;
    std::for_each(numbers.begin(), numbers.end(), [&](int n)mutable -> void{
        if (n%4 ==0) {count++;}
    });
    std::cout<<"\ncount of numbers divisible by 4 are: "<<count<<std::endl;
}

// printing sum of largest and second largest
void sumLargestAndSecondLargest(std::vector<int> numbers){
    int max = std::numeric_limits<int>::min(); 
    int secondMax = max;
    std::for_each(numbers.begin(), numbers.end(), [&](int n)mutable -> void{
        if (n > max) {secondMax = max; max = n;}
        if(n > secondMax && n < max) {secondMax = n;}
    });
    std::cout<<"\nsum of max and second max is: "<<max + secondMax<<std::endl;

}

// printing minumum element
void printMinimumElement(std::vector<int> numbers){
    int min = std::numeric_limits<int>::max(); 
    std::for_each(numbers.begin(), numbers.end(), [&](int n) mutable -> void{
        if (min > n) {min = n;}
    });
    std::cout<<"\nMinimum no is: "<<min<<std::endl;
}

// function to call each function
void operations(std::vector<std::function<void(std::vector<int>)>> funcs, std::vector<int> numbers){
    for (auto & func: funcs){
        func(numbers);
    }
}
