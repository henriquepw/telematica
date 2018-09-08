#include <arpa/inet.h>

#include <bits/stdc++.h>
#include <unistd.h>

#include <sys/socket.h>
#include <sys/types.h>

using namespace std;

#define PORT 4041

int main() {
  struct sockaddr_in client_addr;
  struct sockaddr_in addr;

  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_ANY);
  addr.sin_port = htons(PORT);

  // Criando o socket do servidor e do cliente
  int server = socket(AF_INET, SOCK_STREAM, 0);
  int client;
  socklen_t client_size = sizeof client_addr;

  // lidando o socket ao ip
  bind(server, (struct sockaddr *) &addr, sizeof addr);

  // permintir que o socket receba conexões (socket, numero de conexões)
  listen(server, 5);

  cout << "/* Chat init */" << '\n';
  while (1) {
    // aceitando o pedido do cliente
    client = accept(server, (struct sockaddr *) &client_addr, &client_size);

    while (1) {
      char buff[255];
      int x = recv(client, buff, sizeof buff, 0);
      send(client, buff, x, 0);

      cout << buff;
      fflush(stdout);
    }

  }

  return 0;
}
