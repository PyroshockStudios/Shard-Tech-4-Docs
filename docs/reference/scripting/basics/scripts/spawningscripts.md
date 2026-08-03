# Spawning

## Creating Prefabs (ActorScript)

Prefabs are a bit more involved, as ActorScripts are **always** tied to a prefab. 

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Core.Script;
// ...
public class MyPrefabScript : ActorScript 
{
    // REQUIRED: The engine initialises the actor by invoking it with a token.
    protected MyPrefabScript(ActorScriptToken token) : base(token) {}

    // Implementation
}
// ...
Scene scene = /*...*/;
PrefabAsset prefab = /*...*/; // loaded using the ResourceManager from the AppInstance!

// OnCreate() is immediatelly called, together with OnSpawn() if the scene was already running. 
// If the scene is not running, the script is queued until Start[Async] is called.
// Finally OnBegin() is called before the first OnTick/OnStep of this actor.
// A nullable Actor? is returned as the creation may be veto'ed.
MyPrefabScript? script = scene.CreatePrefabActor(prefab) as MyPrefabScript;

```

## Payloads

ActorScripts may have a [payload](../../../../cs-api-ref/sdt4.managed.core/script/scriptpayload.md) bound to them, which can be used for various state management.

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
    Due to the possibility of Vetoing the creation, `InvokeProp<>()` and `CreatePrefabActor<>()` may return **NULL**.