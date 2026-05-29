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

### Render Pass

#### Pass Mode
Controls which pass the material shader will be rendered in. This will have an influence on the possible features that this shader may access.

**Options:**

- Opaque G-Buffer (Default)
    - Renders the material data to the G-Buffer. Shaders can only have *Opaque* or *Alpha Clip* blend modes, and participate in the Early Z pass. Material parameters may be limited due to G-Buffer constraints.
- Transparent T-Buffer
    - Renders the shaded material data to the order-independent transparency buffer. Requires *OIT Blend* and does not support depth writes. 
- Forward
    - Directly shades the material data with the lighting information to the lighting buffer. Shaders can have any blend mode except *OIT Blend* and participate in the Early Z pass. Does not support MSAA.
- Forward No Early Z
    - Supports same features as *Forward*, except depth is not written in the Early Z pass. MSAA is supported.
- Post Composite Overlay
    - Renders the material after all post processing effects, with a low dynamic colour range [0, 1]. Recommended for UI-like elements that shouldn't be affected by post processing such as bloom. Shaders can have any blend mode except *OIT Blend*. 

### Shading

#### Lighting Model
Controls how the material will be shaded, and enables usage of certain material parameters.

**Options:** 

- Unlit BSDF
    - Does not perform shading, and outputs a single colour.
- Standard BSDF (Default)
    - Recommended option for most materials, is the cheapest lit shading model, and supports common material parameters. 
- Clearcoat BSDF
    - Contains the same parameters as *Standard BSDF- but with *Clear Coat* parameters. Specular lighting is more costly, as lighting is computed twice for the base layer and the clear coat layer. 
- Cloth BSDF
    - Contains the same parameters as *Standard BSDF* but with *Sheen* parameters. 
- Anisotropic BSDF
    - Contains the same parameters as *Standard BSDF* but with an *Anisotropic* parameter. Lighting is significantly more expensive as it must be evaluated from multiple angles.
- Subsurface BSDF
    - Adds subsurface shading parameters to give the material translucent effects. 
- Thin Translucent BSDF
    - Simplified version of *Surface BSDF* that assumes a thin surface. Lighting is more costly as it computes front and back side lighting simulatenously. Recommended for foliage.

### Blend State

#### Blend Mode

Changes how the material's output colour is combined with the colours already present in the background render target.

**Options:**

- Opaque (Default)
    - Directly draws object onto the scene with no alpha information, and is thus the cheapest.
