# auto_ipc
IPC experiment using UFactory Lite6

## Install & Build
- install ROS
- setup workspace
  ```
  mkdir -p ~/ipc_ws/src
  cd ~/ipc_ws
  wstool init src
  catkin build
  ```
- build pkgs
  ```
  git clone https://github.com/asanolab/auto_ipc.git
  wstool merge -t . auto_ipc/install/auto_ipc.noetic.rosinstall
  wstool update
  rosdep install -y -r --from-paths . --ignore-src
  cd auto_ipc
  catkin bt

  echo "source ~/ipc_ws/devel/setup.bash" >> ~/.bashrc
  source ~/ipc_ws/devel/setup.bash
  ```