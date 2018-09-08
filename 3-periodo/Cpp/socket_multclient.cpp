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
  listen(server, SOMAXCONN);

  fd_set master;
  FD_ZERO(&master);
  FD_SET(server, &master);

  vector<int> fd_array;
  fd_array.push_back(server);

  cout << "/* Chat init */" << '\n';
  while (true) {
    // copia do master
    fd_set cmaster = master;

    // pegando os clientes conectados
    int clients = select(0, &cmaster, nullptr, nullptr, nullptr);
    for (int i = 1; i < clients; i++) {
      int sock = fd_array[i];

      if (sock == server) {
        //aceitando novo cliente
        //client = accept(server, (struct sockaddr *) &client_addr, &client_size);
        client = accept(server, nullptr, nullptr);

        // adicionado o novo cliente a lista de clientes
        FD_SET(client, &master);
        fd_array.push_back(client);

        string msg = "Bem vindo ao chat";
        send(client, msg.c_str(), msg.size() + 1, 0);
      } else {
        char buff[255];
        int  inp = recv(client, buff, sizeof buff, 0);

        if (inp <= 0) {
          // finalizando o cliente e removendo da lista
          close(sock);
          FD_CLR(sock, &master);
        } else {
          stringstream msgstring;
          msgstring << "Client " << i << ": "  << inp;
          string msg = msgstring.str();

          for (int i = 0; i < fd_array.size(); i++) {
            int out = fd_array[i];
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
