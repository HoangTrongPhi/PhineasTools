import maya.cmds as cmds
import math
import random
import os
import json


# CHECK IF GLOBAL VARIABLE EXISTS :
def global_variable_exists(var_name):
    return var_name in globals()

if not global_variable_exists("texture_resolution"):
    texture_resolution = 1024
if not global_variable_exists("division_sizes"):
    division_sizes = []
if not global_variable_exists("padding_scale"):
    padding_scale = 0
if not global_variable_exists("randomize_checkbox_value"):
    randomize_checkbox_value = False
if not global_variable_exists("match_division_height_checkbox_value"):
    match_division_height_checkbox_value = False    


# GET UV SHELLS :
def get_uv_shells(selected_objects=None):
    
    selected_objects = cmds.ls(selection=True)
    all_uvs = []

    for obj in selected_objects:
        if cmds.objectType(obj) == "mesh":
            cmds.select(obj)
            cmds.ConvertSelectionToUVs()
            obj_uvs = cmds.ls(selection=True, flatten=True)
            all_uvs.extend(obj_uvs)
        elif cmds.objectType(obj) == "float2":
            all_uvs.append(obj)

    uv_shells = []

    while all_uvs:
        cmds.select(all_uvs[0])
        cmds.ConvertSelectionToUVShell()
        uv_shell = cmds.ls(selection=True, flatten=True)
        uv_shells.append(uv_shell)

        for uv in uv_shell:
            if uv in all_uvs:
                all_uvs.remove(uv)
    
    print("Uv Shells = ", uv_shells)
    print("Numbers of shells = ", len(uv_shells))
    return uv_shells


# GET SHELL CENTER :
def get_shell_center(uv_shell):
    
    uv_bbox = cmds.polyEvaluate(uv_shell, bc2=True)
    center_u = (uv_bbox[0][0] + uv_bbox[0][1]) / 2
    center_v = (uv_bbox[1][0] + uv_bbox[1][1]) / 2
    
    return center_u, center_v
    
# GET SHELL PIXEL HEIGHT :
def get_shell_pixel_height(uv_shell):
    
    uv_bbox = cmds.polyEvaluate(uv_shell, bc2=True)
    pixel_height = (uv_bbox[1][1] - uv_bbox[1][0]) * texture_resolution
    
    print("shells height in pixel = ", pixel_height)
    return pixel_height

# SET SHELL PIXEL HEIGHT :
def set_shell_pixel_height(uv_shell, desired_pixel_height):
    
    current_pixel_height = get_shell_pixel_height(uv_shell)
    
    scale_factor = desired_pixel_height / current_pixel_height
    
    center_u, center_v = get_shell_center(uv_shell)
           
    cmds.select(uv_shell)
    cmds.polyEditUV(pivotU=center_u, pivotV=center_v, scaleU=scale_factor, scaleV=scale_factor)      
        
# CONVERT PIXEL UNIT TO UV UNIT :
def convert_pixel_unit_to_uv_unit(pixel_unit, texture_resolution):
    uv_unit = pixel_unit / texture_resolution
    return uv_unit

# RANDOMIZE BEST MATCH
def randomize_best_match(matching_divisions):
    return random.choice(matching_divisions)    
   
