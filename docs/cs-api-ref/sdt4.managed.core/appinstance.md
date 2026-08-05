# AppInstance

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class AppInstance
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **AppInstance**
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
| `public get; Build` | [InstanceBuild](./instancebuild.md) |  |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; GameVersion` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; EngineVersion` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Platform` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; ResourceManager` | [ResourceManager](./resourcemanager.md) |  |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetCapability&lt;TCapability&gt;(out TCapability capability)

**Parameters:**

- `capability` (TCapability): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateCapabilities()

**Returns:**

- [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---