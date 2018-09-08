
#include <WS2tcpip.h>
#include <iostream>
#include <sstream>

#pragma comment(lib, "ws2_32.lib")

#define PORT 4041

using namespace std;

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
  bind(server, (struct sockaddr *)&addr, sizeof addr);

  // permintir que o socket receba conexões (socket, numero de conexões)
  listen(server, SOMAXCONN);

  fd_set master;
  FD_ZERO(&master);
  FD_SET(server, &master);

  cout << "/* Chat init */" << '\n';
  while (true) {
    // copia do master
    fd_set cmaster = master;

    // pegando os clientes conectados
    int clients = select(0, &cmaster, nullptr, nullptr, nullptr);
    for (int i = 0; i < clients; i++) {
      int sock = cmaster.fd_array[i];

      if (sock == server) {
        // aceitando novo cliente
        // client = accept(server, (struct sockaddr *) &client_addr,
        // &client_size);
        client = accept(server, nullptr, nullptr);

        // adicionado o novo cliente a lista de clientes
        FD_SET(client, &master);

        string msg = "Bem vindo ao chat";
        send(client, msg.c_str(), msg.size() + 1, 0);
      } else {
        char buff[255];
        int inp = recv(client, buff, sizeof buff, 0);

        if (inp <= 0) {
          // finalizando o cliente e removendo da lista
          closesocket(sock);
          FD_CLR(sock, &master);
        } else {
          stringstream msgstring;
          msgstring << "Client " << i << ": " << inp;
          string msg = msgstring.str();

          for (int i = 0; i < master.fd_count; i++) {
            int out = master.fd_array[i];
            if (out != sock && out != server) {
              send(out, msg.c_str(), msg.size(), 0);
            }
          }
        }

        fflush(stdout);
      }
    }
  }

  return 0;
}