# ALIGN UV SHELLS ON THE GRID TEMPLATE :
def align_uv_shells_to_grid_template(uv_shells, grid_template, randomize=False, match_division_height=False):
    # Find the largest division size
    if grid_template:
        # Find the largest division size
        largest_division_size = max(division['size'] for division in grid_template) * texture_resolution
    else:
        largest_division_size = 0  # or any default value you want to use when the grid_template is empty

    for shell in uv_shells:
        shell_pixel_height = get_shell_pixel_height(shell)
        shell_center_u, shell_center_v = get_shell_center(shell)

        # If the shell is larger than the largest division size, assign it to the largest division size
        if shell_pixel_height > largest_division_size:
            best_matching_divisions = [division for division in grid_template if division['size'] * texture_resolution == largest_division_size]
        else:
            min_diff = float('inf')
            best_matching_divisions = []

            for division in grid_template:
                if shell_pixel_height <= division['size'] * texture_resolution:
                    diff = division['size'] - shell_pixel_height
                    if diff < min_diff:
                        min_diff = diff
                        best_matching_divisions = [division]
                    elif diff == min_diff:
                        best_matching_divisions.append(division)

        if best_matching_divisions:
            if randomize:
                best_match = randomize_best_match(best_matching_divisions)
            else:
                best_match = best_matching_divisions[0]

            target_center_v = best_match['pos'] + (best_match['size'] / 2)
            cmds.select(shell)
            cmds.polyEditUV(pivotU=shell_center_u, pivotV=shell_center_v, uValue=0.5 - shell_center_u, vValue=(target_center_v - shell_center_v))
                
            if match_division_height:
                desired_pixel_height = best_match['size'] * texture_resolution
                set_shell_pixel_height(shell, desired_pixel_height)
                
            # Apply padding :
            cmds.select(shell, r=1)
            uniform_scale_factor = pixel_padding_to_uniform_scale_factor(shell, padding_scale, texture_resolution)
            shell_center_u, shell_center_v = get_shell_center(shell)
            cmds.polyEditUV(pivotU=shell_center_u, pivotV=shell_center_v, scaleU=uniform_scale_factor, scaleV=uniform_scale_factor)    
            
            
    cmds.select(cl=1)       
    
    for shell in uv_shells:
        cmds.select(shell, add=1)

# CREATE TEMPLATE GRID :
def create_template_grid(texture_resolution, division_sizes):
    grid_template = []
    current_pos = 0

    for size in division_sizes:
        uv_pos = 1 - convert_pixel_unit_to_uv_unit(current_pos, texture_resolution) # Start from the top of the UV space
        uv_size = convert_pixel_unit_to_uv_unit(size, texture_resolution)
        grid_template.append({
            'pos': uv_pos - uv_size, # Subtract uv_size from uv_pos to have the divisions aligned correctly
            'size': uv_size
        })
        current_pos += size
        print(1 - (current_pos - uv_size))

    return grid_template

# CENTER UV SHELL IN SELECTED TRIM
def center_uv_shell_in_division(uv_shells, division_index, match_division_height=False):
    if division_index >= len(division_sizes):
        cmds.warning("Invalid division index")
        return

    grid_template = create_template_grid(texture_resolution, division_sizes)
    target_division = grid_template[division_index]

    for uv_shell in uv_shells:
        shell_center_u, shell_center_v = get_shell_center(uv_shell)
        target_center_u = 0.5
        target_center_v = target_division['pos'] + (target_division['size'] / 2)

        cmds.select(uv_shell)
        cmds.polyEditUV(pivotU=shell_center_u, pivotV=shell_center_v, uValue=target_center_u - shell_center_u, vValue=target_center_v - shell_center_v)

        if match_division_height:
            desired_pixel_height = target_division['size'] * texture_resolution
            set_shell_pixel_height(uv_shell, desired_pixel_height)
        
        # Apply padding :
        cmds.select(uv_shell, r=1)
        uniform_scale_factor = pixel_padding_to_uniform_scale_factor(uv_shell, padding_scale, texture_resolution)
        shell_center_u, shell_center_v = get_shell_center(uv_shell)
        cmds.polyEditUV(pivotU=shell_center_u, pivotV=shell_center_v, scaleU=uniform_scale_factor, scaleV=uniform_scale_factor)    

# GET THE UV SHELLS :
uv_shells = get_uv_shells()

# CREATE THE GRID TEMPLATE
grid_template = create_template_grid(texture_resolution, division_sizes)

# UI LOGIC :

# GET TRIM VALUE
def add_division(*args):
    size = cmds.intField(size_input, query=True, value=True)
    division_sizes.append(size)
    update_division_list()

# REMOVE TRIM VALUE
def remove_division(*args):
    if division_sizes:
        division_sizes.pop()
        update_division_list()

# CLEAR DIVISIONS
def clear_divisions(*args):
    division_sizes.clear()
    update_division_list()

