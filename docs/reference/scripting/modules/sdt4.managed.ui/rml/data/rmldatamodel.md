# RMLDataModel

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.RML.Data`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
abstract class RMLDataModel
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLDataModel**
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
| `public get; Canvas` | [RMLCanvas](../rmlcanvas.md) |  |

---


## Methods

#### protected abstract [Void](https://learn.microsoft.com/dotnet/api/system.void) InitEvent()

##### Summary
Called when RmlUi constructs the data model

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) FlagDirty([String?](https://learn.microsoft.com/dotnet/api/system.string) variable)

##### Summary
Marks the data model as dirty to rebuild (part of) the DOM.
If the <paramref name="variable" /> is null, then the entire model is assumed dirty

**Parameters:**

- `variable` ([String?](https://learn.microsoft.com/dotnet/api/system.string)): <em>Valid</em> name of the variable to specify, or null


---


---