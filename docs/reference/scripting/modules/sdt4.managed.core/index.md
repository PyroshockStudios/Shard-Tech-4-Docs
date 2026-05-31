# SDT4.Managed.Core

## Namespaces

### `SDT4.Managed.Core`

| Type | Description |
| --- | --- |
| [Actor](./actor.md) |  |
| [AppExitRequest](./appexitrequest.md) |  |
| [AppInstance](./appinstance.md) |  |
| [AppLoadContext](./apploadcontext.md) | Contains the application load information when the game initially loads. |
| [InstanceEnvironment](./instanceenvironment.md) |  |
| [IResourceManager](./iresourcemanager.md) |  |
| [Scene](./scene.md) |  |
| [Thread](./thread.md) |  |

### `SDT4.Managed.Core.Asset`

| Type | Description |
| --- | --- |
| [AssetErrorCode](./asset/asseterrorcode.md) |  |
| [AssetID](./asset/assetid.md) |  |
| [AssetLoadResult&lt;TResource&gt;](./asset/assetloadresult`1.md) |  |
| [AssetType](./asset/assettype.md) |  |
| [IConvexHullAsset](./asset/iconvexhullasset.md) |  |
| [IMaterialAsset](./asset/imaterialasset.md) |  |
| [IModelAsset](./asset/imodelasset.md) |  |
| [IPrefabAsset](./asset/iprefabasset.md) |  |
| [IResource](./asset/iresource.md) |  |
| [ISceneAsset](./asset/isceneasset.md) |  |
| [ISkeletonAsset](./asset/iskeletonasset.md) |  |
| [ITexture2DAsset](./asset/itexture2dasset.md) |  |
| [ITrimeshAsset](./asset/itrimeshasset.md) |  |

### `SDT4.Managed.Core.Attributes`

| Type | Description |
| --- | --- |
| [AssetStringFieldEditPropertiesAttribute](./attributes/assetstringfieldeditpropertiesattribute.md) |  |
| [ExposeFieldAttribute](./attributes/exposefieldattribute.md) |  |
| [ExposeMethodAttribute](./attributes/exposemethodattribute.md) |  |
| [GameEntryAttribute](./attributes/gameentryattribute.md) | Defines the application entry point. Can only be applied on one single method in the entire application. Must be applied on a static method with a single <see cref="T:SDT4.Managed.Core.AppLoadContext" /> input parameter. |
| [NumericFieldEditPropertiesAttribute](./attributes/numericfieldeditpropertiesattribute.md) |  |
| [ReturnPinNameAttribute](./attributes/returnpinnameattribute.md) |  |
| [ScriptEventAttribute](./attributes/scripteventattribute.md) |  |
| [ScriptGeneratedAttribute](./attributes/scriptgeneratedattribute.md) |  |
| [ScriptHiddenAttribute](./attributes/scripthiddenattribute.md) |  |
| [ScriptPure](./attributes/scriptpure.md) |  |
| [ScriptWildcardAttribute](./attributes/scriptwildcardattribute.md) |  |

### `SDT4.Managed.Core.Capabilities`

| Type | Description |
| --- | --- |
| [ICapability](./capabilities/icapability.md) | Base capabilities indicator |
| [ILocalizationCapability](./capabilities/ilocalizationcapability.md) | Defines a localisation capability |
| [INetworkingCapability](./capabilities/inetworkingcapability.md) | Defines a networking capability |
| [IRendererCapability](./capabilities/irenderercapability.md) | Defines a renderer capability |
| [IWindowingCapability](./capabilities/iwindowingcapability.md) |  |

### `SDT4.Managed.Core.Components`

| Type | Description |
| --- | --- |
| [AbstractComponent](./components/abstractcomponent.md) |  |
| [BoxVolumeComponent](./components/boxvolumecomponent.md) |  |
| [CameraComponent](./components/cameracomponent.md) |  |
| [ColorGrading](./components/colorgrading.md) |  |
| [DeferredDecalComponent](./components/deferreddecalcomponent.md) |  |
| [DirectionalLightComponent](./components/directionallightcomponent.md) |  |
| [HDR](./components/hdr.md) |  |
| [Mesh3DComponent](./components/mesh3dcomponent.md) |  |
| [Mobility](./components/mobility.md) |  |
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

### `SDT4.Managed.Core.Graphics`

| Type | Description |
| --- | --- |
| [CameraProjection](./graphics/cameraprojection.md) |  |

### `SDT4.Managed.Core.Math`

| Type | Description |
| --- | --- |
| [AxisAlignedBox](./math/axisalignedbox.md) |  |
| [ITransform3D](./math/itransform3d.md) |  |
| [IVectorComparable](./math/ivectorcomparable.md) |  |
| [IVectorSpatial&lt;TGenType&gt;](./math/ivectorspatial`1.md) |  |
| [Matrix3x3f](./math/matrix3x3f.md) |  |
| [Matrix4x4f](./math/matrix4x4f.md) |  |
| [Quaternion](./math/quaternion.md) |  |
| [SMath](./math/smath.md) |  |
| [Vector2b](./math/vector2b.md) |  |
| [Vector2d](./math/vector2d.md) |  |
| [Vector2f](./math/vector2f.md) |  |
| [Vector3b](./math/vector3b.md) |  |
| [Vector3d](./math/vector3d.md) |  |
| [Vector3f](./math/vector3f.md) |  |
| [Vector4b](./math/vector4b.md) |  |
| [Vector4d](./math/vector4d.md) |  |
| [Vector4f](./math/vector4f.md) |  |

### `SDT4.Managed.Core.Native`

| Type | Description |
| --- | --- |
| [NativeQuaternion](./native/nativequaternion.md) |  |
| [NativeVector2d](./native/nativevector2d.md) |  |
| [NativeVector2f](./native/nativevector2f.md) |  |
| [NativeVector3d](./native/nativevector3d.md) |  |
| [NativeVector3f](./native/nativevector3f.md) |  |
| [NativeVector4d](./native/nativevector4d.md) |  |
| [NativeVector4f](./native/nativevector4f.md) |  |

### `SDT4.Managed.Core.Script`

| Type | Description |
| --- | --- |
| [ActorScript](./script/actorscript.md) |  |
| [IScriptTarget](./script/iscripttarget.md) |  |
| [PropScript](./script/propscript.md) |  |
| [SceneScript](./script/scenescript.md) |  |
| [ScriptPayload](./script/scriptpayload.md) |  |

### `SDT4.Managed.Core.Utility`

| Type | Description |
| --- | --- |
| [Bitmask&lt;T&gt;](./utility/bitmask`1.md) |  |

