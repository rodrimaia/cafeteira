# Cafeteira Hacker TW

A ideia da cafeteira, ela criar um mecanismo que divulgaria atraves do twitter o momento no qual começariamos a fazer café.

# O que esta implementado no codigo?

Há um metodo no arquivo job.py, que verifica o arquivo schedule_coffee.txt, analistando quais são os horarios agendados para iniciar o café. Quando horario confere com esperado é iniciado a rotina de fazer café, sendo esta irá manter a cafeteira ligada por 16 minutos, após este tempo, entrará em ação uma rotina que manter o café aquecido por um intervalo de tempo 29 minutos, ligando e desligando a cafeteira de 1 em 1 minuto para aumentar vida util da cafeteira.

As rotinas de iniciar café e acionamento do botão de panico irão twittar mensagem

# O que esta contruido no circuito?

Temos um rele, conectado na saida de 5V da raspi, e outra perna da bobina conectada ao coletor do transistor NPN, este transistor esta com base conectada a uma saida da raspi, com resistor em serie de 1k ohms, este transistor funciona basicamente como chave para conectar a bobina do rele a GND.
O diodo está como uma proteçao para transistor e raspi.

O botão é uma forma para abortar/iniciar a rotina de fazer café, tem rotina que lê a ação neste botão caso ele seja acionado ele pode mudar o estado da saida que controla a base do transistor.

## Circuito 
![alt tag](http://i63.photobucket.com/albums/h143/dmbarra/coffee_machine_circuit_schem.jpg)

Responsaveis pelo projeto: Rodrigo Maia, Daniel Barra, Rodolfo Pereira e Dawson Israel (Ordem de beleza)