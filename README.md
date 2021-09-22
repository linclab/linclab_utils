# LiNCLab utilities

## Description
This repository contains LiNCLab utilities, i.e. code that is useful across projects.  
&nbsp;

## Installation
- Code is written in `python 3`.
- Requirements are listed under `requirements.txt`.  
- To use a **local, editable version**, you can download the repository, and either:
    - install from `setup.py`, by running `pip install -e .`  
    or
    - use the module locally.
- To use a **fixed version**, you can either:
    - install with `pip install git+https://github.com/linclab/linclab_utils.git`  
    or
    - download the repository and install from `setup.py`, by running `pip install .`
&nbsp;


## Contributions
- Team members are encouraged to contribute to the utilities.  
- Extensions and bug fixes are encouraged, though maintaining backwards compatibility is best, when possible.
- Please document any code you add, and update `requirements.txt`, if needed.
- If you wish to make personalized tweaks, don't hesitate to create your own branch or fork the repository.  
&nbsp;


## Modules
### `plot_utils`: Utilities for setting LiNCLab style `matplotlib` plotting parameters.
- `LINCLAB_COLS`: module-wide dictionary of LiNCLab colors.
- `linclab_plt_default()`: sets plotting parameters to use LiNCLab colors and to improve figure better readability. Call it before you start plotting. (NOTE: It just updates the defaults. You can still use custom plotting settings in your scripts.)
 - `linclab_colormap()`: returns a 2 or 3-color colormap using LiNCLab colors.
 - `set_font()`: sets matplotlib font to preferred font/font family.
 - `help_logging()`: prints information on using the python `logging` module (which is used in this module).  
&nbsp;


 ## Plotting and analysis tips notebook
|   | Run | View |
| - | --- | ---- |
| Tutorial | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/linclab/linclab_utils/blob/main/plotting_tips.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/linclab/linclab_utils/blob/main/plotting_tips.ipynb?flush_cache=true) | 

