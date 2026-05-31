# Scene



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

Gets the <see cref="T:SDT4.Managed.Core.Script.SceneScript" /> instance of this <see cref="T:SDT4.Managed.Core.Scene" /> class.

**Returns:**

- T: A valid T if it is a derived instance of a non-null SceneScript. Returns <strong>NULL</strong> otherwise.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Reparent([Actor](./actor.md) newParent, [Actor](./actor.md) child)

**Parameters:**

- `newParent` ([Actor](./actor.md)): 

- `child` ([Actor](./actor.md)): 


---
#### public [Actor](./actor.md) CreateActor([String](https://learn.microsoft.com/dotnet/api/system.string) tag, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) stationary)

**Parameters:**

- `tag` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `stationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor](./actor.md) CreateActorFromPrefab([IPrefabAsset](./asset/iprefabasset.md) prefab, [String](https://learn.microsoft.com/dotnet/api/system.string) tag, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) stationary, [Object?](https://learn.microsoft.com/dotnet/api/system.object) state)

**Parameters:**

- `prefab` ([IPrefabAsset](./asset/iprefabasset.md)): 

- `tag` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `stationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `state` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public static [Actor](./actor.md) GetActorFromId([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) id)

**Parameters:**

- `id` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor[]](./actor.md) GetActorsWithTag([String](https://learn.microsoft.com/dotnet/api/system.string) tag)

**Parameters:**

- `tag` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [Actor[]](./actor.md): 

---
#### public T[] GetActorsOfClass&lt;T&gt;([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) canBeDerived)

**Parameters:**

- `canBeDerived` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- T[]: 

---
#### public [IEnumerable&lt;Actor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateActorsWith&lt;T&gt;(T component)

**Parameters:**

- `component` (T): 


**Returns:**

- [IEnumerable&lt;Actor&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) KillActor([Actor](./actor.md) actor)

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

---


---