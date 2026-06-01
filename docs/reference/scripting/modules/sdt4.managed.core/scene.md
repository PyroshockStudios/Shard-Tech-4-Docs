# Scene

## Summary
Scene object that contains all actors and lifecycle.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Main Thread. 
    See <see cref="M:SDT4.Managed.Core.Thread.RunLater(System.Threading.ThreadStart)" /> on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class Scene
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Scene**
**Implements:**

##### [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |

---


## Methods

#### public T AsScript&lt;T&gt;()

##### Summary
Gets the <see cref="T:SDT4.Managed.Core.Script.SceneScript" /> instance of this <see cref="T:SDT4.Managed.Core.Scene" /> class.

**Returns:**

- T: A valid T if it is a derived instance of a non-null SceneScript. Returns <strong>NULL</strong> otherwise.

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
#### public [Actor](./actor.md) CreatePrefabActor([IPrefabAsset](./asset/iprefabasset.md) prefab, [String?](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) isStationary, [Object?](https://learn.microsoft.com/dotnet/api/system.object) payload)

##### Summary
Creates an actor from a prefab asset. This will instantiate a new instance of actors from the prefab chain,
and optionally initialise a script if the prefab has one.

**Parameters:**

- `prefab` ([IPrefabAsset](./asset/iprefabasset.md)): Prefab asset to create the actor from

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): Optional actor name, if null, no name is given.

- `isStationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Advanced: if the actor should be treated as a stationary object. This means the actor is NOT allowed to alter positions or state.

- `payload` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): Optional script payload that is provided in the <see cref="M:SDT4.Managed.Core.Script.ActorScript.OnCreate(SDT4.Managed.Core.Script.ScriptPayload)" /> function


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor](./actor.md) GetActorFromId([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) id)

**Parameters:**

- `id` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor](./actor.md) GetActorFromGuid([Guid](https://learn.microsoft.com/dotnet/api/system.guid) guid)

**Parameters:**

- `guid` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor[]](./actor.md) GetActorsWithName([String](https://learn.microsoft.com/dotnet/api/system.string) name)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [Actor[]](./actor.md): 

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
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveActor([Actor](./actor.md) actor)

**Parameters:**

- `actor` ([Actor](./actor.md)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) disposing)

**Parameters:**

- `disposing` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Finalize()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

##### Summary
Releases all scene resources and destroys all actors.

---


---