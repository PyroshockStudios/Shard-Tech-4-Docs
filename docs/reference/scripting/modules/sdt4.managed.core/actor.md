# Actor



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


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; ScopeID` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) |  |
| `public get; ID` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) |  |
| `public get; Mobility` | [Mobility](./components/mobility.md) |  |
| `public get; Parent` | [Actor](./actor.md) |  |
| `public get; Children` | [Actor[]](./actor.md) |  |
| `public get; set; Tag` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; ScopeRoot` | [Actor](./actor.md) | Returns the top most actor in the current scope. |
| `public get; IsValid` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |
| `public get; IsAlive` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |


---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) HasComponent&lt;T&gt;()

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public T GetComponent&lt;T&gt;()

**Returns:**

- T: 

---
#### public T AddComponent&lt;T&gt;()

**Returns:**

- T: 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) KillComponent&lt;T&gt;()

---
#### public [Actor](./actor.md) GetActor([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) uuid)

**Parameters:**

- `uuid` ([UInt64](https://learn.microsoft.com/dotnet/api/system.uint64)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public T AsScript&lt;T&gt;()

**Returns:**

- T: 

---
#### public [Actor](./actor.md) CreateEmptyActor([String](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) stationary)

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `stationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- [Actor](./actor.md): 

---
#### public [Actor](./actor.md) SpawnPrefabActor([String](https://learn.microsoft.com/dotnet/api/system.string) prefabAsset, [Object?](https://learn.microsoft.com/dotnet/api/system.object) state, [String](https://learn.microsoft.com/dotnet/api/system.string) name, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) stationary)

**Parameters:**

- `prefabAsset` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `state` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `stationary` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


**Returns:**

- [Actor](./actor.md): 

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