#include <math.h>

// Square
#define SQ_XC   10
#define SQ_YC  -10
#define SQ_SIDE 10


int in_square(double x, double y, double xc, double yc, double side)
{
    return (x >= xc - side / 2) && (x <= xc + side / 2) &&
           (y >= yc - side / 2) && (y <= yc + side / 2);
}

int in_area_2(int x, int y)
{
    return in_square(x, y, SQ_XC, SQ_YC, SQ_SIDE);
}
