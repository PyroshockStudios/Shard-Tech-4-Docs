# Loading the Scene

As shown in the [Entry Point](../entrypoint.md) guide, to get our scene, we use the [ResourceManager](../../../../cs-api-ref/sdt4.managed.core/resourcemanager.md) to load our scene. 

## Loading Resources

The asset interface for _Scenes_ is [SceneAsset](../../../../cs-api-ref/sdt4.managed.core/asset/sceneasset.md). Loading is very straightforward, and we will once again use modern C# async and await.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
// ...
AppInstance instance = /*...*/;
ResourceManager resourceManager = instance.ResourceManager;
// Use use AssetID for referencing assets.
var sceneAsset = new AssetID("Master/MyScene.sdt");

// LoadAssetAsync<TResource>() returns a Task on which we can await the SceneAsset.
var mySceneResult = await resourceManager.LoadAssetAsync<SceneAsset>(sceneAsset);
// ...  
```

## Instantiating the scene

Once the scene asset has been loaded, it is time to _instantiate_ it. This is separate from loading for the following reasons:

1. It allows restoring scene state quickly without reloading the entire asset
2. It enables easier management of multiple concurrent scene load operations.

```csharp
// ...  
// You should check load results, however for the sake of brevity, 
// we will assume it loaded correctly.
Scene scene = mySceneResult.Resource!.CreateScene("My scene");
// Start() initialises the scene script. This must be performed on the main thread!
scene.Start();
// scene.StartAsync() is an alternative, and allows concurrent ticking.
// ... 
```

!!! danger
    Any calls to the [Scene](../../../../cs-api-ref/sdt4.managed.core/scene.md) object **MUST** be performed on the [master thread](../../../../cs-api-ref/sdt4.managed.core/threads.md).