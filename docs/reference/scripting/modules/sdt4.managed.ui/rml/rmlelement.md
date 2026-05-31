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

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Attributes` | [RMLNamedNodeMap](./rmlnamednodemap.md) |  |
| `public get; Style` | [Object](https://learn.microsoft.com/dotnet/api/system.object) | An object representing the declarations of an element’s style attributes. Returns <see cref="T:SDT4.Managed.UI.RML.RCSSStyleDeclaration" /> |
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
#### public [RMLElement?](./rmlelement.md) Closest([String](https://learn.microsoft.com/dotnet/api/system.string) selector)

Retrieve the first ancestor element matching the provided RCSS selector(s).

**Parameters:**

- `selector` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement?](./rmlelement.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DispatchEvent([String](https://learn.microsoft.com/dotnet/api/system.string) event)

Dispatch an event to this node in the DOM. <param name="event"></param>

**Parameters:**

- `event` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddEventListener([String](https://learn.microsoft.com/dotnet/api/system.string) type, [RMLEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)

Register an event handler to a specific event type on the element.

**Parameters:**

- `type` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Event type (same string name as javascript)

- `listener` ([RMLEventListener](./rmleventlistener.md)): Delegate function to be called

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddEventListener([RMLEventID](./rmleventid.md) type, [RMLEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)

Register an event handler to a specific event type on the element.

**Parameters:**

- `type` ([RMLEventID](./rmleventid.md)): Event type

- `listener` ([RMLEventListener](./rmleventlistener.md)): Delegate function to be called

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveEventListener([String](https://learn.microsoft.com/dotnet/api/system.string) type, [RMLEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)

Removes an event handler from a specific event type if it was registered.

**Parameters:**

- `type` ([String](https://learn.microsoft.com/dotnet/api/system.string)): Event type (same string name as javascript)

- `listener` ([RMLEventListener](./rmleventlistener.md)): Exact delegate object that was added as a listener

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveEventListener([RMLEventID](./rmleventid.md) type, [RMLEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)

Removes an event handler from a specific event type if it was registered.

**Parameters:**

- `type` ([RMLEventID](./rmleventid.md)): Event type

- `listener` ([RMLEventListener](./rmleventlistener.md)): Exact delegate object that was added as a listener

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AppendChild([RMLElement](./rmlelement.md) element)

Insert a node as the last child node of this element. The newly parented node must first be detached from its existing parent.

**Parameters:**

- `element` ([RMLElement](./rmlelement.md)): 


---
#### public [RMLElement](./rmlelement.md) RemoveChild([RMLElement](./rmlelement.md) element)

Removes a child node from the current element.

**Parameters:**

- `element` ([RMLElement](./rmlelement.md)): 


**Returns:**

- [RMLElement](./rmlelement.md): Element that has been removed. If this element is not reassigned nor kept alive, it will be destroyed.

---
#### public [RMLElement?](./rmlelement.md) GetElementById([String](https://learn.microsoft.com/dotnet/api/system.string) id)

Returns an element by its id.

**Parameters:**

- `id` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement?](./rmlelement.md): 

---
#### public [RMLElement[]](./rmlelement.md) GetElementsByClassName([String](https://learn.microsoft.com/dotnet/api/system.string) names)

Retrieve a set of all descendant elements with a particular class set.

**Parameters:**

- `names` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement[]](./rmlelement.md): 

---
#### public [RMLElement[]](./rmlelement.md) GetElementsByTagName([String](https://learn.microsoft.com/dotnet/api/system.string) name)

Retrieve a set of all descendant elements with a particular tag name.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement[]](./rmlelement.md): 

---
#### public [RMLElement?](./rmlelement.md) QuerySelector([String](https://learn.microsoft.com/dotnet/api/system.string) selectors)

Retrieve the first descendant element matching the provided RCSS selector(s).

**Parameters:**

- `selectors` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement?](./rmlelement.md): 

---
#### public [RMLElement[]](./rmlelement.md) QuerySelectorAll([String](https://learn.microsoft.com/dotnet/api/system.string) selectors)

Retrieve a set of all descendant elements matching the provided RCSS selector(s).

**Parameters:**

- `selectors` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [RMLElement[]](./rmlelement.md): 

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