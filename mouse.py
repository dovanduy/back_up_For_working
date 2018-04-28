#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
//author:ningci dev
//date: 2017-05-04 15:39
#define MOUSE_DEV "/dev/input/mouse0"

static int postion_x;
static int postion_y;
static int mouse_fd;

int main(int argc, char **argv)
{
    mouse_fd = open(MOUSE_DEV, O_RDONLY);
    if(-1 == mouse_fd)
    {
        printf("mouse cat't open %s \n", MOUSE_DEV);
        return -1;
    }
    while(1)
    {
        unsigned char buf[3];
        if(read(mouse_fd, buf, sizeof(buf)))
        {
            postion_x = buf[1];
            postion_y = buf[2];
            printf("x:%d y:%d \n", postion_x,  postion_y);
        }
    }
    return 0;
}