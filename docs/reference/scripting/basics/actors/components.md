# Entity Component System

Actors hold components that attach properties to them. Components are hard tied to their native C++ counterparts, meaning they provide access into the fast cache-friendly components. Unfortunately, it is **NOT** possible to define custom components, however the existing list should be extensive enough to provide sufficient functionality.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
// ...
Actor actor = /*...*/;

foreach (var component in actor.EnumerateComponents())
{
    // Identifier is a GUID that is unique to each component type.
    DebugConsole.Print(component.Identifier.ToString());
    DebugConsole.Print(component.GetType().ToString());
}
```

## Accessing Components

Components can be added, removed, accessed, or queried with the following functions:

- `AddComponent<TComponent>` adds a component and returns a reference.  
!!! note
    If the component exists, all of its properties will be reset to default values.
- `RemoveComponent<TComponent>` removes the component from the actor. If the component does not exist an exception will be raised.
- `GetComponent<TComponent>` returns a reference to the component. If the component does not exist, an exception will be raised.
- `HasComponent<TComponent>` returns a boolean indicating whether the component exists or not.

```csharp
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
// ...
Scene scene = /*...*/;
Actor actor = scene.CreateEmptyActor(name: "Mesh");
DebugConsole.Print($"{actor.HasComponent<Mesh3DComponent>()}"); // prints false
var meshComp = actor.AddComponent<Mesh3DComponent>();
DebugConsole.Print($"{actor.HasComponent<Mesh3DComponent>()}"); // prints true
// start accessing the component
meshComp.
```
