# Husky Simulation Project - LaR
Step by step in ROS Noetic for the simulation and odometry analysis of the Husky robot in the Gazebo environment.

## 📁 Repository Structure

This repository should be cloned inside the `src` folder of your Catkin workspace (`catkin_ws/src`):

```text
catkin_ws/
└── src/
    ├── lar_gazebo/      # Gazebo simulation environment
    └── odo_vs_dc/       # Control logic, odometry, and graphics/plotting
```
# Prerequisites

- Ubuntu (with GUI support enabled)
- Docker installed
- Docker container configured with ROS Noetic and Gazebo (lar_noetic)

# How to Run the Project

## Environment Setup (On Host Machine)

Before starting the container, allow Docker to access your host's display (graphics interface) and ensure the container is active:

```bash
xhost +local:docker
docker start lar_noetic
```
## Terminal Optimization (Optional - First time only)

To avoid having to source your environment in every new terminal tab, enter the container once

```bash
docker exec -it lar_noetic bash
```
And inject the automatic configurations into your .bashrc:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "cd /root/catkin_ws" >> ~/.bashrc
exit
```
# Running the Simulation

Open three separate terminals on your host machine and follow the steps below:

## Terminal 1: Open Gazebo with the Robot

Enter the container and launch the virtual environment:

```bash
docker exec -it lar_noetic bash
roslaunch lar_gazebo lar_husky.launch
```
## Terminal 2: Logic and Graphics

Enter the container and execute the node responsible for data processing and plotting:

```bash
docker exec -it lar_noetic bash
roslaunch odo_vs_dc loc0.launch
```
Terminal 3: Play Data (Rosbag)

Enter the container, navigate to the package folder, and play the recorded sensor data from the real robot:

```bash
docker exec -it lar_noetic bash
cd /root/catkin_ws/src/odo_vs_dc
rosbag play husky_odom_real.bag
```

---

### 🛠️ Git Commands (Translated Guide)

If you are setting up the repository from your local machine terminal:

# 1. Initialize git in your local folder
```bash
git init
```
# 2. (Optional) Ignore the heavy rosbag file to prevent GitHub upload blocks
```bash
echo "odo_vs_dc/husky_odom_real.bag" >> .gitignore
```
# 3. Create and paste the English README content above
```bash
nano README.md
```
# 4. Commit your files
```bash
git add .
git commit -m "Initial commit: adding lar_gazebo and odo_vs_dc packages"
```
# 5. Link to your GitHub repository and push
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```






