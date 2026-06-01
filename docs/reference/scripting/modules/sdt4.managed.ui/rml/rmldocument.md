# RMLDocument

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
class RMLDocument
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [RMLElement](./rmlelement.md) ➔  **RMLDocument**
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
| `public get; set; Title` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; SourceURL` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |

---


## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) ReloadRCSS()

---
#### public [RMLDocument](./rmldocument.md) ReloadRML()

**Returns:**

- [RMLDocument](./rmldocument.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Display()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Hide()

---
#### public [RMLElement](./rmlelement.md) CreateElement([String](https://learn.microsoft.com/dotnet/api/system.string) name)

##### Summary
Creates a new orphan element. This element has no parent and must be assigned immediately
otherwise, it will be destroyed

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement](./rmlelement.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) PullToFront()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) PushToBack()

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---