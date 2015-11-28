#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

void error(char *msg)
{
    perror(msg);
    exit(2);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;

    struct sockaddr_in serv_addr;
    struct hostent *server;

    char buffer[256];
    if (argc < 3) {
       fprintf(stderr,"Usage: %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR connecting");
    printf("Connection Established...\n");
    printf("Hostname: %s\tPort: %s\n\n", argv[1], argv[2]);
    
    while(true){
      bzero(buffer,256);
      printf("Please enter the message (enter quit to disconnect): ");
      fgets(buffer,255,stdin);
      n = write(sockfd,buffer,strlen(buffer));
      if (n < 0) 
	error("ERROR writing to socket");
      if(strncmp(buffer, "quit", 4) == 0)
	break;
      bzero(buffer, 256);
      n = read(sockfd,buffer,255);
      if (n < 0) 
	error("ERROR reading from socket");
      printf("%s\n",buffer);
    }
    printf("Connection terminated...\n");
    return 0;
}
