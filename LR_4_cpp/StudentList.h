#include "Student.h"

#ifndef LABA1_STUDENTLIST_H
#define LABA1_STUDENTLIST_H


class StudentList {
private:
    Student **data;
    int size;

public:
    StudentList &add(Student &st);
    StudentList &remove(int index);
    StudentList *findGoodStudents();
    void showGoodStudents();

    StudentList();
    ~StudentList();

    Student **getData() const;
    int getSize() const;
    void print();

};


#endif


