# Kinova Arm Controller - Noetic
This repository contains the information to setup the ROS Noetic based controller part of [DIME](https://arxiv.org/abs/2203.13251) to control the Kinova Arm. We would advice you to install the Kinova SDK and run the setup.sh file in the base repository for convenience and use this as a debugging tool.

## Contents
1. [Requirements](#requirements)
2. [Launching the Controller](#launch-controller)

## Installation Requirements <a name="requirements"></a>
1. Kinova SDK
1. Kinova JACO Arm

## Installing the Kinova SDK
We need to setup the Kinova SDK before we make the C binaries for the controller. You can download the SDK from https://drive.google.com/u/0/uc?id=1UEQAow0XLcVcPCeQfHK9ERBihOCclkJ9&export=download. You should be able make the controller binaries and run the controller after this step.

## Launching the Controller <a name="launch-controller"></a>
After installing the Kinova SDK, you can run catkin_make from the base controller directory (where you have both - Kinova JACO arm controller and Allegro Hand controller). Do the following from this directory:
```
cd <base-controller-dir>
catkin_make
```
After you make the binaries, you need to source the setup files using the below command:
```
source <base-controller-dir>/devel/setup.bash
```
Then you can launch the Allegro Hand's roslaunch file to start controlling the roslaunch file.
```
roslaunch kinova_arm kinova_robot.launch
```
## Citation

If you use this repo in your research, please consider citing the paper as follows:
```
@article{arunachalam2022dime,
  title={Dexterous Imitation Made Easy: A Learning-Based Framework for Efficient Dexterous Manipulation},
  author={Sridhar Pandian Arunachalam and Sneha Silwal and Ben Evans and Lerrel Pinto},
  journal={arXiv preprint arXiv:2203.13251},
  year={2022}
}
```
