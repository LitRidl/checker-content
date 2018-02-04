#include <math.h>

// Circle 1 (inner)
#define V1_C1X0  10
#define V1_C1Y0  10
#define V1_C1RAD  5

// Circle 2 (outer)
#define V1_C2X0  10
#define V1_C2Y0  10
#define V1_C2RAD 10

int in_circle_2(double x, double y, double x0, double y0, double radius)
{
    return hypot(x - x0, y - y0) <= radius;
}

int in_area_1(int x, int y)
{
    return in_circle_2(x, y, V1_C2X0, V1_C2Y0, V1_C2RAD) && !in_circle_2(x, y, V1_C1X0, V1_C1Y0, V1_C1RAD);
}
