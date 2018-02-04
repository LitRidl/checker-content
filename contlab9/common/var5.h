#include <math.h>

// triangle
#define T_1X  -10
#define T_1Y    0
#define T_2X    0
#define T_2Y   10
#define T_3X  -10
#define T_3Y   20

typedef struct {
    int x, y;
} Point;

int wedge_product(Point p1, Point p2, Point p3)
{
    return (p1.x - p3.x) * (p2.y - p3.y) -
           (p2.x - p3.x) * (p1.y - p3.y);
}

int is_in_triangle(Point pt, Point v1, Point v2, Point v3)
{
    int b1 = wedge_product(pt, v1, v2) <= 0;
    int b2 = wedge_product(pt, v2, v3) <= 0;
    int b3 = wedge_product(pt, v3, v1) <= 0;
    return (b1 == b2) && (b2 == b3);
}


int in_area_5(int x, int y)
{
    Point pt = { x, y };
    Point v1 = { T_1X, T_1Y }, v2 = { T_2X, T_2Y }, v3 = { T_3X, T_3Y };
    return is_in_triangle(pt, v1, v2, v3);
}
