#include <arpa/inet.h>
#include <bits/stdc++.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>

#define port 1159

using namespace std;

int main() {
  struct sockaddr_in client_addr;
  struct sockaddr_in addr;

  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_ANY);
  addr.sin_port = htons(port);

  int sock = socket(AF_INET, SOCK_STREAM, 0), client;
  socklen_t client_size = sizeof client_addr;

  bind(sock, (struct sockaddr *)&addr, sizeof addr);
  listen(sock, 1);

  cout << "/* Telefone sem fio inicicado na porta " << port << " */ \n";
  while (true) {
    client = accept(sock, (struct sockaddr *)&client_addr, &client_size);

    char buff[1024];
    int x = recv(client, buff, sizeof buff, 0);

    cout << "Recebido de " << client_addr.sin_addr.s_addr << ": " << buff << '\n';

    fflush(stdin);
    unsigned int prox = 0;

    /*
    cout << "IP do proximo: "; cin >> prox;
    close(client);

    client = socket(AF_INET, SOCK_STREAM, 0);
    client_addr.sin_addr.s_addr = htonl(prox);
    client_addr.sin_family = AF_INET;
    client_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    client_size = sizeof client_addr;

    connect(client, (struct sockaddr *)&client_addr, client_size);
    send(client, buff, sizeof buff, 0);
    */

    close(client);
  }

  close(sock);
  return 0;
}
