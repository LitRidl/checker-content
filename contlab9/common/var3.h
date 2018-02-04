#include <math.h>

// Circle 1
#define C1X0  -10
#define C1Y0  -10
#define C1RAD  10

// Circle 2
#define C2X0  -20
#define C2Y0  -20
#define C2RAD  10

int in_circle(double x, double y, double x0, double y0, double radius)
{
    return hypot(x - x0, y - y0) <= radius;
}

int in_area_3(int x, int y)
{
    return in_circle(x, y, C1X0, C1Y0, C1RAD) && in_circle(x, y, C2X0, C2Y0, C2RAD);
}