- Alpha Clip
    - Discards fragments if *Opacity Mask* falls below the *Alpha Cuttoff* threshold. When multi sampled *A2C* is enabled, this maps to a tight coverage based on [Esoteric Alpha To Coverage](https://bgolus.medium.com/anti-aliased-alpha-test-the-esoteric-alpha-to-coverage-8b177335ae4f)
- Alpha Blend
    - Blends fragments with the standard linear interpolation. 
    !!! note
        This blend mode is **not** order independent and may cause primitives to artifact.
- Additive Blend
    - Blends fragments with an additive blend operation.
- Multiplicative Blend
    - Blends fragments with a multiplicative blend operation.
- OIT Blend
    - Uses order independent rendering techniques to perform transparency effects. 
    !!! note 
        This blend is only enabled if *Pass Type* is set to **Transparent T-Buffer**

#### Alpha Cutoff

Determines the threshold value at which pixels are completely discarded (clipped) when rendering. Any alpha value below this threshold will not be drawn, resulting in sharp, hard edges instead of smooth gradients.

!!! note
    This is only active when Blend Mode is set to **Alpha Clip**.

#### Draw Order Hint

Provides a manual sorting priority offset for transparent or overlapping objects. This is useful for resolving depth sorting artifacts where the engine struggles to automatically determine which transparent material should render in front of another.

### Rasteriser State

#### Polygon Mode

Defines how the rasteriser translates the geometry's vertices into pixels on the screen. Usually modified for debugging purposes or specific stylistic wireframe effects.

**Options:**

- Filled (Default)
    - Fills the polygons of the mesh entirely.
- Wireframe
    - Only renders edges of polygons. Significantly increases rasteriser load.

#### Culling

Determines which faces of a polygon are discarded (culled) based on their normal direction relative to the camera. This optimises performance by skipping faces that point away from the viewer. Assumed winding order is *Clockwise*.

**Options:**

- None
    - Both front and back sides are visible.
- Back (Default)
    - Back side is culled, only front side is visible.
- Front
    - Front side is culled, Only back side is visible.

### Depth State

#### Depth Modify

Allows modification of depth values through Pixel Depth Offset. 

!!! note
    Since Shard Tech 4 is primarily Reverse Z, negative values move further *away* from the camera. 
!!! note 
    On pass mode **Opaque G-Buffer** this can visually alter lighting information, as position information is inferred from depth.

**Options:**

- No Modify (Default)
    - Disables depth modification.
- Modify
    - Allows changing depth values to be either larger or smaller. Not recommended as this disables any depth test optimisations.
- Conservative Less Equal
    - Allows changing depth values to only be smaller or equal (further from the camera).
- Conservative Greater Equal
    - Allows changing depth values only to be larger or equal (closer to the camera).

### Geometry Manipulation

#### Vertex Offset Mode

Allows modification of vertex positions, and that the node either designates local or world offset. 
!!! note
    Local offset is **post-skinning**! This is due to vertex transform caching for improved efficiency!

**Options:** 

- No Offset (Default)
    - Disables custom vertex transforms and displacement.
- Local Position Offset
    - Maps *Vertex Position Offset* to be relative to the local pose (pre transform). 
- World Position Offset
    - Maps *Vertex Position Offset* to be relative to the world pose (post transform). 

#### Tessellation Mode

Enables subdivision of vertices for improved geometry quality. 
!!! warning
    Performance may significantly degrade with this rendering feature! Please use with caution! Consider using more subdivided meshes instead.

**Options:**

- No Tessellation (Default)
    - Disables tessellation.
- Triangles
    - Uses 3 control points for tessellation. This is to be used on common triangle based meshes.
- Quads
    - Uses 4 control points for tessellation. (Not usable at the moment)

#### Tessellation Partitioning

Controls how the tessellation factors are interpreted when dividing an edge, dictating how new vertices are introduced and how smoothly geometry transitions between different levels of detail.

**Options:**

- Integer
    - Uses integer partitioning.
- Fractional Even
    - Uses even fractioning.
- Fractional Odd
    - Uses odd fractioning.

!!! note
    These settings are only available when *Tessellation Mode* is **not** set to **No Tessellation**.

#### Multi Sample State

#### MSAA Mode

Enhance quality through MSAA usage. Only supported on Forward render modes.

**Options:**

- No MSAA (Default)
    - Disables MSAA
- MSAA Only
    - Uses multiple samples to evaluate geometric anti-aliasing.
- A2C Only
    - Maps output alpha values to MSAA coverage. 
    !!! note
        Different renderer backends as well as different vendors **may** implement this visually differently, causing potential visual differences.

!!! note
    MSAA is only available when *Pass Mode* is set to **Forward No Early Z**.

### Render Systems

- **Orthogonal Shadows**
    - Determines if this material casts shadows from directional lights (which use orthogonal projections).
- **Perspective Shadows**
    - Determines if this material casts shadows from local light sources, such as point lights or spot lights (which use perspective projections).
- **Reflective Shadows**
    - Determines if this material generates *Global Illumination* data on shadow maps. *(Currently Disabled)*
- **Transparent Shadows**
    - Enables the material to cast coloured or partial shadows based on its transparency/alpha values. *(Currently Disabled)*
- **Primary Viewports**
    - Draws the scene through the standard render pipeline path, for regular possessed camera viewports.
- **Secondary Viewports**
    - Renders in a low-quality Forward+ style, no early depth and aggressive MSAA usage. Typically used for dynamic reflection cubemaps.


### Renderer Features

- **Enable Lightmapping**
    - Allows the material to receive baked, static lighting information from pre-computed lightmaps.
- **Receive Opaque Shadows**
    - Enables the material to receive shadows cast by opaque objects in the scene. Increases fragment shader load.
- **Receive Transparent Shadows**
    - Enables the material to receive soft or coloured shadows cast by transparent objects. Increases fragment shader load.
- **Enable Skinned Velocities**
    - Calculates accurate per-vertex motion vectors for animated models. This is essential for rendering high-quality motion blur on moving characters. Increases memory usage and vertex shader load.

### Supported Geometry

- **Static Meshes**
    - Standard 3D geometry with rigid transforms and no skeletal animation.
- **Skinned Meshes**
    - 3D models driven by a skeletal hierarchy (bones) for complex character animations. *(Currently Disabled)*
- **Terrain**
    - Landscape geometry generated dynamically from heightmap data. *(Currently Disabled)*
- **Billboards**
    - 2D camera-facing quads, typically used for distant imposters or foliage. *(Currently Disabled)*
- **Particles**
    - Dynamic geometry spawned and managed by visual effects particle emitters. *(Currently Disabled)*

## Decal Pipeline Signature

## Volumetric Pipeline Signature
## Post Processing Pipeline Signature
## RML Pipeline Signature
## Brush Pipeline Signature

# Input Parameters

To allow reusing shaders across multiple materials, input parameters are a powerful way of sending data to the GPU.

# Shader Editor

Material Shaders are written by method of visual nodes. This is a restriction imposed to optimise shader permutation optimisation.