# Creation

Materials allow customising the parameters of [Material Shaders](./materialshader.md) which define the base properties of the material.

Right click on the [Asset Explorer](../assetexplorer.md) background, and select *Create Material*

# Parameters

## Material Shader
Sets the shader that defines the base properties of this material. 

## Parent Material
Sets the material that inherits the shader, and allows property propagation.

## Parameter Overrides
Material parameters are always opt-in, they derive the parameters for inherited materials and the base shader, meaning that any unchanged parameters will assume the parameter of the defining parent. Overriden parameters always reflect the changes defined within that material.