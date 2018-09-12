#include <WS2tcpip.h>
#include <iostream>
#include <sstream>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {
  struct sockaddr_in client_addr;
  struct sockaddr_in addr;

  int PORT = 4040;
  cout << "Digite a porta: " << '\n';
  cin >> PORT;

  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_ANY);
  addr.sin_port = htons(PORT);

  int server = socket(AF_INET, SOCK_STREAM, 0), client;
  socklen_t client_size = sizeof client_addr;

  bind(server, (struct sockaddr *)&addr, sizeof addr);
  listen(server, SOMAXCONN);

  cout << "/* Chat init */" << '\n';
  while (true) {
    int client = accept(server, (struct sockaddr *)&client_addr, &client_size);

    while (true) {
      char buff[255];
      int inp = recv(client, buff, sizeof buff, 0);

      cout << buff;
      fflush(stdin);
    }
  }
  return 0;
}
