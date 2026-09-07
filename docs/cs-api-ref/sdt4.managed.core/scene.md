# Scene

## Summary
Scene object that contains all actors and lifecycle.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](./threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.
    
!!! important
    This class <strong>MUST</strong> be disposed manually.

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class Scene
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Scene**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IDisposeTracker&lt;Scene&gt;](./utility/idisposetracker`1.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; NativeHandle` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Throws an [ObjectDisposedException](https://learn.microsoft.com/dotnet/api/system.objectdisposedexception) if this is null. |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |


##### `NativeHandle` Remarks
!!! warning
    Not for public access, usually not needed anyway.


---

## Methods

#### public static [Scene](./scene.md) CreateEmptyScene([String?](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Creates an empty scene with no actors.

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): Optional debug name


**Returns:**

- [Scene](./scene.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Start()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Stop()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Reparent([Actor](./actor.md) newParent, [Actor](./actor.md) child)

**Parameters:**

- `newParent` ([Actor](./actor.md)): 

- `child` ([Actor](./actor.md)): 


---
#### public [Actor](./actor.md) CreateEmptyActor([String?](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) isStationary)

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): 

- `isStationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor?](./actor.md) CreatePrefabActor([PrefabAsset](./asset/prefabasset.md) prefab, [String?](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) isStationary, [Object?](https://learn.microsoft.com/dotnet/api/system.object) payload)


**Summary:**
Creates an actor from a prefab asset. This will instantiate a new instance of actors from the prefab chain,
and optionally initialise a script if the prefab has one.

**Parameters:**

- `prefab` ([PrefabAsset](./asset/prefabasset.md)): Prefab asset to create the actor from

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): Optional actor name, if null, no name is given.

- `isStationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Advanced: if the actor should be treated as a stationary object. This means the actor is NOT allowed to alter positions or state.

- `payload` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): Optional script payload that is provided in the [ActorScript.OnCreate](./script/actorscript.md#oncreate) function


**Returns:**

- [Actor?](./actor.md): A valid actor if the instantiation was <strong>NOT</strong> veto'd

---
#### public [Actor?](./actor.md) GetActorFromId([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) id)


**Summary:**
Gets an actor from an ID relative to the scene root.

**Parameters:**

- `id` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): The ID relative to the scene root


**Returns:**

- [Actor?](./actor.md): A valid actor if an actor with the ID exists

---
#### public [Actor?](./actor.md) GetActorFromGuid([Guid](https://learn.microsoft.com/dotnet/api/system.guid) guid)


**Summary:**
Gets an actor from an absolute GUID.

**Parameters:**

- `guid` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): The GUID of the actor


**Returns:**

- [Actor?](./actor.md): A valid actor if an actor with the GUID exists

---
#### public [IEnumerable&lt;TScript&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateActorsOfScript&lt;TScript&gt;([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) canBeDerived)

**Parameters:**

- `canBeDerived` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- [IEnumerable&lt;TScript&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public [IEnumerable&lt;Actor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateActorsWithComponent&lt;TComponent&gt;(TComponent component)

**Parameters:**

- `component` (TComponent): 


**Returns:**

- [IEnumerable&lt;Actor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) KillActor([Actor](./actor.md) actor)

**Parameters:**

- `actor` ([Actor](./actor.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()


**Summary:**
Releases all scene resources and destroys all actors.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---