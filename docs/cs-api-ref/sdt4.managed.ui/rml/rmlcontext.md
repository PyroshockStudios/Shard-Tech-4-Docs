# RmlContext

## Summary


## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread.
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

!!! important
    This class <strong>MUST</strong> be disposed manually.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RmlContext
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RmlContext**
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
| `public get; Contexts` | [RmlContext[]](./rmlcontext.md) | Returns an array of active contexts |
| `public get; set; Dpi` | [Single](https://learn.microsoft.com/dotnet/api/system.single) | Gets/sets the ratio between the dp/px size |
| `public get; LoadedDocuments` | [RmlDocument[]](./rmldocument.md) | Retrieves all currently loaded documents |
| `public get; DataModels` | [RmlDataModel[]](./data/rmldatamodel.md) | Retrieves all currently instantiated data models |
| `public get; ThemeQuery` | [RmlThemeQuery](./rmlthemequery.md) | The theme query associated with this context |
| `public get; protected set; Name` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |



---

## Methods

#### public static [RmlContext](./rmlcontext.md) CreateContext([String](https://learn.microsoft.com/dotnet/api/system.string) name, [ViewportRenderInstance](../../sdt4.managed.renderer/xrp/viewportrenderinstance.md) viewport)


**Summary:**
Creates a new RmlUi context, with a given name. The name must be unique!

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): A unique name identifying this context.

- `viewport` ([ViewportRenderInstance](../../sdt4.managed.renderer/xrp/viewportrenderinstance.md)): The viewport to attach upon creation.


**Returns:**

- [RmlContext](./rmlcontext.md): A valid RmlContext

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AttachToViewport([ViewportRenderInstance](../../sdt4.managed.renderer/xrp/viewportrenderinstance.md) viewport)


**Summary:**
Attaches this context to a new viewport.
The old viewport is automatically detached.
If the viewport is the same as the current, the operation does nothing.

**Parameters:**

- `viewport` ([ViewportRenderInstance](../../sdt4.managed.renderer/xrp/viewportrenderinstance.md)): A new valid render instance.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) ForceUpdate()


**Summary:**
Immediately attempts to update the context. 

**Remarks:**
!!! important
    It is rare appropriate that this needs to be called. Every frame, contexts get updated automatically.
    This method is mainly here to aid unit testing.

---
#### public T CreateDataModel&lt;T&gt;([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Retrieves the data model instantiated for this context

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): A unique data model name.


**Returns:**

- T: The exact data model instance. Null if the type was not registered as an RML Data Model.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DestroyDataModel([RmlDataModel](./data/rmldatamodel.md) dataModel)


**Summary:**
Destroys the data model
<param name="dataModel">A data model to destroy.</param>

**Parameters:**

- `dataModel` ([RmlDataModel](./data/rmldatamodel.md)): 


---
#### public [RmlDocument?](./rmldocument.md) LoadDocument([AssetId](../../sdt4.managed.core/asset/assetid.md) document)

**Parameters:**

- `document` ([AssetId](../../sdt4.managed.core/asset/assetid.md)): 


**Returns:**

- [RmlDocument?](./rmldocument.md): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) DestroyDocument([RmlDocument](./rmldocument.md) document)


**Summary:**
Removes the document from the UI. The document will be disposed!

**Parameters:**

- `document` ([RmlDocument](./rmldocument.md)): Document instance


---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessKeyDown([Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyIdentifier, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a key down event into this context.

**Parameters:**

- `keyIdentifier` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The key pressed.

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed (i.e., was prevented from propagating by an element); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessKeyUp([Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyIdentifier, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a key up event into this context.

**Parameters:**

- `keyIdentifier` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The key released.

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed (i.e., was prevented from propagating by an element); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessTextInput([Rune](https://learn.microsoft.com/dotnet/api/system.text.rune) unicode)


**Summary:**
Sends a single Unicode character as text input into this context.

**Parameters:**

- `unicode` ([Rune](https://learn.microsoft.com/dotnet/api/system.text.rune)): The Unicode code point to send into this context.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed (i.e., was prevented from propagating by an element); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessTextInput([Char](https://learn.microsoft.com/dotnet/api/system.char) character)


**Summary:**
Sends a single ASCII character as text input into this context.

**Parameters:**

- `character` ([Char](https://learn.microsoft.com/dotnet/api/system.char)): The ASCII character to send into this context.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed; otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessTextInput([String](https://learn.microsoft.com/dotnet/api/system.string) text)


**Summary:**
Sends a string of text as text input into this context.

**Parameters:**

- `text` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The UTF-8 string to send into this context.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed (i.e., was prevented from propagating by an element); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessMouseMove([Int32](https://learn.microsoft.com/dotnet/api/system.int32) x, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) y, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a mouse movement event into this context.

**Parameters:**

- `x` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The x-coordinate of the mouse cursor, in window-coordinates (i.e., 0 should be the left of the client area).

- `y` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The y-coordinate of the mouse cursor, in window-coordinates (i.e., 0 should be the top of the client area).

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the mouse is not interacting with any elements in the context (see <c>IsMouseInteracting</c>); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessMouseButtonDown([Int32](https://learn.microsoft.com/dotnet/api/system.int32) buttonIndex, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a mouse-button down event into this context.

**Parameters:**

- `buttonIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The index of the button that was pressed. Left: 0, Right: 1, Middle: 2.

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the mouse is not interacting with any elements in the context (see <c>IsMouseInteracting</c>); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessMouseButtonUp([Int32](https://learn.microsoft.com/dotnet/api/system.int32) buttonIndex, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a mouse-button up event into this context.

**Parameters:**

- `buttonIndex` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The index of the button that was released. Left: 0, Right: 1, Middle: 2.

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the mouse is not interacting with any elements in the context (see <c>IsMouseInteracting</c>); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessMouseWheel([Vector2d](../../sdt4.managed.core/math/vector2d.md) wheelDelta, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) keyModifierState)


**Summary:**
Sends a <c>mousescroll</c> event into this context, and scrolls the document unless the event was stopped from propagating.

**Parameters:**

- `wheelDelta` ([Vector2d](../../sdt4.managed.core/math/vector2d.md)): The mouse-wheel movement this frame, with positive values being directed right and down.

- `keyModifierState` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): The state of key modifiers (shift, control, caps-lock, etc.) keys; this should be generated by ORing together
members of the <c>Input.KeyModifier</c> enumeration.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the event was not consumed (i.e., was prevented from propagating by an element); otherwise, <see langword="false" />.

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ProcessMouseLeave()


**Summary:**
Tells the context the mouse has left the window.

**Remarks:**
This removes any hover state from all elements and prevents <c>Update()</c> from setting the hover
state for elements under the mouse. The mouse is considered activated again after the next call to [RmlContext.ProcessMouseMove](./rmlcontext.md#processmousemove).

**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> if the mouse is not interacting with any elements in the context (see <c>IsMouseInteracting</c>); otherwise, <see langword="false" />.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SubscribeToWindow([Window](../../sdt4.managed.windowing/window.md) window)


**Summary:**
Subscribes the input processors to the window event listener

**Parameters:**

- `window` ([Window](../../sdt4.managed.windowing/window.md)): A valid window to subscribe to


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) UnsubscribeFromWindow([Window](../../sdt4.managed.windowing/window.md) window)


**Summary:**
Unsubscribes the input processors from the window event listener

**Parameters:**

- `window` ([Window](../../sdt4.managed.windowing/window.md)): A valid window to unsubscribe from


---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object?](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Dispose()

---


---