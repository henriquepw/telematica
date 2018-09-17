#include <arpa/inet.h>

#include <bits/stdc++.h>
#include <unistd.h>

#include <sys/socket.h>
#include <sys/types.h>

#define PORT 4041

using namespace std;

int main() {
  struct sockaddr_in client_addr;
  struct sockaddr_in addr;

  int port = PORT;
  while (true) {
    cin >> port;

    if (port >= 0 and port <= 1024)
      cout << "Porta reservada, tente outra" << '\n';
    else
      break;
  }

  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_ANY);
  addr.sin_port = htons(port);

  // Criando o socket do servidor e do cliente
  int server = socket(AF_INET, SOCK_STREAM, 0), client;
  socklen_t client_size = sizeof client_addr;

  // ligando o socket ao ip e limitando o numero de conexões
  bind(server, (struct sockaddr *)&addr, sizeof addr);=
  listen(server, 1);

  cout << "/* Chat inicicado na porta " << port << " */ \n";
  while (true) {
    // aceitando o pedido do cliente
    client = accept(server, (struct sockaddr *)&client_addr, &client_size);

    while (client > 0) {
      char buff[255];
      int x = recv(client, buff, sizeof buff, 0);

      cout << buff;
      fflush(stdin);
    }

    close(client);
  }

  return 0;
}
