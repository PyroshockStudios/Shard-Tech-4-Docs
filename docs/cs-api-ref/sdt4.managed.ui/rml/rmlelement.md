# RmlElement

## Summary
Represents an element in the RmlUi DOM tree, providing DOM-like manipulation, 
layout inspection, styling, and event handling based on the 
<a href="https://mikke89.github.io/RmlUiDoc/pages/cpp_manual/elements.html">RmlUi C++ Element API</a>.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
class RmlElement
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RmlElement**
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
| `public get; Attributes` | [Object](https://learn.microsoft.com/dotnet/api/system.object) | An object representing the declarations of an element’s attribute collection. Returns [NamedNodeMap](./namednodemap.md). Attributes are accessed in C# property naming conventions, e.g. <c>margin-left</c> becomes <c>MarginLeft</c>. Return types of the accessed attributes are non-null [String](https://learn.microsoft.com/dotnet/api/system.string). |
| `public get; AttributesTyped` | [NamedNodeMap](./namednodemap.md) | Gets the strongly typed attribute collection for this element. |
| `public get; Style` | [Object](https://learn.microsoft.com/dotnet/api/system.object) | An object representing the declarations of an element’s style attributes. Returns [RcssStyleDeclaration](./rcssstyledeclaration.md). Styles are accessed in C# property naming conventions, e.g. <c>background-color</c> becomes <c>BackgroundColor</c>. Return types of the accessed properties are [RmlVariant](./rmlvariant.md). |
| `public get; StyleTyped` | [RcssStyleDeclaration](./rcssstyledeclaration.md) | Gets an object representing the inline RCSS style declarations of this element. |
| `public get; set; Id` | [String?](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the unique identifier (<c>id</c>) attribute of the element. |
| `public get; set; ClassName` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the <c>class</c> attribute of the element, representing a space-separated list of CSS/RCSS class names. |
| `public get; set; InnerRml` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the serialized RML markup contained within the element. Setting this parses the markup and replaces all child nodes. |
| `public get; set; InnerText` | [String?](https://learn.microsoft.com/dotnet/api/system.string) | Gets or sets the raw text content of the element if this element is or wraps a text node. Returns <see langword="null" /> if this element cannot be cast to a text element. |
| `public get; set; Value` | [RmlVariant](./rmlvariant.md) | Gets or sets the value of the element. For form controls (inputs, selects, etc.),  this interacts with the underlying form control value; otherwise, it accesses the <c>value</c> attribute. |
| `public get; set; OwnerDocument` | [RmlDocument](./rmldocument.md) | Gets the top-level [RmlDocument](./rmldocument.md) that contains this element. |
| `public get; PreviousSibling` | [RmlElement](./rmlelement.md) | Gets the node immediately preceding this element in its parent's child list,  or <see langword="null" /> if this element is the first child. |
| `public get; NextSibling` | [RmlElement](./rmlelement.md) | Gets the node immediately following this element in its parent's child list,  or <see langword="null" /> if this element is the last child. |
| `public get; ParentNode` | [RmlElement](./rmlelement.md) | Gets the parent [RmlElement](./rmlelement.md) of this element in the DOM tree,  or <see langword="null" /> if this element has no parent. |
| `public get; ChildNodes` | [RmlElement[]](./rmlelement.md) | Gets an array containing all child elements of this element. |
| `public get; FirstChild` | [RmlElement](./rmlelement.md) | Gets the first direct child element of this node, or <see langword="null" /> if it has no children. |
| `public get; LastChild` | [RmlElement](./rmlelement.md) | Gets the last direct child element of this node, or <see langword="null" /> if it has no children. |
| `public get; ClassList` | [DomTokenList](./domtokenlist.md) | Gets a live [DomTokenList](./domtokenlist.md) representing the element's class attribute,  allowing manipulation of individual classes (add, remove, toggle, contains). |
| `public get; ClientHeight` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the inner height of the element in pixels, including padding but excluding borders, margins, and horizontal scrollbars. |
| `public get; ClientLeft` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the width of the left border of the element in pixels. |
| `public get; ClientTop` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the width of the top border of the element in pixels. |
| `public get; ClientWidth` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the inner width of the element in pixels, including padding but excluding borders, margins, and vertical scrollbars. |
| `public get; OffsetHeight` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the height of the element in pixels, including vertical padding, borders, and scrollbars. |
| `public get; OffsetLeft` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the distance in pixels from the outer left edge of this element to the inner left edge of its [RmlElement.OffsetParent](./rmlelement.md#offsetparent). |
| `public get; OffsetTop` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the distance in pixels from the outer top edge of this element to the inner top edge of its [RmlElement.OffsetParent](./rmlelement.md#offsetparent). |
| `public get; OffsetWidth` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets the width of the element in pixels, including horizontal padding, borders, and scrollbars. |
| `public get; OffsetParent` | [RmlElement](./rmlelement.md) | Gets the nearest ancestor element that has a position other than static,  or <see langword="null" /> if no positioned ancestor exists. |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) HasAttribute([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Checks whether the element has an attribute with the given name.
Corresponds to JavaScript <c>element.hasAttribute(name)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the attribute to look for.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the attribute exists; otherwise, <see langword="false" />.

---
#### public [RmlVariant](./rmlvariant.md) GetAttribute([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Retrieves the value of an attribute by its exact case-insensitive name.
Corresponds to JavaScript <c>element.getAttribute(name)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The attribute name (e.g., <c>"data-id"</c>, <c>"href"</c>).


**Returns:**

- [RmlVariant](./rmlvariant.md): An [RmlVariant](./rmlvariant.md) holding the attribute value. If the attribute does not exist,
returns a variant with type [RmlVariantType.None](./rmlvarianttype.md#none).

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetAttribute([String](https://learn.microsoft.com/dotnet/api/system.string) name, [RmlVariant](./rmlvariant.md) value)


**Summary:**
Sets the value of an attribute on the specified element.
Corresponds to JavaScript <c>element.setAttribute(name, value)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The attribute name.

- `value` ([RmlVariant](./rmlvariant.md)): The attribute value as an [RmlVariant](./rmlvariant.md).


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveAttribute([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Removes the attribute with the specified name from the element.
Corresponds to JavaScript <c>element.removeAttribute(name)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the attribute to remove.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Blur()


**Summary:**
Removes input focus from this element.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Focus([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) focusVisible)


**Summary:**
Sets input focus to this element.

**Parameters:**

- `focusVisible` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): If <see langword="true" />, forces visible focus indicators (such as focus outlines) to appear.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): True if the change focus request was successful

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Click()


**Summary:**
Simulates a mouse click on this element, triggering click events and default actions.

---
#### public [RmlElement?](./rmlelement.md) Closest([String](https://learn.microsoft.com/dotnet/api/system.string) selector)


**Summary:**
Traverses this element and its ancestors up toward the document root, returning the first 
element that matches the specified RCSS selector.

**Parameters:**

- `selector` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The RCSS selector query string.


**Returns:**

- [RmlElement?](./rmlelement.md): The closest matching ancestor [RmlElement](./rmlelement.md), or <see langword="null" /> if none matched.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DispatchEvent([String](https://learn.microsoft.com/dotnet/api/system.string) type, [IReadOnlyDictionary&lt;String?, RmlVariant?&gt;?](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2) parameters)


**Summary:**
Dispatches a synthetic event to this node in the DOM tree.

**Parameters:**

- `type` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the event type to dispatch.

- `parameters` ([IReadOnlyDictionary&lt;String?, RmlVariant?&gt;?](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)): A dictionary of event parameters to pass, or null if no parameters


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DispatchEvent([RmlEventId](./rmleventid.md) type, [IReadOnlyDictionary&lt;String?, RmlVariant?&gt;?](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2) parameters)


**Summary:**
Dispatches a synthetic event to this node in the DOM tree.

**Parameters:**

- `type` ([RmlEventId](./rmleventid.md)): The strongly typed event ID to dispatch.

- `parameters` ([IReadOnlyDictionary&lt;String?, RmlVariant?&gt;?](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)): A dictionary of event parameters to pass, or null if no parameters


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddEventListener([String](https://learn.microsoft.com/dotnet/api/system.string) type, [RmlEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)


**Summary:**
Registers an event handler for a specific event type on this element by name.

**Parameters:**

- `type` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the event type (e.g., <c>"click"</c>, <c>"keydown"</c>).

- `listener` ([RmlEventListener](./rmleventlistener.md)): The delegate function to invoke when the event is triggered.

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): If <see langword="true" />, the listener is added to the capture phase; 
otherwise, it is added to the bubble/target phase.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddEventListener([RmlEventId](./rmleventid.md) type, [RmlEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)


**Summary:**
Registers an event handler for a specific event type on this element using an [RmlEventId](./rmleventid.md).

**Parameters:**

- `type` ([RmlEventId](./rmleventid.md)): The strongly typed event ID.

- `listener` ([RmlEventListener](./rmleventlistener.md)): The delegate function to invoke when the event is triggered.

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): If <see langword="true" />, the listener is added to the capture phase; 
otherwise, it is added to the bubble/target phase.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveEventListener([String](https://learn.microsoft.com/dotnet/api/system.string) type, [RmlEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)


**Summary:**
Removes a previously registered event listener by event type name.

**Parameters:**

- `type` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The name of the event type.

- `listener` ([RmlEventListener](./rmleventlistener.md)): The exact delegate instance that was registered.

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Specifies whether the listener being removed was registered as a capturing listener.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemoveEventListener([RmlEventId](./rmleventid.md) type, [RmlEventListener](./rmleventlistener.md) listener, [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) useCapture)


**Summary:**
Removes a previously registered event listener by its strongly typed event ID.

**Parameters:**

- `type` ([RmlEventId](./rmleventid.md)): The strongly typed event ID.

- `listener` ([RmlEventListener](./rmleventlistener.md)): The exact delegate instance that was registered.

- `useCapture` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): Specifies whether the listener being removed was registered as a capturing listener.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AppendChild([RmlElement](./rmlelement.md) element)


**Summary:**
Inserts a node as the last child node of this element.
The newly parented node must first be detached from its existing parent before being appended.

**Parameters:**

- `element` ([RmlElement](./rmlelement.md)): The element to append as a child.


---
#### public [RmlElement](./rmlelement.md) RemoveChild([RmlElement](./rmlelement.md) element)


**Summary:**
Removes a child node from the current element.

**Parameters:**

- `element` ([RmlElement](./rmlelement.md)): The child node to be removed.


**Returns:**

- [RmlElement](./rmlelement.md): The removed [RmlElement](./rmlelement.md). Note: This instance now owns the native handle and will destroy it when disposed.

---
#### public [RmlElement?](./rmlelement.md) GetElementById([String](https://learn.microsoft.com/dotnet/api/system.string) id)


**Summary:**
Returns the descendant element with the specified <c>id</c> attribute.

**Parameters:**

- `id` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The case-sensitive ID of the element to locate.


**Returns:**

- [RmlElement?](./rmlelement.md): The matching [RmlElement](./rmlelement.md), or <see langword="null" /> if not found.

---
#### public [RmlElement[]](./rmlelement.md) GetElementsByClassName([String](https://learn.microsoft.com/dotnet/api/system.string) names)


**Summary:**
Retrieves an array of all descendant elements with the specified class name(s).

**Parameters:**

- `names` ([String](https://learn.microsoft.com/dotnet/api/system.string)): One or more space-separated class names.


**Returns:**

- [RmlElement[]](./rmlelement.md): An array of matching [RmlElement](./rmlelement.md) instances.

---
#### public [RmlElement[]](./rmlelement.md) GetElementsByTagName([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Retrieves an array of all descendant elements with the specified tag/element name.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The tag name to search for (e.g., <c>"div"</c>, <c>"button"</c>).


**Returns:**

- [RmlElement[]](./rmlelement.md): An array of matching [RmlElement](./rmlelement.md) instances.

---
#### public [RmlElement?](./rmlelement.md) QuerySelector([String](https://learn.microsoft.com/dotnet/api/system.string) selectors)


**Summary:**
Returns the first descendant element matching the specified RCSS selector string.

**Parameters:**

- `selectors` ([String](https://learn.microsoft.com/dotnet/api/system.string)): A valid RCSS selector query string.


**Returns:**

- [RmlElement?](./rmlelement.md): The first matching [RmlElement](./rmlelement.md), or <see langword="null" /> if no match is found.

---
#### public [RmlElement[]](./rmlelement.md) QuerySelectorAll([String](https://learn.microsoft.com/dotnet/api/system.string) selectors)


**Summary:**
Returns an array of all descendant elements matching the specified RCSS selector string.

**Parameters:**

- `selectors` ([String](https://learn.microsoft.com/dotnet/api/system.string)): A valid RCSS selector query string.


**Returns:**

- [RmlElement[]](./rmlelement.md): An array containing all matched [RmlElement](./rmlelement.md) instances.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)


**Summary:**
Determines whether this instance and another specified object have the same underlying native handle.

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The object to compare with the current instance.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if `obj` is an [RmlElement](./rmlelement.md) with an identical native handle; otherwise, <see langword="false" />.

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()


**Summary:**
Serves as the default hash function, hashing the underlying native handle.

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): A hash code for the current element.

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns a string representation of the element, including its ID, class name, and styles.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): A formatted string with element metadata.

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) disposing)


**Summary:**
Releases unmanaged resources and optionally managed resources.

**Parameters:**

- `disposing` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): <see langword="true" /> if called from [RmlElement.Dispose](./rmlelement.md#dispose); 
<see langword="false" /> if called from the finaliser.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) Finalize()


**Summary:**
Finalizer for [RmlElement](./rmlelement.md) that ensures unmanaged handles are cleaned up if owned.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()


**Summary:**
Releases all resources used by the current instance of [RmlElement](./rmlelement.md).

**Remarks:**
!!! danger
    Do NOT call this on an [RmlDocument](./rmldocument.md) that is loaded by a context.
    The result is undefined behaviour

---


---