#include"Inventory.h"
#include<string>
#include<stdexcept>
#include<iostream>

// constructor --> default --> stock size of 20
Inventory::Inventory(): m_balanceStock(20), m_descriptionOfProduct(""), m_productCode(101){}

// constructor --> parameterized --> validate balanceStock
Inventory::Inventory(const std::string& description, int balanceStock_, int productCode_): m_descriptionOfProduct(description), m_productCode(productCode_){
    if(balanceStock_<20){
        throw std::invalid_argument("InvalidBalanceStockException: Balance stock can never go below 20");
    }
    else{
        m_balanceStock = balanceStock_;
    }
}

// adds stock to current stock and display current stock
void Inventory::purchase(int stock){
    if(stock<=0){
        throw std::invalid_argument("InvalidStockException: stock to add can never be -ve or 0");
    }else{
        m_balanceStock += stock;
        std::cout<<"New balance stock is: "<<m_balanceStock<<std::endl;
    }
}

// reduce stock to current stock, if less than 20 throws exception and display current stock
void Inventory::sale(int stock){
    if(stock<=0){
        throw std::invalid_argument("InvalidStockException: stock to sale can never be -ve or 0");
    }else {
        if(m_balanceStock-stock < 20) {
            throw std::invalid_argument("StockNotAvailableException: not available stock equal to quantity of stock to sale ");
        }else{
            m_balanceStock -= stock;
            std::cout<<"New balance stock is: "<<m_balanceStock<<std::endl;
        }
    }
}

// getter
int Inventory::getProductCode() const{
    return m_productCode;
}

// display function
void Inventory::display() const{
    std::cout<<"Product Code: "<<m_productCode<<std::endl;
    std::cout<<"Product Description: "<<m_descriptionOfProduct<<std::endl;
    std::cout<<"Stock Available: "<<m_balanceStock<<std::endl;
}
