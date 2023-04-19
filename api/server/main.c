#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main(int argc, char** argv) {

    struct sockaddr_in sa;
    memset(&sa, 0, sizeof(sa));
    int socket_fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (socket_fd == -1) {
        fprintf(stderr, "Error: Cannot create socket.\n");
        return EXIT_FAILURE;
    }
    #ifdef PRINT_FD
    printf("socket fd: %d\n", socket_fd);
    #endif

    short port = 8080;
    sa.sin_family = AF_INET;
    sa.sin_port = htons(port);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(socket_fd, (struct sockaddr *)&sa, sizeof(sa)) == -1) {
        fprintf(stderr, "Error: Cannot bind socket to port %d.\n", port);
        close(socket_fd);
        return EXIT_FAILURE;
    }
    
    if (listen(socket_fd, 100) == -1) {
        fprintf(stderr, "Error: Cannot listen.\n");
        close(socket_fd);
        return EXIT_FAILURE;
    }


    printf("hello there\n");

    return EXIT_SUCCESS;
}