# CENTER UV SHELL IN DIVISION
def center_uv_shell_callback(division_index, *args):
    uv_shells = get_uv_shells()
    match_division_height_opt = cmds.checkBox(match_division_height_checkbox, query=True, value=True)
    if uv_shells:
        center_uv_shell_in_division(uv_shells, division_index, match_division_height=match_division_height_opt)


def update_division_list():

    global division_input_layout
    children = cmds.columnLayout(division_input_layout, query=True, childArray=True)
    if children:
        for child in children:
            cmds.deleteUI(child)

    for idx, size in enumerate(division_sizes):
        cmds.setParent(division_input_layout)
        cmds.rowLayout(numberOfColumns=3, columnWidth3=(50, 50, 100), adjustableColumn=2, columnAlign=(1, 'left'))
        size_field = cmds.intField(value=size)
        
        def update_division_size(value, index):
            division_sizes[index] = value

        from functools import partial
        cmds.intField(size_field, edit=True, changeCommand=partial(update_division_size, index=idx))
        cmds.button(label="Center", command=partial(center_uv_shell_callback, idx))
        cmds.setParent("..")  # Move back to the division_input_layout

def align_uv_shells_callback(*args):
    randomize_opt = cmds.checkBox(randomize_checkbox, query=True, value=True)
    match_division_height_opt = cmds.checkBox(match_division_height_checkbox, query=True, value=True)
    uv_shells = get_uv_shells()
    grid_template = create_template_grid(texture_resolution, division_sizes)
    align_uv_shells_to_grid_template(uv_shells, grid_template, randomize=randomize_opt, match_division_height=match_division_height_opt)


# PIXEL PADDING TO UNIFORM SCALE FACTOR (0.2 Replace the scaling factor logic)

def pixel_padding_to_uniform_scale_factor(uv_shell, pixel_padding, texture_resolution, precision=10):
    # Calculate the bounding box size in UV space
    uv_bbox = cmds.polyEvaluate(uv_shell, bc2=True)
    bbox_width_uv = uv_bbox[0][1] - uv_bbox[0][0]
    bbox_height_uv = uv_bbox[1][1] - uv_bbox[1][0]

    # Convert padding from pixels to UV space
    padding_u = pixel_padding / texture_resolution
    padding_v = pixel_padding / texture_resolution

    # Adjust the UV dimensions to account for the padding
    target_width_uv = bbox_width_uv - 2 * padding_u
    target_height_uv = bbox_height_uv - 2 * padding_v

    # Ensure target dimensions are positive and non-zero
    target_width_uv = max(target_width_uv, 0.0001)
    target_height_uv = max(target_height_uv, 0.0001)

    # Calculate scale factors and apply rounding
    scale_factor_u = round(target_width_uv / bbox_width_uv if bbox_width_uv > 0 else 1, precision)
    scale_factor_v = round(target_height_uv / bbox_height_uv if bbox_height_uv > 0 else 1, precision)

    # Use the minimum scale factor to maintain aspect ratio
    uniform_scale_factor = min(scale_factor_u, scale_factor_v)

    return uniform_scale_factor
    
def update_padding_scale(*args):
    global padding_scale
    padding_scale = cmds.floatField(padding_input, query=True, value=True) 
    
def update_texture_resolution(*args):
    global texture_resolution
    texture_resolution = cmds.floatField(texture_res_input, query=True, value=True)     
    
def shuffle_uv_shells_callback(*args):
    uv_shells = get_uv_shells()
    for shell in uv_shells:
        cmds.select(shell, add=1)
        u, v = get_shell_center(shell)
        cmds.polyEditUV(shell, relative=True, uValue=random.uniform(-1, 1) - u)    
    
def update_randomize_checkbox_value(*args):
    global randomize_checkbox_value
    randomize_checkbox_value = cmds.checkBox(randomize_checkbox, query=True, value=True)

def update_match_division_height_checkbox_value(*args):
    global match_division_height_checkbox_value
    match_division_height_checkbox_value = cmds.checkBox(match_division_height_checkbox, query=True, value=True)

