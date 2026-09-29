# Actor vs ActorHandle

SDT4 offers a distinction between [ActorHandle](../../../../cs-api-ref/sdt4.managed.core/actorhandle.md) and [Actor](../../../../cs-api-ref/sdt4.managed.core/actor.md). This distinction is for performance reasons, as querying possibly up to thousands of actors will create unnecessary heap allocations.

The difference is that [ActorHandle](../../../../cs-api-ref/sdt4.managed.core/actorhandle.md) is a *readonly struct* whilst [Actor](../../../../cs-api-ref/sdt4.managed.core/actor.md) is a *class*. They both contain the same functionality when it comes to the Actor Component System, however [Actor](../../../../cs-api-ref/sdt4.managed.core/actor.md) is the required class whenever dealing with scripts (see [Scene and Actor Scripts](../scripts/sceneactorscript.md))

```csharp
using System;
using SDT4.Managed.Core;
using SDT4.Managed.Debugging;
// ...
Scene scene = /*...*/;
ActorHandle structActor = scene.CreateEmptyActor("New actor");
Actor classActor = structActor.AsActor(); // This will get a class instance of an actor.
DebugConsole.Print($"ActorHandle              = {someActor}"); 
DebugConsole.Print($"Actor                    = {classActor}");
DebugConsole.Print($"ActorHandle (from Actor) = {classActor.Handle}");
```

## Converting to script instances

When spawning prefabs (see [Spawning Scripts](../scripts/spawningscripts.md)), you may want to access the instance, this cannot be done through [ActorHandle](../../../../cs-api-ref/sdt4.managed.core/actorhandle.md), so you must access using the `AsActor()` or `AsScript<>()` functions. 

```csharp
ActorHandle myPrefabActor = ...;
// Suppose myPrefabActor has "A_MyScript" attached
A_MyScript script = myPrefabActor.AsScript<A_MyScript>()!;
// This is an equivalent statement
script = (myPrefabActor.AsActor() as A_ScriptedActor)!;
```

This power guarantees that **any** [Actor](../../../../cs-api-ref/sdt4.managed.core/actor.md) instance correlates to the underlying script instance, while [ActorHandle](../../../../cs-api-ref/sdt4.managed.core/actorhandle.md) is a performant alternative to allow querying thousands of actors without the overhead of memory allocations or the garbage collector.
