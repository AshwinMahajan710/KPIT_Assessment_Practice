#ifndef FUNCTIONALITIES_H
#define FUNCTIONALITIES_H

#include<vector>
#include<functional>

void printOddNumbers(std::vector<int> numbers);

void printCountDivisibleBy4(std::vector<int> numbers);

void sumLargestAndSecondLargest(std::vector<int> numbers);

void printMinimumElement(std::vector<int> numbers);

void operations(std::vector<std::function<void(std::vector<int>)>> funcs, std::vector<int> numbers);

#endif // FUNCTIONALITIES_H
