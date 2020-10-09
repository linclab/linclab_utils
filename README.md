# LiNCLab utilities

## Description
This repository contains LiNCLab utilities, i.e. code that is useful across projects.  
&nbsp;

## Installation
- Code is written in `python 3`.
- Requirements are listed under `requirements.txt`.  
- If desired, install using `setup.py`, by running `pip install [-e] .` 
- Alternatively, use modules locally.  
&nbsp;


## Contributions
- Team members are free to contribute to the utilities.  
- Extensions and bug fixes are encouraged, though maintaining backwards compatibility is best, when possible.
- Please document any code you add, and update `requirements.txt` if needed.
- If you wish to make personalized tweaks, don't hesitate to create your own branch or fork the repository.  
&nbsp;

## Modules
### `plot_utils`: Utilities for setting LiNCLab style `matplotlib` plotting parameters.
- `LINCLAB_COLS`: module-wide dictionary of LiNCLab colors.
- `linclab_plt_default()`: sets plotting parameters to use LiNCLab colors and to improve figure better readability. Call it before you start plotting. (NOTE: It just updates the defaults. You can still use custom plotting settings in your scripts.)
 - `linclab_colormap()`: returns a 3-color colormap using LiNCLab colors.
 - `set_font()`: sets matplotlib font to preferred font/font family.
 - `help_logging()`: prints information on using the python `logging` module (which is used in this module).