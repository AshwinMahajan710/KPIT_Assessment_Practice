#ifndef GLOBAL_H
#define GLOBAL_H

#include"Battery.h"
#include<string>
#include<iostream>

void searchBatteriesByManufacturer(Battery* batteries, int count,const std::string& manufacturer);
void displayAllBatteries(Battery* batteries, int count);
#endif