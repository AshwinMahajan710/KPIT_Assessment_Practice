#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>
#include<memory>
#include"SharedLogger.h"
#include"freefunc.h"

// function to print specific log info
void printLogInfo(const Datalog& log){
    log.display();
}