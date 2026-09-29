# SDT4.Managed.Core

## Namespaces

### `SDT4.Managed.Core`

| Type | Description |
| --- | --- |
| [Actor](./actor.md) | Represents an entity in the scene hierarchy with associated lifecycle, components, and hierarchy management. |
| [ActorHandle](./actorhandle.md) | Represents a lightweight, zero-allocation handle wrapping an actor in a scene. |
| [AppInstance](./appinstance.md) | Represents the running application instance, providing system metadata, resource management, and service capabilities. |
| [AppLoadContext](./apploadcontext.md) | Contains the application load information when the game initially loads. |
| [InstanceBuild](./instancebuild.md) | Specifies the target configuration and environment under which the application instance is executing. |
| [Mobility](./mobility.md) | Defines the movement and transform mutability behaviour of an actor within a scene. |
| [ResourceManager](./resourcemanager.md) |  |
| [Scene](./scene.md) | Represents the primary scene graph container managing actor hierarchies, components, and execution lifecycles. |
| [Threads](./threads.md) |  |

### `SDT4.Managed.Core.Asset`

| Type | Description |
| --- | --- |
| [AssetErrorCode](./asset/asseterrorcode.md) | Represents the status or error state resulting from an asset management or load operation. |
| [AssetId](./asset/assetid.md) | Represents an immutable identifier for an asset, wrapping its string path or name and providing access to its corresponding unique identifier. |
| [AssetLoadResult&lt;TResource&gt;](./asset/assetloadresult`1.md) | Represents the result of an asset loading operation, encapsulating an outcome status code and the loaded resource instance if successful. |
| [AssetType](./asset/assettype.md) | Defines the supported asset types within the engine. |
| [IResourceMapping](./asset/iresourcemapping.md) | Defines a contract for associating a managed resource type with its engine-level `AssetType`. |
| [MaterialAsset](./asset/materialasset.md) | A material asset |
| [ModelAsset](./asset/modelasset.md) | A 3D Model asset |
| [PrefabAsset](./asset/prefabasset.md) | A prefab asset |
| [Resource](./asset/resource.md) | Serves as the abstract base class for engine resources backed by native memory and control blocks. |
| [SceneAsset](./asset/sceneasset.md) | A scene asset |

### `SDT4.Managed.Core.Attributes`

| Type | Description |
| --- | --- |
| [ReturnPinNameAttribute](./attributes/returnpinnameattribute.md) | Allows giving a name to a return value, reflecting in the visual script UI. |
| [ScriptCategoryAttribute](./attributes/scriptcategoryattribute.md) | Allows categorising a member into a hierarchy in the V-Script Node Context Menu Valid categories contain strictly only alphanumeric characters, and are separated with a pipe \|              Valid categories include: * "Input\|Utility": all members fall under "Input" &gt; "Utility" * "MyHelpers": all members fall under "MyHelpers" * "Audio and Music\|Controls": all members fall under "Audio and Music" &gt; "Controls"              Note that if `FlattenType` is set to `false`, and this attribute is applied onto a class/struct/interface/enum, the type <em>itself</em> will fall under the category.  For instance for a class MyClass with  `FlattenType` set to false: * "Input\|Helpers": all members fall under "Input" &gt; "Utility" &gt; "MyClass" |
| [ScriptComplexityAttribute](./attributes/scriptcomplexityattribute.md) | Specifies a method that does not have side effects. |
| [ScriptComputationalComplexity](./attributes/scriptcomputationalcomplexity.md) | Specifies the expected computational overhead or workload category of a function. |
| [ScriptEventAttribute](./attributes/scripteventattribute.md) | Defines a virtual method to be an event |
| [ScriptGeneratedAttribute](./attributes/scriptgeneratedattribute.md) | A reserved attribute for visual scripts. |
| [ScriptHiddenAttribute](./attributes/scripthiddenattribute.md) | Hides a target from the visual script environment |
| [ScriptImpureAttribute](./attributes/scriptimpureattribute.md) | Specifies a method that does have side effects. |
| [ScriptPureAttribute](./attributes/scriptpureattribute.md) | Specifies a method that does not have side effects. |
| [ScriptWildcardAttribute](./attributes/scriptwildcardattribute.md) | Defines a parameter to be a type that takes any form. |

### `SDT4.Managed.Core.Capabilities`

| Type | Description |
| --- | --- |
| [ICapability](./capabilities/icapability.md) | Base capabilities indicator |
| [ILocalizationCapability](./capabilities/ilocalizationcapability.md) | Defines a localisation capability |
| [INetworkingCapability](./capabilities/inetworkingcapability.md) | Defines a networking capability |
| [IRenderingCapability](./capabilities/irenderingcapability.md) | Defines a rendering capability |
| [IWindowingCapability](./capabilities/iwindowingcapability.md) | Defines a windowing capability |

### `SDT4.Managed.Core.Components`

| Type | Description |
| --- | --- |
| [CameraComponent](./components/cameracomponent.md) | Represents a camera component attached to an actor, defining view and projection parameters for scene rendering. |
| [DirectionalLightComponent](./components/directionallightcomponent.md) | Represents a directional light component attached to an actor. |
| [IActorComponent](./components/iactorcomponent.md) |  |
| [Mesh3DComponent](./components/mesh3dcomponent.md) | Represents a 3D mesh component attached to an actor for rendering geometry. |
| [MeshMaterialCollection](./components/meshmaterialcollection.md) | Provides access to the collection of material assets assigned to a `Mesh3DComponent`. |
| [PointLightComponent](./components/pointlightcomponent.md) | Represents an omnidirectional point light component attached to an actor. |
| [ProjectionMode](./components/projectionmode.md) | Defines the projection modes supported by a `CameraComponent`. |
| [SpotLightComponent](./components/spotlightcomponent.md) | Represents a spot light component attached to an actor, emitting light in a cone shape. |
| [Transform3DComponent](./components/transform3dcomponent.md) | Represents a 3D transformation component attached to an actor, defining position, rotation, and scale in local and world space. |

### `SDT4.Managed.Core.Exceptions`

| Type | Description |
| --- | --- |
| [NativeEngineException](./exceptions/nativeengineexception.md) | Exception class for unexpected engine failure. Hopefully this never needs to be triggered, however this is thrown if an unexpected invalid state is reached, that would never in normal circumstances. |

### `SDT4.Managed.Core.Math`

| Type | Description |
| --- | --- |
| [AxisAlignedBox](./math/axisalignedbox.md) | Represents an axis-aligned bounding box (AABB) 3D space defined by minimum and maximum extents. |
| [ColorRgba](./math/colorrgba.md) | Represents an 8-bit per channel 32-bit RGBA colour value. |
| [Constants](./math/constants.md) | Provides mathematical constants and floating-point precision tolerances for single and double precision operations. |
| [EulerAngle](./math/eulerangle.md) | Represents a 3D rotation expressed as intrinsic Euler angles (pitch, yaw, and roll) with a specified rotation order. |
| [EulerOrder](./math/eulerorder.md) | Specifies the sequence in which intrinsic Euler angle rotations are applied around coordinate axes. |
| [IMatrixSpatial&lt;TComponentType, TVectorType, TMatrixType&gt;](./math/imatrixspatial`3.md) | Defines a contract for square spatial transformation matrices operating over numeric component and vector types. |
| [IVectorComparable&lt;TVectorType&gt;](./math/ivectorcomparable`1.md) | Defines a contract for evaluation operations for vector comparison results. |
| [IVectorSpatial&lt;TComponentType, TLengthType, TVectorType, TNormalizedType&gt;](./math/ivectorspatial`4.md) | Defines a contract for spatial vectors providing geometric length and normalisation operations. |
| [Matrix](./math/matrix.md) | Provides utility methods and constants for matrix transformations, conversions, and decompositions. |
| [Matrix2x2f](./math/matrix2x2f.md) | Represents a 2x2 single-precision floating-point matrix arranged in row-major layout. |
| [Matrix3x3f](./math/matrix3x3f.md) | Represents a 3x3 single-precision floating-point matrix arranged in row-major layout. |
| [Matrix4x4f](./math/matrix4x4f.md) | Represents a 4x4 single-precision floating-point matrix arranged in row-major layout, commonly utilised for 3D affine transformations. |
| [MatrixStorage](./math/matrixstorage.md) | Specifies the memory layout or element ordering convention for a matrix. |
| [Quaternion](./math/quaternion.md) | Represents a four-dimensional complex number utilised for 3D spatial rotations. |
| [Scalar](./math/scalar.md) | The math class containing scalar math operations |
| [Vector](./math/vector.md) | The math class containing vector math operations |
| [Vector2b](./math/vector2b.md) | Represents a 2D boolean vector supporting component-wise logical operations. |
| [Vector2d](./math/vector2d.md) | Represents a 2D double-precision floating-point vector. |
| [Vector2f](./math/vector2f.md) | Represents a 2D single-precision floating-point vector. |
| [Vector2i](./math/vector2i.md) | Represents a 2D 32-bit signed integer vector. |
| [Vector3b](./math/vector3b.md) | Represents a 3D boolean vector supporting component-wise logical operations. |
| [Vector3d](./math/vector3d.md) | Represents a 3D double-precision floating-point vector. |
| [Vector3f](./math/vector3f.md) | Represents a 3D single-precision floating-point vector. |
| [Vector3i](./math/vector3i.md) | Represents a 3D 32-bit signed integer vector. |
| [Vector4b](./math/vector4b.md) | Represents a 4D boolean vector supporting component-wise logical operations. |
| [Vector4d](./math/vector4d.md) | Represents a 4D double-precision floating-point vector. |
| [Vector4f](./math/vector4f.md) | Represents a 4D single-precision floating-point vector. |
| [Vector4i](./math/vector4i.md) | Represents a 4D 32-bit signed integer vector. |

