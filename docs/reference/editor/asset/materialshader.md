# Creation

Material Shaders are a powerful way of controlling the artistic beauty of your game's environment, but can also be a cost to performance, game size and load times if abused. A balance of efficient shader code and reusing parameters is how you can reduce the overall load of the renderer, allow better draw batching, as well as reduce shader compilation times and file sizes!

# Domain

Material Shaders have several domains, each with a different underlying purpose:

- Surface:
    - Is used for rendering materials on phyisical 3D objects, e.g. 3D Models, particles, billboards, terrain, etc. 
- Decal:
    - Is used for *projective* substances, to alter or overlay material properties onto [Surface]() materials.
- Volumetric:
    - Is used for add volumetric data for volumetric lights. This can be an expensive shader, so use with caution.
- Post Processing:
    - Is used for building custom post processing effects.
- RML:
    - Is used for building custom shaders that can be used on RmlUi elements via the `<shader>` tag. 
- Brush:
    - Is an editor only asset used for creating 2D brushes, most notably for [terrain]() editing.

## Surface Pipeline Signature

Here is the Markdown documentation structured from your ImGui code snippet. I've populated the descriptions using the tooltips provided in the code, added the available options for dropdowns, noted conditional UI states, and left placeholders for you to fill in the rest.

### Render Pass

#### Pass Mode
[Add description here]

**Options:**

- Opaque G-Buffer
- Transparent T-Buffer
- Forward
- Forward No Early Z
- Post Composite Overlay

### Shading

#### Lighting Model
[Add description here]*

**Options:** 

- Unlit BSDF
- Standard BSDF
- Clearcoat BSDF
- Cloth BSDF
- Anisotropic BSDF
- Thin Subsurface BSDF
- Thin Translucent BSDF


### Blend State

#### Blend Mode
*[Add description here]*

**Options:** 

- Opaque
- Masked
- Alpha Blend
- Additive Blend
- Multiplicative Blend
- OIT Blend


#### Alpha Cutoff
*[Add description here]*


*Note: Only active when Blend Mode is set to 'Masked'.*


#### Draw Order Hint
*[Add description here]*


### Rasteriser State

#### Polygon Mode
*[Add description here]*


**Options:** 

- Filled
- Wireframe


#### Culling
*[Add description here]*

**Options:** 

- None
- Back
- Front

### Depth State

#### Depth Modify
Allows modification of depth values through Pixel Depth Offset. Note that the pixel depth is Reverse Z, meaning negative values move further *away* from the camera.

**Options:** 

- No Modify
- Modify,
- Conservative Less Equal
- Conservative Greater Equal

### Geometry Manipulation

#### Vertex Offset Mode
Allows modification of vertex positions, and that the node either designates local or world offset. Note that Local offset is post-skinning! This is due to vertex transform caching for improved efficiency!

**Options:** 

- No Offset
- Local Position Offset
- World Position Offset

#### Tessellation Mode
Enables subdivision of vertices for improved geometry quality. Note that performance may significantly degrade with this rendering feature! Please use with caution! Consider using more subdivided meshes instead.

**Options:**

- No Tessellation
- Triangles
- Quads

#### Tessellation Partitioning**
*[Add description here]*

**Options:**

- Integer
- Fractional Even
- Fractional Odd

*Note: Only active when Tessellation Mode is not set to 'No Tessellation'.*

#### Multi Sample State

#### MSAA Mode
Enhance quality through MSAA usage. Only supported on Forward render modes.

**Options:**
- No MSAA,
- MSAA Only
- A2C Only

*Note: Only active when Pass Mode is set to 'Forward No Early Z'.*


### Render Systems

- **Orthogonal Shadows**
    - *[Add description here]*


- **Perspective Shadows**
    - *[Add description here]*


- **Reflective Shadows**
    - *[Add description here]* *(Currently Disabled)*


- **Transparent Shadows**
    - *[Add description here]* *(Currently Disabled)*


- **Primary Viewports**
    - Draws the scene through the standard render pipeline path, for regular possessed camera viewports.


- **Secondary Viewports**
    - Renders in a low-quality Forward+ style, no early depth and aggressive MSAA usage. Typically used for dynamic reflection cubemaps.



### Renderer Features

- **Enable Lightmapping**
    - *[Add description here]*


- **Receive Opaque Shadows**
    - *[Add description here]*


- **Receive Transparent Shadows**
    - *[Add description here]*


- **Enable Skinned Velocities**
    - *[Add description here]*



### Supported Geometry

- **Static Meshes**
    - *[Add description here]*

- **Skinned Meshes**
    - *[Add description here]* *(Currently Disabled)*

- **Terrain**
    - *[Add description here]* *(Currently Disabled)*

- **Billboards**
    - *[Add description here]* *(Currently Disabled)*

- **Particles**
    - *[Add description here]* *(Currently Disabled)*

## Decal Pipeline Signature

##  Pipeline Signature

# Input Parameters
