# SoK_Material

You can find here:
- exported drawios code
- all the images we included in the paper

- the Docker setup that reproduces the Matplotlib-generated radar plot used as
Figure 3. In this artifact repository, the script is `radar.py` and the expected
output is `out/vfl_radar_comparison_feasibility.png`. The draw.io figures are
not containerized because they are manually authored diagrams rather than
computational artifacts.

## Requirements

- Docker Engine or Docker Desktop

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
