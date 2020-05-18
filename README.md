# app
Aplikacja klient-serwer z wykorzystaniem Dockera
Klient i Serwer łączą się przy pomocy protokołu TCP dla IPv4.

Zadanie zostało wykonane w oparciu o system Linux Mint w wersji 19.3-Cinnamon
Do realizacji wykorzystano język Python i aplikacje Docker oraz docker-compose w wersjach:
  Python v. 3.6.9
  Docker v. 19.03.8
  docker-compose v. 1.23.1
  
Pliki projektu zostały umieszczone według następującej struktury:
|--docker-compose.yml
|--client
|  |--client.py
|  └--Dockerfile
└--server
   |--Dockerfile
   └--server.py

Plik docker-compose.yml zawiera informacje konfiguracyjne dotyczące budowy kontenerów i wywoływanych aplikacji Serwera i Klienta. Ponadto zawiera informacje o sposobie połączenia sieciowego obu kontenerów oraz uzależnieniu uruchomienia kontenera Klienta od gotowości kontenera Serwera.

W folderze client znajduje się wykorzystywany plik aplikacji Klienta (client.py) oraz Dockerfile, określający jakie procesy będą wykonywane w utworzonym kontenerze Klienta.

W folderze server znajduje się wykorzystywany plik aplikacji Serwera (server.py) oraz Dockerfile, określający jakie procesy będą wykonywane w utworzonym kontenerze Serwera.

Bazowym obrazem dla obu plików Dockerfile jest obraz pythona w wersji 3.6.9 zaimporotwany z DockerHub.

Wiadomości od Klienta podawane przez Serwer na stdout można przekierować do pliku hosta przykładową komendą aplikacji docker-compose:
docker-compose logs -f -t server > server.log
