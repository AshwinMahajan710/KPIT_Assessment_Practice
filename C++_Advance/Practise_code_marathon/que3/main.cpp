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
#include<thread>

int main(){

    // get all employees
    auto fut = std::async(std::launch::async, std::ref(createObjs));
    auto employees = fut.get();

    // calculating alll bonuses
    std::thread th1(calculateAllBonuses, std::ref(employees));
    th1.join();

    // second thread
    std::thread th2(std::ref(displayDetailsForHighestSalary), std::ref(employees));
    th2.join();
    

    // Third thread
    std::promise<Grade> prom;
    std::future<Grade> futGrade = prom.get_future();
    prom.set_value(Grade::A);

    // If your function signature is:
    // void displayEmployeeLocationViaGrade(std::vector<std::unique_ptr<FullTimeEmployee>>& employees,
    //                                      std::future<Grade> grade);
    // (non-const employees)
    std::thread th3(
        displayEmployeeLocationViaGrade,          // no std::ref on the function
        std::ref(employees),                      // pass employees by reference
        std::move(futGrade)                       // move the future (move-only)
    );
    th3.join();
    


    // auto fut = std::async(std::launch::async, std::ref(getProjectNameByID), grd);
    // std::thread th4(std::ref(displayDetailsForHighestSalary), std::ref(employees));
    // th4.join();



    return 0;
}