#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netdb.h>
#include <string.h>
#include <fcntl.h> 
#include <unistd.h> 

const char APRESSMESSAGE[] = "APRESS for professionals\n";

int main(int argc, char *argv[]) {

    int simpleSocket = 0;
    int simplePort = 0;
    int returnStatus = 0;
    struct sockaddr_in simpleServer;

    /* check we got port num */
    if (2 != argc) {

        fprintf(stderr, "Usage: %s <port>\n", argv[0]);
        exit(1);
    }


    /* create streaming socket, simpleSocket gets file descriptor num */
    simpleSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    printf("sipleSocket=%d", simpleSocket);
    if (simpleSocket == -1) {
        fprintf(stderr, "fail\n");
        exit(1);
    }
    else {
        fprintf(stderr, "success\n");
    }

    /* retrieve port num */ 
    simplePort = atoi(argv[1]);
    
    /* set up address struct */
    /* use INADDR_ANY to bind to all addresses */
    bzero(&simpleServer, sizeof(simpleServer));
    simpleServer.sin_family = AF_INET;
    simpleServer.sin_addr.s_addr = htonl(INADDR_ANY);
    simpleServer.sin_port = htons(simplePort);

    /* bind to the address and port with socket */
    returnStatus = bind(simpleSocket, 
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
    
    /*lets listen on the socket for connections */ 
    
    returnStatus = listen(simpleSocket, 5);
    
    if (returnStatus == -1) {
        fprintf(stderr, "Cannot listen on socket! \n");
        close(simpleSocket);
        exit(1);
    }
    
    while (1){
        struct sockaddr_in clientName = { 0 };
        int simpleChildSocket = 0;
        int clientNameLength = sizeof(clientName);
                            /* accept() is a blocking function */
        simpleChildSocket = accept(simpleSocket, 
                                   (struct sockaddr *)&clientName,
                                   &clientNameLength);

        if (simpleChildSocket == -1) {
            fprintf(stderr, "Cannot accept connections\n");
            close(simpleSocket);
            exit(1);
        }

        /* handle connection, write message */
        write(simpleChildSocket, APRESSMESSAGE, strlen(APRESSMESSAGE));
        close(simpleChildSocket);

    }


    close(simpleSocket);
    return 0;



}


    

