#include <arpa/inet.h>

#include <bits/stdc++.h>
#include <unistd.h>

#include <sys/socket.h>
#include <sys/types.h>

using namespace std;

#define PORT 4040
typedef struct sockaddr_in sockaddr_in;

int main() {
  string buff;

  sockaddr_in client_addr;
  sockaddr_in addr = {.sin_family = AF_INET,
                      .sin_addr.s_addr = htonl(SINADDR_ANY),
                      .sin_port = htons(PORT)};

  // Criando o socket do servidor e do cliente
  int server = socket(AF_INET, SOCK_STREAM, 0);
  int client;

  // lidando o socket ao ip
  bind(server, (struct sockaddr *)&addr, sizeof addr);

  // permintir que o socket receba conexões (socket, numero de conexões)
  listen(server, 5);

  while (1) {
    // aceitando o pedido do cliente
    client =
        accept(server, (struct sockaddr *)&client_addr, &(sizeof client_addr));

    // recebendo mensagens do cliente
    recv(client, buff, sizeof buff, 0);

    cout << buff << '\n';
  }

  return 0;
}
