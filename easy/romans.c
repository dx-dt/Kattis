/* https://open.kattis.com/problems/romans */

#include <stdio.h>

int main(void) {
    const float factor = 880000.0/809.0;
    float input;
    scanf("%f", &input);
    printf("%d",(int)(input*factor + 0.5));
    return 0;
}
