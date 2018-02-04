#include <math.h>

//ellipse
//center
#define C_X0  20
#define C_Y0  0

#define V_1X 10
#define V_1Y 0
#define V_2X 30
#define V_2Y 0
#define V_3X 20
#define V_3Y 5
#define V_4X 20
#define V_4Y -5

int semiaxis(double x, double x0)
{
    return (x - x0) / 2;
}

int in_ellipse(double x, double y, double xc, double yc, double axis1x1, double axis1x2, double axis2y1, double axis2y2)
{
    return (hypot((x - xc) / semiaxis(axis1x2, axis1x1), (y - yc) / semiaxis(axis2y1, axis2y2)) <= 1);
}

int in_area_6(int x, int y)
{
    return in_ellipse(x, y, C_X0, C_Y0, V_1X, V_2X, V_3Y, V_4Y);
}

//проверить
