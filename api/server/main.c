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

    sa.sin_family = AF_INET;
    sa.sin_port = htons(8080);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);


    printf("hello there\n");

    return EXIT_SUCCESS;
}