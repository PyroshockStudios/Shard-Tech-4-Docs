# Script Entry Point

When the game initialises, while loading the startup screen, the entry point is called. This allows for loading game assets and auto while the game starts in the background.

## Defining the entry
An entry point is expected to be defined as `Game.OnInit`, where `OnInit` is a static method with [AppLoadContext](../modules/sdt4.managed.core/apploadcontext.md) as its
sole input parameter. 

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Attributes;
static class Game 
{
    static void OnInit(AppLoadContext appLoadContext) 
    {
        // set up your systems and contexts
    }
}
```
using SDT4.Managed.Core.Asset;

The [AppLoadContext](../modules/sdt4.managed.core/apploadcontext.md) is a data structure containing asynchronous Task objects. 

!!! warning
    The entry point is a **blocking** function, meaning do **NOT** perform blocking tasks in the function, as it will cause the application to either slow down or to hang.

## Loading the AppInstance

The [AppInstance](../modules/sdt4.managed.core/appinstance.md) holds the heart of the engine, which can be used for loading resources, gathering inputs, and start network connections. Below is an example on how to do make use of the asynchronous task using modern C# _async_ and _await_: 

```csharp
using SDT4.Managed.Core;
// ...
// Since the entry point is blocking, we should delegate expensive 
// work to a seperate thread
appLoadContext.InstanceReadyTask.ContinueWith(async (task) =>
{
    // Wait for the instance
    var instance = await task;
    // Now we can use the instance, let's load our scene
    var lobbyAsset = new AssetID("Master/S_Lobby.sdt");
    var loadResult = await instance.ResourceManager.LoadAssetAsync<SceneAsset>(lobbyAsset);
    // Now we can start using our scene 
    // ...
});
```