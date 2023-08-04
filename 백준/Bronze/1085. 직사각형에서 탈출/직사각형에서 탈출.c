#include <stdio.h>
#define MIN(a, b) (((a) < (b)) ? (a):(b))

int main(){
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    printf("%d", MIN(MIN(MIN(x, y), w-x), h-y));
    
    return 0;
}