### `SDT4.Managed.Core.Script`

| Type | Description |
| --- | --- |
| [ActorScript](./script/actorscript.md) | Represents a scriptable actor that provides a foundational blank slate for custom gameplay behaviours. |
| [ActorScriptToken](./script/actorscripttoken.md) | Initialisation token for `ActorScript`. |
| [IScriptTarget](./script/iscripttarget.md) | Defines a script execution target and is strictly local to the owning client or server. |
| [SceneScript](./script/scenescript.md) | Represents a scriptable scene controller providing lifecycle callbacks across scene execution phases. |
| [SceneScriptToken](./script/scenescripttoken.md) | Initialisation token for `SceneScript`. |
| [ScriptPayload](./script/scriptpayload.md) | Represents payload data supplied during actor script initialisation and creation control. |

### `SDT4.Managed.Core.Threading`

| Type | Description |
| --- | --- |
| [OffThreadAwaiter](./threading/offthreadawaiter.md) |  |
| [OffThreadAwaiter&lt;T&gt;](./threading/offthreadawaiter`1.md) |  |
| [OffThreadTask](./threading/offthreadtask.md) | A task wrapper that explicitly forbids awaiting or blocking on the Master Thread. Prevents deadlocks where work scheduled on the master thread is awaited by the master thread itself. |
| [OffThreadTask&lt;T&gt;](./threading/offthreadtask`1.md) | A generic task wrapper that explicitly forbids awaiting or blocking on the Master Thread. |

### `SDT4.Managed.Core.Utility`

| Type | Description |
| --- | --- |
| [Bitmask&lt;T&gt;](./utility/bitmask`1.md) | Represents a generic bitmask wrapper over an underlying binary integer type, providing bitwise query and manipulation operations. |
| [DebugUtils](./utility/debugutils.md) |  |
| [IDisposeTracker&lt;T&gt;](./utility/idisposetracker`1.md) |  |

### `SDT4.Managed.Core.VScript.Debugging`

| Type | Description |
| --- | --- |
| [VScriptAssertion](./vscript/debugging/vscriptassertion.md) | A reserved class for visual scripts. |
| [VScriptDebugHook](./vscript/debugging/vscriptdebughook.md) | A reserved class for visual scripts. |

### `SDT4.Managed.Core.VScript.Exceptions`

| Type | Description |
| --- | --- |
| [VScriptException](./vscript/exceptions/vscriptexception.md) | Exception class for Visual Script. |
| [VScriptExceptionType](./vscript/exceptions/vscriptexceptiontype.md) |  |

