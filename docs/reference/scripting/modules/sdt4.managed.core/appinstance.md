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
| `public get; Environment` | [InstanceEnvironment](./instanceenvironment.md) |  |
| `public get; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Version` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; Platform` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; ResourceManager` | [IResourceManager](./iresourcemanager.md) |  |

---


## Methods

#### public TCapability TryGetCapability&lt;TCapability&gt;()

**Returns:**

- TCapability: 

---
#### public [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) EnumerateCapabilities()

**Returns:**

- [IEnumerable&lt;ICapability&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1): 

---
#### public [Task&lt;AppExitRequest&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) RequestAppExitAsync()

**Returns:**

- [Task&lt;AppExitRequest&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Terminate()

---


---