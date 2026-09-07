# SDT4.Managed.Core

## Namespaces

### `SDT4.Managed.Core`

| Type | Description |
| --- | --- |
| [Actor](./actor.md) | Scene object that contains all actors and lifecycle. |
| [AppInstance](./appinstance.md) |  |
| [AppLoadContext](./apploadcontext.md) | Contains the application load information when the game initially loads. |
| [InstanceBuild](./instancebuild.md) |  |
| [Mobility](./mobility.md) |  |
| [ResourceManager](./resourcemanager.md) |  |
| [Scene](./scene.md) | Scene object that contains all actors and lifecycle. |
| [Threads](./threads.md) |  |

### `SDT4.Managed.Core.Asset`

| Type | Description |
| --- | --- |
| [AssetErrorCode](./asset/asseterrorcode.md) |  |
| [AssetID](./asset/assetid.md) |  |
| [AssetLoadResult&lt;TResource&gt;](./asset/assetloadresult`1.md) |  |
| [AssetType](./asset/assettype.md) |  |
| [ConvexHullAsset](./asset/convexhullasset.md) |  |
| [IResourceMapping](./asset/iresourcemapping.md) |  |
| [MaterialAsset](./asset/materialasset.md) |  |
| [ModelAsset](./asset/modelasset.md) |  |
| [PrefabAsset](./asset/prefabasset.md) |  |
| [Resource](./asset/resource.md) |  |
| [SceneAsset](./asset/sceneasset.md) |  |
| [SkeletonAsset](./asset/skeletonasset.md) |  |
| [Texture2DAsset](./asset/texture2dasset.md) |  |
| [TrimeshAsset](./asset/trimeshasset.md) |  |

### `SDT4.Managed.Core.Attributes`

| Type | Description |
| --- | --- |
| [ActorReferenceAttribute](./attributes/actorreferenceattribute.md) | Allows referencing an actor either locally or globally by its ID. This automatically populates the field with a strong reference to the actor. It can be applied on `Actor` or any class deriving from `ActorScript`. |
| [AssetStringFieldEditPropertiesAttribute](./attributes/assetstringfieldeditpropertiesattribute.md) |  |
| [ExposeFieldAttribute](./attributes/exposefieldattribute.md) |  |
| [ExposeMethodAttribute](./attributes/exposemethodattribute.md) |  |
| [NumericFieldEditPropertiesAttribute](./attributes/numericfieldeditpropertiesattribute.md) |  |
| [ReturnPinNameAttribute](./attributes/returnpinnameattribute.md) | Allows giving a name to a return value, reflecting in the visual script UI. |
| [ScriptCategoryAttribute](./attributes/scriptcategoryattribute.md) | Allows categorising a member into a hierarchy in the V-Script Node Context Menu Valid categories contain strictly only alphanumeric characters, and are seperated with a pipe \|              Valid categories include: * "Input\|Utility": all members fall under "Input" &gt; "Utility" * "MyHelpers": all members fall under "MyHelpers" * "Audio and Music\|Controls": all members fall under "Audio and Music" &gt; "Controls"              Note that if `FlattenType` is set to `false`, and this attribute is applied onto a class/struct/interface/enum, the type <em>itself</em> will fall under the category.  For instance for a class MyClass with  `FlattenType` set to false: * "Input\|Helpers": all members fall under "Input" &gt; "Utility" &gt; "MyClass" |
| [ScriptEventAttribute](./attributes/scripteventattribute.md) | Defines a virtual method to be an event |
| [ScriptGeneratedAttribute](./attributes/scriptgeneratedattribute.md) | A reserved attribute for visual scripts. |
| [ScriptHiddenAttribute](./attributes/scripthiddenattribute.md) | Hides a target from the visual script environment |
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
| [BoxVolumeComponent](./components/boxvolumecomponent.md) |  |
| [CameraComponent](./components/cameracomponent.md) |  |
| [ColorGrading](./components/colorgrading.md) |  |
| [Component](./components/component.md) |  |
| [DeferredDecalComponent](./components/deferreddecalcomponent.md) |  |
| [DirectionalLightComponent](./components/directionallightcomponent.md) |  |
| [HDR](./components/hdr.md) |  |
| [Mesh3DComponent](./components/mesh3dcomponent.md) |  |
| [PhysicsConstraintComponent](./components/physicsconstraintcomponent.md) |  |
| [PointLightComponent](./components/pointlightcomponent.md) |  |
| [PostProcessingComponent](./components/postprocessingcomponent.md) |  |
| [PostProcessingEffect](./components/postprocessingeffect.md) |  |
| [Rigidbody3DComponent](./components/rigidbody3dcomponent.md) |  |
| [SkinnedMeshComponent](./components/skinnedmeshcomponent.md) |  |
| [SpotLightComponent](./components/spotlightcomponent.md) |  |
| [Transform3DComponent](./components/transform3dcomponent.md) |  |
| [WaypointComponent](./components/waypointcomponent.md) |  |
| [WaypointSplinePathPoint](./components/waypointsplinepathpoint.md) |  |
| [WaypointSplinePoint](./components/waypointsplinepoint.md) |  |

### `SDT4.Managed.Core.Exceptions`

| Type | Description |
| --- | --- |
| [NativeEngineException](./exceptions/nativeengineexception.md) | Exception class for unexpected engine failure. Hopefully this never needs to be triggered, however this is thrown if an unexpected invalid state is reached, that would never in normal circumstances. |
| [VisualScriptAssertion](./exceptions/visualscriptassertion.md) | A reserved class for visual scripts. |
| [VisualScriptException](./exceptions/visualscriptexception.md) | Exception class for Visual Script. |
| [VisualScriptExceptionType](./exceptions/visualscriptexceptiontype.md) |  |

### `SDT4.Managed.Core.Graphics`

| Type | Description |
| --- | --- |
| [CameraProjection](./graphics/cameraprojection.md) |  |
| [ColorRgba](./graphics/colorrgba.md) |  |

### `SDT4.Managed.Core.Math`

| Type | Description |
| --- | --- |
| [AxisAlignedBox](./math/axisalignedbox.md) |  |
| [IVectorComparable](./math/ivectorcomparable.md) |  |
| [IVectorSpatial&lt;TGenType&gt;](./math/ivectorspatial`1.md) |  |
| [Matrix3x3f](./math/matrix3x3f.md) |  |
| [Matrix4x4f](./math/matrix4x4f.md) |  |
| [Quaternion](./math/quaternion.md) |  |
| [SMath](./math/smath.md) |  |
| [Vector2b](./math/vector2b.md) |  |
| [Vector2d](./math/vector2d.md) |  |
| [Vector2f](./math/vector2f.md) |  |
| [Vector2i](./math/vector2i.md) |  |
| [Vector3b](./math/vector3b.md) |  |
| [Vector3d](./math/vector3d.md) |  |
| [Vector3f](./math/vector3f.md) |  |
| [Vector3i](./math/vector3i.md) |  |
| [Vector4b](./math/vector4b.md) |  |
| [Vector4d](./math/vector4d.md) |  |
| [Vector4f](./math/vector4f.md) |  |
| [Vector4i](./math/vector4i.md) |  |

### `SDT4.Managed.Core.Script`

| Type | Description |
| --- | --- |
| [ActorScript](./script/actorscript.md) |  |
| [ActorScriptToken](./script/actorscripttoken.md) | Initialisation token for `ActorScript` |
| [IScriptTarget](./script/iscripttarget.md) |  |
| [SceneScript](./script/scenescript.md) |  |
| [SceneScriptToken](./script/scenescripttoken.md) | Initialisation token for `SceneScript` |
| [ScriptPayload](./script/scriptpayload.md) |  |

### `SDT4.Managed.Core.Utility`

| Type | Description |
| --- | --- |
| [Bitmask&lt;T&gt;](./utility/bitmask`1.md) |  |
| [DebugUtils](./utility/debugutils.md) |  |
| [IDisposeTracker&lt;T&gt;](./utility/idisposetracker`1.md) |  |

