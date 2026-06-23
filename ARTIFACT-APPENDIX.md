# Artifact Appendix 

Paper title: **SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning**

Requested Badge(s):
  - [x] **Available**

## Description 
The artifact relate to the paper #139:  
Title: SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning  
Authors: Andrea Rizzini, Marco Esposito, Tommaso Gagliardoni, Francesco Bruschi  

Within this github repository you can find:  
- drawios source code for the images we inserted in the paper (.drawio files) - the draw.io figures are not containerized because they are manually authored diagrams rather than
computational artifacts.
- the actual images we have inserted in the paper (.png files)
- the source code for the radarplot together with a Docker setup that reproduces the Matplotlib-generated radar plot used as Figure 3.

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
4. Docker Engine or Docker Desktop

### Estimated Time and Storage Consumption

- no more than 20 minutes are required 
- 2.3 MB

## Environment 

You just need to install drawio, docker and having the correct python version

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

**2. Install Docker**  

You can follow the steps described in the official docker manual at this link https://docs.docker.com/engine/install/ubuntu/#:~:text=Set%20up%20Docker%27s%20apt%20repository

**3. Install draw.io 28.0.6**

Download and install the official `.deb` package:

```bash
wget https://github.com/jgraph/drawio-desktop/releases/download/v28.0.6/drawio-amd64-28.0.6.deb
sudo apt install -y ./drawio-amd64-28.0.6.deb
```

You can verify the installation with `drawio --version`, which should print `28.0.6`.

**4. Clone the repository**

```bash
git clone https://github.com/xxxx-yyyy-zzzz/SoK_Material
cd SoK_Material
```

No further configuration is needed. The environment is now ready.

### Testing the Environment

**1. Test the Python script - radar plot (no Docker)**

From the repository root, run:

```bash
mkdir out
python3 radar.py
```

This will generate the radar plot (Figure 3 of the paper) and save it as `out/vfl_radar_comparison_feasibility.png`. If matplotlib and numpy are correctly installed, the script will complete without errors.

**2. Test the Python script - radar plot (Docker)**
## Build

From the root of the artifact repository:

```sh
docker build -t sok-vfl-radar .
```

## Run

The default command runs `radar.py` from the repository root:

```sh
docker run --rm -v "$PWD":/artifact -w /artifact sok-vfl-radar
open out/vfl_radar_comparison_feasibility.png
```

**3. Test the draw.io diagrams**

The `.drawio` files can be opened with the draw.io desktop application. To open a file, run:

```bash
drawio .drawio
```

This will open the draw.io GUI with the diagram loaded. The `.png` files included in the repository are the exported versions of each diagram and can be used as a reference to verify that the diagrams render correctly.

### Literature search and selection procedure reproducibility

To broaden coverage beyond the works already known, we performed a structured search using multiple scholarly search engines, including Google Scholar. We used combinations of keywords such as: “verifiable federated learning,” “verifiability in federated learning,” “verifiable TEE-based federated learning,” “blockchain-based federated learning,” and related variants/synonyms. Candidate papers were collected from search results and then filtered according to the scope and framework defined in the paper. To further broaden coverage
beyond conventional keyword search, we also used AI-assisted “deep research” tools (ChatGPT, Gemini, and Claude) as supplementary discovery mechanisms to identify potentially relevant papers and venues. All quantitative and qualitative information reported in this paper is extracted from publicly available published works and can be independently verified by consulting the cited sources.
