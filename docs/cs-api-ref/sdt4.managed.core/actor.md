# Actor

## Summary
Represents an entity in the scene hierarchy with associated lifecycle, components, and hierarchy management.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](./threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophic failures as the engine is not designed for concurrent scene mutation.

## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class Actor
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **Actor**
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `public readonly Handle` | [ActorHandle](./actorhandle.md) | The underlying handle referencing this actor instance within its owning scene. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; NativeHandle` | [UInt32](https://learn.microsoft.com/dotnet/api/system.uint32) | Gets the underlying native entity identifier. |
| `public get; Scene` | [Scene](./scene.md) | Gets the scene in which this actor resides. |
| `public get; GlobalId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the persistent globally unique identifier of this actor. |
| `public get; ScopeId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the unique identifier of the scope hierarchy that contains this actor. |
| `public get; LocalId` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) | Gets the scope-local identifier of this actor. |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the display or debug name of this actor, or <see langword="null" /> if unnamed. |
| `public get; Mobility` | [Mobility](./mobility.md) | Gets the mobility state of this actor (e.g. static, stationary, or dynamic). |
| `public get; IsValid` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Gets a value indicating whether the actor represents an active, valid entity within the scene. |
| `public get; ScopeRoot` | [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | Gets the root actor handle of the current hierarchy scope, or <see langword="null" /> if this actor has no scope root. |
| `public get; Parent` | [Nullable&lt;ActorHandle&gt;](https://learn.microsoft.com/dotnet/api/system.nullable-1) | Gets the handle of this actor's direct parent in the transform hierarchy, or <see langword="null" /> if it is a root entity. |
| `public get; Children` | [ActorHandle[]](./actorhandle.md) | Gets an array of handles representing all direct children of this actor in the hierarchy. |
| `public get; Components` | [IActorComponent[]](./components/iactorcomponent.md) | Gets an array containing all components currently attached to this actor. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) HasComponent&lt;T&gt;()


**Summary:**
Determines whether this actor has a component of the specified type attached.

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the component is present; otherwise, <see langword="false" />.

---
#### public T GetComponent&lt;T&gt;()


**Summary:**
Retrieves the attached component of the specified type.

**Returns:**

- T: The component instance.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetComponent&lt;T&gt;(out T component)


**Summary:**
Attempts to retrieve an attached component of the specified type.

**Parameters:**

- `component` (T): When this method returns, contains the component instance if found; otherwise, <see langword="null" />.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the component was found; otherwise, <see langword="false" />.

---
#### public T AddComponent&lt;T&gt;()


**Summary:**
Instantiates and attaches a new component of the specified type to this actor.

**Returns:**

- T: The newly created component instance.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) RemoveComponent&lt;T&gt;()


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
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether the specified object is an [Actor](./actor.md) and matches this instance.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the object is an [Actor](./actor.md) referencing the same entity and scene; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Actor](./actor.md) other)


**Summary:**
Determines whether the specified [Actor](./actor.md) references the same native entity and scene.

**Parameters:**

- `other` ([Actor](./actor.md)): The actor to compare with this instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if both instances reference the same native entity within the same scene; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Returns the hash code for this actor.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A 32-bit signed integer hash code.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a formatted string representation of this actor.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string identifying the actor and its handle state.

---


---