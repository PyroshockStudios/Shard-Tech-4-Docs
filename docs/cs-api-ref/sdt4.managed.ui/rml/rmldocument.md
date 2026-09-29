# RmlDocument

## Summary
Represents the root RmlUi document window hosting a hierarchy of UI elements, styling rules, and layout contexts.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophic failures as the engine is not designed for concurrent UI mutation.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RmlDocument
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [RmlElement](./rmlelement.md) ➔  **RmlDocument**
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
| `public get; set; Title` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the document's window title. |
| `public get; SourceUrl` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the source asset path or URL from which this document was loaded. |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) ReloadRcss()


**Summary:**
Forces a reload of the external and inline RCSS stylesheets associated with this document, reapplying styles across the DOM.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Show()


**Summary:**
Makes the document visible and enables rendering to the UI viewport canvas.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Hide()


**Summary:**
Hides the document from the UI viewport canvas, suspending its layout rendering.

---
#### public [RmlElement](./rmlelement.md) CreateElement([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Creates a new unparented (orphaned) element within the document context.

**Remarks:**
The created element has no parent upon construction and must be attached to the DOM hierarchy (e.g. via <c>AppendChild</c>);
otherwise, it may be collected or destroyed.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The RML tag name for the new element (e.g. <c>"div"</c>, <c>"span"</c>, <c>"button"</c>).


**Returns:**

- [RmlElement](./rmlelement.md): The newly created orphaned [RmlElement](./rmlelement.md).

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) PullToFront()


**Summary:**
Moves this document to the top of the z-order stack within its UI context, displaying it in front of sibling documents.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) PushToBack()


**Summary:**
Moves this document to the bottom of the z-order stack within its UI context, displaying it behind sibling documents.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a formatted string representation of this document.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A string identifying the document and its active title or disposed state.

---


---