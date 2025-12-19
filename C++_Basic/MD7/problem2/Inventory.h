#ifndef INVENTORY_H
#define INVENTORY_H

#include<string>

class Inventory{
    private:
        std::string m_descriptionOfProduct;
        int m_balanceStock;
        int m_productCode;

    public:
        // default --> stock size of 20
        Inventory();

        // parameterized --> validate balanceStock
        Inventory(const std::string& description_, int balanceStock_, int productCode_);

        // adds stock to current stock and display current stock
        void purchase(int stock);

        // reduce stock to current stock, if less than 20 throws exception and display current stock
        void sale(int stock);        

        // getter for product code
        int getProductCode() const;

        // display function --> to display outputs
        void display() const;

};

#endif // INVENTORY_H
