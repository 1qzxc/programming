#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netdb.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {

    int simpleSocket = 0;
    int simplePort = 0;
    int returnStatus = 0;
    struct sockaddr_in simpleServer;
    char buffer[256] = "";

    /* check we got port num and server address */
    if (3 != argc) {

        fprintf(stderr, "Usage: %s <server> <port>\n", argv[0]);
        exit(1);
    }


    /* create streaming socket, simpleSocket gets file descriptor num */
    simpleSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    if (simpleSocket == -1) {
        fprintf(stderr, "fail\n");
        exit(1);
    }
    else {
        fprintf(stderr, "success\n");
    }

    /* retrieve port num */ 
    simplePort = atoi(argv[3]);
    
    /* set up address struct */
    /* use IP  */
    bzero(&simpleServer, sizeof(simpleServer));
    simpleServer.sin_family = AF_INET;
    inet_addr(argv[2], &simpleServer.sin_addr.s_addr);
    simpleServer.sin_port = htons(simplePort);

    /* connect to the address and port with our socket */
    returnStatus = connect(simpleSocket, 
                        (struct sockaddr *)&simpleServer,
                        sizeof(simpleServer));
    
    if (returnStatus == 0) {
        fprintf(stderr, "Bind completed!\n");
    }
    else {
        fprintf(stderr, "bind failed\n");
        close(simpleSocket);
        exit(1);
    }
    
    /* get message from server */ 
    returnStatus = read(simpleSocket, buffer, sizeof(buffer));
    
    if (returnStatus > 0) {
        printf("%d: %s", returnStatus, buffer);
        } else {    
            fprintf(stderr, "return status = %d \n", returnStatus);
        }
        
    close(simpleSocket);
    return 0;

}


    

