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
