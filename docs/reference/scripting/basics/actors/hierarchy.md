# Actor hierarchy

Actors always belong to a specific scene, and cannot be created or managed independently. 

```csharp
using System;
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
// ...
Scene scene = /*...*/;
// Each actor has a unique GUID, based on its scope and local id
Actor someActor = scene.GetActorFromGuid(new Guid("0b2dec00-aa7d-447b-98ce-94e818ad6535"));

DebugConsole.Print($"Local ID = {someActor.LocalId}"); 
DebugConsole.Print($"Scope GUID = {someActor.ScopeId}");
```

## Scope encapsulation

The `LocalId` is relative to the current _scope_; the scope is the encapsulating body of the Actor. Scopes are defined by _prefabs_, and are recursive.

```csharp
// These two print the same!
DebugConsole.Print($"Scope GUID = {someActor.ScopeId}");
DebugConsole.Print($"Scope GUID = {someActor.ScopeRoot?.GlobalId ?? Guid.Empty}");
```

This is a powerful encapsulation as it allows retrieving actors deterministically by scope, once we get into referencing Actors in [ActorScripts](../scripts/scenepropactorscript.md).
