#ifndef DATALOG_H
#define DATALOG_H

#include<vector>
#include<cstddef>

class Datalog{
    private:
        int m_logId;
        std::vector<int> m_rawData; // (represents sensor readings)
    public:
        Datalog(int id, std::vector<int> rawdata);
        Datalog() = default;
        Datalog(const Datalog&) = delete;
        Datalog(Datalog&& other) noexcept;
        
        Datalog& operator = (const Datalog&) = delete;
        Datalog& operator = (Datalog&& other);

        ~Datalog() = default;

        // member funcs
        int getId() const;
        size_t getDataSize() const;
        void display() const;
};

#endif // DATALOG_H
