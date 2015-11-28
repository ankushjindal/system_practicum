#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdbool.h>

void error(char *msg)
{
  perror(msg);
  exit(2);
}

void *chat_application(void *ptr){
  int sockfd, newsockfd, portno, clilen;
  char buffer[256];
  struct sockaddr_in serv_addr, cli_addr;
  int n;
  /*  if (argc < 2) {
    fprintf(stderr,"Usage: %s port\n");
    exit(1);
  }
  */
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) 
    error("ERROR opening socket");
  bzero((char *) &serv_addr, sizeof(serv_addr));
  portno = 1000; //atoi(argv[1]);
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_addr.s_addr = INADDR_ANY;
  serv_addr.sin_port = htons(portno);
  if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
    error("ERROR on binding");
  printf("Server running\nServer \tPort: %d\n\n", portno);
  while(true){
    printf("\nWaiting for connection...\n\n");
    listen(sockfd,5);
    clilen = sizeof(cli_addr);
    newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
    if (newsockfd < 0) 
      error("ERROR on accept");
    bzero(buffer,256);
    printf("Connection to client established...\n\n");
    while(true){
      bzero(buffer,256);
      n = read(newsockfd,buffer,255);
      if (n < 0) 
	error("ERROR reading from socket");
      if(strncmp(buffer, "quit", 4) == 0){
	printf("Connection terminated\n");
	break;
      }
      printf("Here is the message: %s\n",buffer);
      n = write(newsockfd,"Message recieved by server\n\0",50);
      if (n < 0) 
	error("ERROR writing to socket"); 
    }
  }
  return NULL;
}

int main(int argc, char *argv[]){
  
  return 0; 
}
