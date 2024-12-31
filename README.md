## Mesh Renderer 3D

This is a custom-made and bare-bone engine that can render 3D geometric shapes. By default, the window will render a [tesseract](https://en.wikipedia.org/wiki/Tesseract#:~:text=In%20geometry%2C%20a%20tesseract%20or,and%20a%20three%2Ddimensional%20cube.) in 3D. See [How to](#how-to) for specifying your own mesh.

## Getting Started

First, clone this repository via:

```
git clone https://github.com/d22046/3d-mesh-renderer.git
```

The only dependencies that this renderer depends on is a version of `python 3` and `pygame`. You can install Python [here](https://www.python.org/downloads/) if not previously. The easiest way to install pygame is through `pip`, where the installation process can be found [here](https://pip.pypa.io/en/stable/installation/). Then, simply run the following to install pygame:

```
pip install pygame
```

After installing `python` and `pygame`, you can run the renderer using the `python3` command like so:

```
python3 renderer.py
```

## Movement

* Use `W`, `A`, `S`, `D` to move around.
* Press `Space` to float up.
* Press `F` to float down. 
* Use the arrow keys to rotate your field of view.
* Press `R` to reset to everything to their original position.

## How to

This section outlines the various commands you can tell the renderer about how to draw a mesh.

### Specify a Vertex

In `renderer.py`, in the function `initiate`, specify a new vertex by calling the Vertex constructor:

```
v = Vertex( x, y, z )
```

Where `x`, `y`, and `z` are the coordinates of `v` using the normal [Euclidean coordinates plane](https://en.wikipedia.org/wiki/Euclidean_plane). Then, tell the renderer to show `v` by adding it to the `vertices` list via `vertices.append(v)`.

### Specify a Connection between Vertices

At the end of `renderer.py`, there is a section that prompts you to connect the vertices. Specify a connection using the `draw_line` function:

```
draw_line( n, m )
```

Where `n` and `m` are indexes in `vertices`. The `draw_line` function tells the renderer to connect the `n`th vertex to the `m`th vertex in `vertices`.
