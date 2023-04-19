#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 2048


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



    while (true) {

        printf("Waiting for connections...\n");
        int connect_fd = accept(socket_fd, NULL, NULL);
        printf("Accepted a connection.\n");

        if (connect_fd == -1) {
            fprintf(stderr, "Error: Cannot listen.\n");
            close(socket_fd);
        }

        char buffer[BUFFER_SIZE];
        int read_count = read(connect_fd, buffer, BUFFER_SIZE);
        if (read_count == -1) {
            fprintf(stderr, "Error: Could not read from client.\n");
            close(connect_fd);
            continue;
        }
        buffer[read_count] = '\0';
        printf("%s\n", buffer);

        write(connect_fd, "test", 4);


        // close(connect_fd);
    }


    printf("hello there\n");

    return EXIT_SUCCESS;
}