#ifndef FREEFUNCTION_H
#define FREEFUNCTION_H

#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<algorithm>
#include<iostream>
#include"EventAnalytics.h"

void printTopEvents(const std::vector<SensorEvent>& events, size_t topN);

#endif // FREEFUNCTION_H
