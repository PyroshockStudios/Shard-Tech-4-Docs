# Spawning

## Invoking Props (PropScript)

Props are the most straight forward to invoke, as they are [non-phaseable](./phaseability.md#non-phaseable), meaning they do not require any physical presence, and thus have no [Resource](../../modules/sdt4.managed.core/asset/resource.md) to be loaded. This is the fastest way to invoke a script.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;
// ...
class MyScript : PropScript 
{
    // REQUIRED: The engine initialises the prop by invoking it with a token.
    MyScript(PropScriptToken token) : base(token) {}

    // Implementation
}
// ...
Scene scene = /*...*/;
// OnCreate() is immediatelly called, together with OnSpawn() if the scene is running. 
// If the scene is not running, the script is queued until Start[Async] is called,
// where OnBegin() is called instead 
// Template argument is *required* to know which script to instantiate.
MyScript? script = scene.InvokeProp<MyScript>();

// Removing the prop from the scene is required, or the prop will not stop execution
// This will invoke OnKill() and OnDestroy().
// scene.KillProp(script);

// If the prop is never removed, OnEnd() will be invoked once the scene stops, 
// followed by OnDestroy().
```

## Creating Prefabs (ActorScript)

Prefabs are a bit more involved, as ActorScripts are **always** tied to a prefab. 

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;
// ...
class MyPrefabScript : ActorScript 
{
    // REQUIRED: The engine initialises the actor by invoking it with a token.
    MyPrefabScript(ActorScriptToken token) : base(token) {}

    // Implementation
}
// ...
Scene scene = /*...*/;
PrefabAsset prefab = /*...*/; // loaded using the ResourceManager from the AppInstance!

// OnCreate() is immediatelly called, together with OnSpawn() if the scene is running. 
// If the scene is not running, the script is queued until Start[Async] is called,
// where OnBegin() is called instead.
// Template argument is *optional*, and will return an Actor by default.
MyPrefabScript? script = scene.CreatePrefabActor<MyPrefabScript>(prefab);

```

## Payloads

Prop- and ActorScripts may have a [payload](../../modules/sdt4.managed.core/script/scriptpayload.md) bound to them, which can be used for various state management.

This payload is referenced in the `OnCreate` method, where it carries custom state information


```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;
// ...
class MyPrefabScript : ActorScript 
{
    MyPrefabScript(ActorScriptToken token) : base(token) {}

    protected override void OnCreate(ScriptPayload payload) 
    {
        // payload.Veto allows cancelling the instantiation, 
        // and abort the OnCreate() chain for nested prefabs!
        
        // payload.State holds an optional object with state. 
        // This is useful for physics actors where setting an 
        // initial transform is vital. 
        var translation = (Vector3d)payload.State ?? Vector3d.Zero;
        this.GetComponent<Transform3DComponent>().Translation = translation;
    }
}
// ...
Scene scene = /*...*/;
scene.CreatePrefabActor<MyPrefabScript>(prefab, payload: new Vector3d(1000.0, 10.0, 5000.0));

```

!!! note
    Due to the possibility of Veto'ing the creation, `InvokeProp<>()` and `CreatePrefabActor<>()` may return **NULL**.