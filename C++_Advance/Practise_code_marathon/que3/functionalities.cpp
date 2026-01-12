#include<string>
#include"Employee.h"
#include"Grade.h"
#include"FullTimeEmployee.h"
#include<stdexcept>
#include<iostream>
#include<vector>
#include<memory>
#include<future>
#include"functionalities.h"
#include<algorithm>

// function to create vector of FullTimeEmployee objects
std::vector<std::unique_ptr<FullTimeEmployee>> createObjs(){
    std::vector<std::unique_ptr<FullTimeEmployee>> employees;
    employees.emplace_back(std::make_unique<FullTimeEmployee>("Ashwin Mahajan","1001",10000, "Honda", "Nashik", Grade::A, 12));
    employees.emplace_back(std::make_unique<FullTimeEmployee>("Amul singh","1002",20000, "Honda", "Mumbai", Grade::B, 22));
    employees.emplace_back(std::make_unique<FullTimeEmployee>("Vaishnavi deore","1003",30000, "Honda", "Chennai", Grade::C, 22));
    return employees;
}

// function to display result for each obj in vector
void calculateAllBonuses(std::vector<std::unique_ptr<FullTimeEmployee>>& employees){
    for(auto & employee: employees){
        std::cout<<"Bonus for "<<employee->m_name<<" is: "<<employee->calculateBonus()<<std::endl;
    }
}

//  function to display all attributes of fulltime emplyee with highest salary in data container
void displayDetailsForHighestSalary(std::vector<std::unique_ptr<FullTimeEmployee>>& employees){
    auto max = std::max_element(employees.begin(), employees.end(), [](const std::unique_ptr<FullTimeEmployee>& e1, const std::unique_ptr<FullTimeEmployee>& e2){
        return e1->m_salary<e2->m_salary;
    });
    max->get()->display();
}


void displayEmployeeLocationViaGrade(
    const std::vector<std::unique_ptr<FullTimeEmployee>>& employees,
    std::future<Grade> gradeFuture)
{
    Grade grd = gradeFuture.get(); // blocks
    for (const auto& emp : employees) {
        if (emp && emp->m_grade == grd) {
            std::cout << "Employee with name " << emp->m_name
                      << " have location " << emp->m_employeeLocation << '\n';
        }
    }
}

// std::string getProjectNameByID(
//     const std::vector<std::unique_ptr<FullTimeEmployee>>& employees,
//     std::future<std::string> idFuture)
// {
//     const std::string empid = idFuture.get(); // blocks

//     auto it = std::find_if(employees.begin(), employees.end(),
//         & {
//             return emp && emp->m_id == empid;
//         });

//     if (it != employees.end() && *it)
//         return (*it)->m_name;

//     return ""; // or std::optional<std::string>
// }
