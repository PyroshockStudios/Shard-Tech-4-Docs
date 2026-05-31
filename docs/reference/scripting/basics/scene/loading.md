# Loading the Scene

As shown in the [Entry Point](../entrypoint.md) guide, to get our scene, we use the [IResourceManager](../../modules/sdt4.managed.core/iresourcemanager.md) to load our scene. 

## Loading Resources

The asset interface for _Scenes_ is [ISceneAsset](../../modules/sdt4.managed.core/asset/isceneasset.md). Loading is very straightforward, and we will once again use modern C# async and await.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
// ...
AppInstance instance = /*...*/;
IResourceManager resourceManager = instance.ResourceManager;
// Use use AssetID for referencing assets.
var sceneAsset = new AssetID("Master/MyScene.sdt");

// LoadAsset<TResource>() returns a Task on which we can await the ISceneAsset.
var mySceneResult = await resourceManager.LoadAsset<ISceneAsset>(sceneAsset);
// ...  
```

## Instantiating the scene

Once the scene asset has been loaded, it is time to _instantiate_ it. This is seperate from loading for the following reasons:

1. It allows restoring scene state quickly without reloading the entire asset
2. It enables easier management of multiple concurrent scene load operations.

```csharp
// ...  
// You should check load results, however for the sake of brevity, 
// we will assume it loaded correctly.
Scene scene = mySceneResult.Resource!.CreateScene();
// Start() initialises the scene script.
scene.Start();
// ... 
```