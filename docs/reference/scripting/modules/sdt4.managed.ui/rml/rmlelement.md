# RMLElement

RmlUi element based on <a href="https://mikke89.github.io/RmlUiDoc/pages/cpp_manual/elements.html">the RML reference page</a>

## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
class RMLElement
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLElement**
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
| `public get; Attributes` | [RMLNamedNodeMap](./rmlnamednodemap.md) |  |
| `public get; Style` | [RCSSStyleDeclaration](./rcssstyledeclaration.md) | An object representing the declarations of an element’s style attributes |
| `public get; set; ID` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; set; ClassName` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; set; InnerRML` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; set; InnerText` | [String?](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; set; Value` | [RMLVariant](./rmlvariant.md) |  |
| `public get; OwnerDocument` | [RMLDocument](./rmldocument.md) |  |
| `public get; PreviousSibling` | [RMLElement](./rmlelement.md) |  |
| `public get; NextSibling` | [RMLElement](./rmlelement.md) |  |
| `public get; ParentNode` | [RMLElement](./rmlelement.md) |  |
| `public get; ChildNodes` | [RMLElement[]](./rmlelement.md) |  |
| `public get; FirstChild` | [RMLElement](./rmlelement.md) |  |
| `public get; LastChild` | [RMLElement](./rmlelement.md) |  |
| `public get; ClassList` | [RMLClassTokenList](./rmlclasstokenlist.md) |  |
| `public get; ClientHeight` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; ClientLeft` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; ClientTop` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; ClientWidth` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; OffsetHeight` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; OffsetLeft` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; OffsetTop` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; OffsetWidth` | [Single](https://learn.microsoft.com/dotnet/api/system.single) |  |
| `public get; OffsetParent` | [RMLElement](./rmlelement.md) |  |


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Finalize()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Blur()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Focus([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) focusVisible)

**Parameters:**

- `focusVisible` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Click()

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