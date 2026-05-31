# IResourceManager



## Definition

**Namespace:** `SDT4.Managed.Core`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
interface IResourceManager
```
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


---

## Methods

#### public [Task&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1) LoadAsset&lt;TResource&gt;([AssetID](./asset/assetid.md) assetId)

Returns an asynchronous task to an <see cref="T:SDT4.Managed.Core.Asset.AssetLoadResult`1" /> containing <typeparamref name="TResource" />

**Parameters:**

- `assetId` ([AssetID](./asset/assetid.md)): A valid asset handle pointing to a resource described by <typeparamref name="TResource" />


**Returns:**

- [Task&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1): A valid <see cref="T:System.Threading.Tasks.Task" /> holding the load result.

---
#### public TResource FromControlBlock&lt;TResource&gt;([IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) block)

Converts control block pointer to a proper asset handle.

**Parameters:**

- `block` ([IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr)): Control block pointer.


**Returns:**

- TResource: If <paramref name="block" /> is invalid, <em>or</em> the underlying data does NOT match <typeparamref name="TResource" />,

---


---