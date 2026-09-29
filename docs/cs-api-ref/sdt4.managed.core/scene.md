# Scene

## Summary
Represents the primary scene graph container managing actor hierarchies, components, and execution lifecycles.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](./threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophic failures as the engine is not designed for concurrent scene mutation.
    
!!! important
    Instances of this class manage native engine allocations and <strong>MUST</strong> be disposed manually.

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
| `public get; NativeHandle` | [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) | Gets the pointer to the underlying native engine scene. |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the display name of this scene, or <see langword="null" /> if unnamed. |


##### `NativeHandle` Remarks
!!! warning
    Intended for internal engine interop; direct access by user scripts is typically unnecessary.


---

## Methods

#### public static [Scene](./scene.md) CreateEmptyScene([String?](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Creates a new empty scene containing no actors.

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): An optional debug or display name to assign to the scene.


**Returns:**

- [Scene](./scene.md): A newly instantiated and owned [Scene](./scene.md) instance.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Start()


**Summary:**
Starts the scene runtime, transitioning all active actors and scripts into their execution state.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Stop()


**Summary:**
Stops the scene runtime, terminating ticking and active script execution.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) ParentActor([ActorHandle](./actorhandle.md) child, [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) parent)


**Summary:**
Attaches a child actor to a specified parent actor in the hierarchy. If the child is already parented, it is unparented first.

**Parameters:**

- `child` ([ActorHandle](./actorhandle.md)): The child actor handle to parent.

- `parent` ([Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1)): The target parent actor handle, or <see langword="null" /> to detach the child to the scene root.


---
#### public [ActorHandle](./actorhandle.md) CreateEmptyActor([String?](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Spawns a new empty actor within the root scope of this scene.

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): An optional name to assign to the actor.


**Returns:**

- [ActorHandle](./actorhandle.md): The handle of the newly created actor.

---
#### public [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) CreatePrefabActor([PrefabAsset](./asset/prefabasset.md) prefab, [String?](https://learn.microsoft.com/dotnet/api/system.string) name, [Object?](https://learn.microsoft.com/dotnet/api/system.object) payload)


**Summary:**
Instantiates an actor hierarchy from a prefab asset into this scene, optionally initialising its attached script.

**Parameters:**

- `prefab` ([PrefabAsset](./asset/prefabasset.md)): The prefab asset to instantiate.

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): An optional name override for the root actor; if <see langword="null" />, default naming is used.

- `payload` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): An optional script payload forwarded to the [ActorScript.OnCreate](./script/actorscript.md#oncreate) hook.


**Returns:**

- [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1): A valid [ActorHandle](./actorhandle.md) if instantiation succeeded; otherwise, <see langword="null" /> if creation was vetoed.

---
#### public [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) GetActorFromId([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) id)


**Summary:**
Resolves an actor handle using an integer identifier relative to the scene root.

**Parameters:**

- `id` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): The root-relative identifier to query.


**Returns:**

- [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1): The resolved [ActorHandle](./actorhandle.md), or <see langword="null" /> if no matching actor exists.

---
#### public [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) GetActorFromGuid([Guid](https://learn.microsoft.com/dotnet/api/system.guid) guid)


**Summary:**
Resolves an actor handle matching a globally unique identifier.

**Parameters:**

- `guid` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): The globally unique identifier to query.


**Returns:**

- [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1): The resolved [ActorHandle](./actorhandle.md), or <see langword="null" /> if no matching actor exists.

---
#### public [IEnumerable&lt;TComponent&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateComponents&lt;TComponent&gt;()


**Summary:**
Enumerates all active components of the specified type across all actors in this scene.

**Returns:**

- [IEnumerable&lt;TComponent&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): An enumerable sequence of matching component instances.

---
#### public [IEnumerable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateActorsByName([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Enumerates all actor handles in this scene that match a specified name string.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name string to match.


**Returns:**

- [IEnumerable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): An enumerable sequence of matching [ActorHandle](./actorhandle.md) instances.

---
#### public [IEnumerable&lt;TActor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateActorsWithScript&lt;TActor&gt;()


**Summary:**
Enumerates all active actor scripts in this scene matching the specified script type.

**Returns:**

- [IEnumerable&lt;TActor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): An enumerable sequence of matching actor script instances.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) KillActor([ActorHandle](./actorhandle.md) actor)


**Summary:**
Destroys the specified actor and cleans up its components, hierarchy bindings, and script instances.

**Parameters:**

- `actor` ([ActorHandle](./actorhandle.md)): The actor handle to destroy.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()


**Summary:**
Releases all unmanaged scene resources and destroys all associated actors.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is a [Scene](./scene.md) referencing the same native scene instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is a [Scene](./scene.md) with matching native pointers; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this scene based on its native pointer address.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a formatted string representation of this scene.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string identifying the scene pointer and name.

---


---