# SAVE PRESET
def save_preset(*args):
    file_path = cmds.fileDialog2(fileMode=0, dialogStyle=2, caption='Save Preset', fileFilter='Trim Preset (*.json)')
    if file_path:
        data = {
            "division_sizes": division_sizes,
            "texture_resolution": texture_resolution,
            "padding_scale": padding_scale,
            "randomize": cmds.checkBox(randomize_checkbox, query=True, value=True),
            "match_division_height": cmds.checkBox(match_division_height_checkbox, query=True, value=True)
        }
        with open(file_path[0], 'w') as outfile:
            json.dump(data, outfile, indent=4)
            
# LOAD PRESET            
def load_preset(*args):
    file_path = cmds.fileDialog2(fileMode=1, dialogStyle=2, caption='Load Preset', fileFilter='Trim Preset (*.json)')
    if file_path:
        with open(file_path[0], 'r') as infile:
            data = json.load(infile)
            if "division_sizes" in data:
                global division_sizes, texture_resolution, padding_scale
                division_sizes = data["division_sizes"]
                texture_resolution = data.get("texture_resolution", texture_resolution)
                padding_scale = data.get("padding_scale", padding_scale)
                randomize = data.get("randomize", False)
                match_division_height = data.get("match_division_height", False)

                # Update UI elements
                cmds.floatField(texture_res_input, edit=True, value=texture_resolution)
                cmds.floatField(padding_input, edit=True, value=padding_scale)
                cmds.checkBox(randomize_checkbox, edit=True, value=randomize)
                cmds.checkBox(match_division_height_checkbox, edit=True, value=match_division_height)

                update_division_list()
            else:
                cmds.warning("Invalid preset file.")        
       

# Create the UI window
window_name = "Fast_Trim_UV"


if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)    

window = cmds.window(window_name, title="Fast Trim UV", menuBar=True, rtf=1)

MenuLayout = cmds.menuBarLayout()
fileMenu = cmds.menu(label="File")
loadOption = cmds.menuItem(label="Load", command=load_preset)
saveOption = cmds.menuItem(label="Save", command=save_preset)

cmds.columnLayout(adjustableColumn=True)

# Add and remove divisions
cmds.rowLayout(numberOfColumns=3, columnAlign1=("center"), h=50, ad3=1, bgc=(0.2,0.2,0.2))
size_input = cmds.intField(minValue=1, value=64, bgc=(0.15,0.15,0.15))
cmds.button(label="Add Trim", command=add_division)
cmds.button(label="Remove Trim", command=remove_division)
cmds.setParent("..")

# Division size inputs
division_input_layout = cmds.columnLayout(adjustableColumn=True)
update_division_list()

cmds.setParent("..")  # Move back to the main columnLayout

cmds.rowLayout(numberOfColumns=2, columnWidth2=(100, 200), adjustableColumn=2, columnAlign=(1, 'left'))
cmds.text(label="Texture Resolution:")
texture_res_input = cmds.floatField(value=texture_resolution, changeCommand=update_texture_resolution, pre=0)
cmds.setParent("..")

# Padding input
cmds.rowLayout(numberOfColumns=2, columnWidth2=(100, 200), adjustableColumn=2, columnAlign=(1, 'left'))
cmds.text(label="Padding:")
padding_input = cmds.floatField(value=padding_scale, changeCommand=update_padding_scale, pre=2)
cmds.setParent("..")

# Checkboxes
cmds.rowLayout(numberOfColumns=2, columnWidth2=(100, 100), adjustableColumn=2, columnAlign=(2, 'center'))
randomize_checkbox = cmds.checkBox(label="Randomize", value=randomize_checkbox_value, changeCommand=update_randomize_checkbox_value)
match_division_height_checkbox = cmds.checkBox(label="Match Trim Height", value=match_division_height_checkbox_value, changeCommand=update_match_division_height_checkbox_value)
cmds.setParent("..")

# Add UI elements

cmds.button(label="Auto Align Selected UV Shells", command=align_uv_shells_callback, h=30, bgc=(1,0.5,0.1))
cmds.button(label="Randomize Shells U Position", command=shuffle_uv_shells_callback, h=30)

# Display the window
cmds.showWindow(window)
cmds.window(window, e=True, width=250, height=210)



