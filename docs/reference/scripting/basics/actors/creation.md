# Creating and Destroying Actors

Actors can be created from a scene, and have all of its properties managed manually.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
// ...
Scene scene = /*...*/;
// Each actor has a unique GUID, based on its scope and local id
Actor gamingActor = scene.CreateEmptyActor(name: "Gaming");

DebugConsole.Print($"Hello {someActor.Name}!"); 
```

Once an actor is no longer needed, you may remove it from the scene, and it will destroy it.

```csharp

scene.RemoveActor(gamingActor);
// gamingActor is no longer valid, do not attempt to use it
DebugConsole.Print($"{gamingActor.IsAlive}"); // prints false!

```

!!! danger
    While we extensively used async and await in the previous [scene guide](../scene/loading.md), you **MUST** use the master thread to perform **ANY** operations on the scene and actors!