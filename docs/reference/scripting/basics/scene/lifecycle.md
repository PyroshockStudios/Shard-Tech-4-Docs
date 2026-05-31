# Stopping after Starting

As we've seen beforehand in [Loading your Scene](./loading.md), we loaded and instantiated the scene. Now we will look at stopping and unloading the scene.

## Graceful Termination

We have loaded our scene, and let's say we want to load another scene in, and unload the current one. While concurrent scenes can be managed, we will first take a look at unloading the current scene.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
// ...
IResourceManager resourceManager = /*...*/;
ISceneAsset myScene = /*...*/;
Scene scene = /*...*/;

// Finish using the scene
// ...

// Stop the simulation
scene.Stop();

```

Now since the simulation has stopped, we must unload the resources to free up memory. Both [Scene](../../modules/sdt4.managed.core/scene.md) and [ISceneAsset](../../modules/sdt4.managed.core/asset/isceneasset.md) implement the [full Dispose() pattern](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose#dispose-and-disposebool). This is to ensure mistakes do not lead to memory leaks, and that explicit control can be given to the developer on when resources _must_ be freed.

To ensure the scene is destroyed and does not hold references to other resource, and all actors are destroyed, we can call `Dispose()` on the scene and scene asset.

```csharp
// ...
scene.Dispose();
// If you are not creating the scene anymore, you can dispose myScene.
// myScene.Dispose();
```

## Concurrent Scene Management

The power of Shard Tech 4 is to work concurrently with data, without arbitrary limitations, allowing you to have full control over resource management and lifecycle.


```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Asset;
// ...
IResourceManager resourceManager = /*...*/;
Scene lobby = /*...*/;
var loadingScene = await resourceManager.LoadAsset<ISceneAsset>(...);

// Lets say the user is doing a complex operation, and lets mask the loading with a nice loading screen.

Scene loading = loadingScene.Resource!.CreateScene();
loading.Start();

// In the Viewports section, we will see how we can switch rendering scenes while simulating both simultanesously!
// ...
// And now we finish loading, and can continue, and remember to clean up!

loading.Stop();
loading.Dispose();

// ...
// Finally, the user quits the game, lets stop the main scene

lobby.Stop();
lobby.Dispose();

// Free our loading screen scene, we wont be using it anymore.
loadingScene.Dispose();

```