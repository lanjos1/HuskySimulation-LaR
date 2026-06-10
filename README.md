# HuskySimulation-LaR
Step by step in ROS Noetic for the simulation and odometry analysis of the Husky robot in the Gazebo environment.

# Projeto de Simulação Husky - LaR

Este repositório contém os pacotes do ROS Noetic utilizados para a simulação e análise de odometria do robô Husky no ambiente do Gazebo.

## 📁 Estrutura do Repositório

O repositório deve ser clonado dentro da pasta `src` do seu workspace Catkin (`catkin_ws/src`):

```text
catkin_ws/
└── src/
    ├── lar_gazebo/      # Ambiente de simulação no Gazebo
    └── odo_vs_dc/       # Lógica de controle, odometria e gráficos
```
# Pré-requisitos

- Ubuntu (com suporte a interface gráfica)
- Docker instalado
- Container Docker configurado com ROS Noetic e Gazebo (lar_noetic)

# Como Rodar o Projeto

## Preparação do Ambiente (No Host)

Antes de iniciar o container, libere a permissão de tela para o Docker (interface gráfica) e certifique-se de que o container está ativo:

```bash
xhost +local:docker
docker start lar_noetic
```
## Otimização do Terminal (Opcional - Apenas na primeira vez)

Para não ter que dar source em todas as abas do terminal, entre no container uma vez:

```bash
docker exec -it lar_noetic bash
```





