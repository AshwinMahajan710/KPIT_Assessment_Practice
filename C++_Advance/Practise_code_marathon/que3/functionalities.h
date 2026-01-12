#ifndef FUNCTIONALITIES_H
#define FUNCTIONALITIES_H

#include<string>
#include"Employee.h"
#include"Grade.h"
#include"FullTimeEmployee.h"
#include<stdexcept>
#include<iostream>
#include<vector>
#include<memory>
#include<future>

// function to create vector of FullTimeEmployee objects
std::vector<std::unique_ptr<FullTimeEmployee>> createObjs();

// function to display result for each obj in vector
void calculateAllBonuses(std::vector<std::unique_ptr<FullTimeEmployee>>& employees);

//  function to display all attributes of fulltime emplyee with highest salary in data container
void displayDetailsForHighestSalary(std::vector<std::unique_ptr<FullTimeEmployee>>& employees);

// function to display names via grades
void displayEmployeeLocationViaGrade(std::vector<std::unique_ptr<FullTimeEmployee>>& employees,std::future<Grade> grade);

// //function to find project name of employee with respective id
// std::string getProjectNameByID(std::vector<std::unique_ptr<FullTimeEmployee>>& employees,std::future<int> id);
 
#endif // FUNCTIONALITIES_H
