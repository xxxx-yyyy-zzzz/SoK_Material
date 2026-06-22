# Artifact Appendix 

Paper title: **SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning**

Requested Badge(s):
  - [x] **Available**

## Description 
The artifact relate to the paper #139:  
Title: SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning  
Authors: Andrea Rizzini, Marco Esposito, Tommaso Gagliardoni, Francesco Bruschi  

Within this github repository you can find:  
- drawios source code for the images we inserted in the paper (.drawio files)
- the actual images we have inserted in the paper (.png files)
- the source code for the radarplot - figure3 (radar.py file)

### Security/Privacy Issues and Ethical Concerns 

No security or privacy risks come from this artifact

## Basic Requirements 

No special hardware is required, you can run everything on a commodity laptop

### Hardware Requirements 

No special hardware is required, you can run everything on a commodity laptop

### Software Requirements 

1. OS: Ubuntu 24.04.4 LTS
2. Python 3.12.3 and drawio 28.0.6
3. matplotlib and numpy are needed to run the python code

### Estimated Time and Storage Consumption

Replace the following with estimated values for:

- no more than 20 minutes are required 
- 2.3 MB

## Environment 

You just need to install drawio and having the correct python version

### Accessibility 

Everything is available at this repository: https://github.com/xxxx-yyyy-zzzz/SoK_Material

### Set up the environment

The following instructions assume a fresh **Ubuntu 24.04.4 LTS** installation.

**1. Install Python 3.12.3**

Python 3.12 is available in Ubuntu 24.04's default repositories. Run the following commands to install it:

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-pip python3-pip
pip3 install matplotlib numpy --break-system-packages
```

You can verify the installation with `python3 --version`, which should print `Python 3.12.x`.

**2. Install draw.io 28.0.6**

Download and install the official `.deb` package:

```bash
wget https://github.com/jgraph/drawio-desktop/releases/download/v28.0.6/drawio-amd64-28.0.6.deb
sudo apt install -y ./drawio-amd64-28.0.6.deb
```

You can verify the installation with `drawio --version`, which should print `28.0.6`.

**3. Clone the repository**

```bash
git clone https://github.com/xxxx-yyyy-zzzz/SoK_Material
cd SoK_Material
```

No further configuration is needed. The environment is now ready.

### Testing the Environment

**1. Test the Python script (radar plot)**

From the repository root, run:

```bash
mkdir out
python3 radar.py
```

This will generate the radar plot (Figure 3 of the paper) and save it as `out/vfl_radar_comparison_feasibility.png`. If matplotlib and numpy are correctly installed, the script will complete without errors.

**2. Test the draw.io diagrams**

The `.drawio` files can be opened with the draw.io desktop application. To open a file, run:

```bash
drawio .drawio
```

This will open the draw.io GUI with the diagram loaded. The `.png` files included in the repository are the exported versions of each diagram and can be used as a reference to verify that the diagrams render correctly.
```

This will open the draw.io GUI with the diagram loaded. The `.png` files included in the repository are the exported versions of each diagram and can be used as a reference to verify that the diagrams render correctly.
