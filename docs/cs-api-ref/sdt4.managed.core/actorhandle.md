# ActorHandle

## Summary
Represents a lightweight, zero-allocation handle wrapping an actor in a scene.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](./threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophic failures as the engine is not designed for concurrent scene mutation.

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct ActorHandle
```
**Implements:**

##### [IEquatable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public readonly NativeHandle` | [UInt32](https://learn.microsoft.com/dotnet/api/system.uint32) | Native entity handle. |
| `public readonly Scene` | [Scene](./scene.md) | Native scene pointer. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; GlobalId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the persistent globally unique identifier of the referenced actor. |
| `public get; ScopeId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the unique identifier of the hierarchy scope containing this actor. |
| `public get; LocalId` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) | Gets the scope-local identifier of the referenced actor. |
| `public get; set; Name` | [String?](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the display or debug name of the actor, or <see langword="null" /> if unnamed. |
| `public get; IsValid` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the actor is a valid, active instance in the scene. |
| `public get; ScopeRoot` | [ActorHandle](./actorhandle.md) | Gets the top-most root actor handle in the current hierarchy scope. If the actor is the top most, it will return itself. |
| `public get; Mobility` | [Mobility](./mobility.md) | Gets the mobility state of this actor (e.g. static, stationary, or dynamic). |
| `public get; Parent` | [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | Gets the handle of this actor's direct parent in the transform hierarchy, or <see langword="null" /> if it has no parent. |
| `public get; Children` | [ActorHandle[]](./actorhandle.md) | Gets an array of handles representing all direct children of this actor in the hierarchy. |
| `public get; Components` | [IActorComponent[]](./components/iactorcomponent.md) | Gets an array containing all components currently attached to this actor. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) HasComponent&lt;TComponent&gt;()


**Summary:**
Determines whether this actor has a component of the specified type attached.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the component is present; otherwise, <see langword="false" />.

---
#### public TComponent GetComponent&lt;TComponent&gt;()


**Summary:**
Retrieves the attached component of the specified type.

**Returns:**

- TComponent: The component instance.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetComponent&lt;TComponent&gt;(out TComponent component)


**Summary:**
Attempts to retrieve an attached component of the specified type.

**Parameters:**

- `component` (TComponent): When this method returns, contains the component instance if found; otherwise, <see langword="null" />.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the component was found; otherwise, <see langword="false" />.

---
#### public TComponent AddComponent&lt;TComponent&gt;()


**Summary:**
Instantiates and attaches a new component of the specified type to this actor.

**Returns:**

- TComponent: The newly created component instance.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) RemoveComponent&lt;TComponent&gt;()


**Summary:**
Removes the component of the specified type from this actor.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the component was found and removed; otherwise, <see langword="false" />.

---
#### public [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) GetActorByLocalIdInScope([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) localId)


**Summary:**
Resolves an actor handle within the same hierarchy scope matching a scope-local identifier.

**Parameters:**

- `localId` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): The scope-local identifier of the target actor.


**Returns:**

- [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1): The matching actor handle, or <see langword="null" /> if no matching actor exists in scope.

---
#### public [ActorHandle](./actorhandle.md) CreateEmptyActorInScope([String?](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Spawns a new empty actor belonging to the current actor's hierarchy scope.

**Parameters:**

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): The optional debug or display name to assign to the new actor.


**Returns:**

- [ActorHandle](./actorhandle.md): The handle of the newly created actor.

---
#### public [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) CreatePrefabActorInScope([PrefabAsset](./asset/prefabasset.md) prefab, [String?](https://learn.microsoft.com/dotnet/api/system.string) name, [Object?](https://learn.microsoft.com/dotnet/api/system.object) payload)


**Summary:**
Creates an actor from a prefab asset. This will instantiate a new instance of actors from the prefab chain,
and optionally initialise a script if the prefab has one. This will insert it within the scope of the current actor.

**Parameters:**

- `prefab` ([PrefabAsset](./asset/prefabasset.md)): The prefab asset to instantiate.

- `name` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): Optional actor name; if <see langword="null" />, no name is assigned.

- `payload` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): Optional script payload provided to the [ActorScript.OnCreate](./script/actorscript.md#oncreate) callback.


**Returns:**

- [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1): A valid [ActorHandle](./actorhandle.md) if instantiation succeeded; otherwise, <see langword="null" /> if creation was vetoed.

---
#### public TActor AsScript&lt;TActor&gt;()


**Summary:**
Resolves the typed script instance associated with this actor if it exists.

**Returns:**

- TActor: The script instance cast to <typeparamref name="TActor" />, or <see langword="null" /> if not found or the type does not match.

---
#### public [Actor](./actor.md) AsActor()


**Summary:**
Returns the associated script instance as an [Actor](./actor.md), or instantiates a new managed representation if none exists.

**Returns:**

- [Actor](./actor.md): A managed [Actor](./actor.md) wrapper.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is an [ActorHandle](./actorhandle.md) and matches this instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is an [ActorHandle](./actorhandle.md) referencing the same entity and scene; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([ActorHandle](./actorhandle.md) other)


**Summary:**
Determines whether the specified [ActorHandle](./actorhandle.md) references the same native entity and scene.

**Parameters:**

- `other` ([ActorHandle](./actorhandle.md)): The handle to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if both handles reference the same native entity within the same scene; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this actor handle.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a formatted string representation of this actor handle.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string identifying the actor handle and its state.

---


---