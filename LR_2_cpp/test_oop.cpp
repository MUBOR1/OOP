#include <gtest/gtest.h>
#include "your_file_name_with_classes.cpp" // Replace with the actual file name containing Shape, Circle, Square, and Rectangle classes

TEST(ShapeTest, MoveTest) {
    Shape* shape = new Circle(1.0, 2.0, 3.0);
    shape->move(1.0, 1.5);
    EXPECT_DOUBLE_EQ(2.0, shape->getX());
    EXPECT_DOUBLE_EQ(3.5, shape->getY());
    delete shape;
}

TEST(CircleTest, ResizeTest) {
    Circle circle(0.0, 0.0, 4.0);
    circle.resize(2.0);
    EXPECT_DOUBLE_EQ(8.0, circle.getRadius());
}
