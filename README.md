# Cafeteira Hacker TW

A ideia da cafeteira é criar um mecanismo, que divulgará através do twitter, o momento no qual começaríamos a fazer café.

# O que está implementado no código?

Há um método no arquivo job.py que verifica o arquivo schedule_coffee.txt, analisando quais são os horários agendados para iniciar o café. Quando o horário confere com o esperado, a rotina de fazer o café é iniciada. Esta irá manter a cafeteira ligada por 16 minutos e, após este tempo, entrará em ação uma rotina para manter o café aquecido por um período de 29 minutos, ligando e desligando a cafeteira de 1 em 1 minuto para aumentar vida útil da mesma.

As rotinas de iniciar café e acionamento do botão de pânico irão twittar mensagens.

# O que está construído no circuito?

Temos um rele, conectado na saída de 5V da raspi, e outra perna da bobina conectada ao coletor do transistor NPN. O transistor está com base conectada a uma saida da raspi (com resistor em série de 1k ohms) e funciona basicamente como chave para conectar a bobina do rele a GND.
O diodo está como uma proteçao para transistor e raspi.

O botão é uma forma para abortar/iniciar a rotina de fazer café. Existem rotinas que leem a ação neste botão, caso ele seja acionado, ele pode mudar o estado da saída que controla a base do transistor.

## Circuito 
![alt tag](http://i63.photobucket.com/albums/h143/dmbarra/coffee_machine_circuit_schem.jpg)

Responsáveis pelo projeto: Rodrigo Maia, Daniel Barra, Rodolfo Pereira e Dawson Israel (Ordem de beleza)