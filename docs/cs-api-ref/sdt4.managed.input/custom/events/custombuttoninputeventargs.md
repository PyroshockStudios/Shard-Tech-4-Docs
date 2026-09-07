# CustomButtonInputEventArgs

## Summary
Provides event data for digital button or binary state changes originating from custom input devices.



## Definition

**Namespace:** `SDT4.Managed.Input.Custom.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct CustomButtonInputEventArgs
```
**Implements:**

##### [IEquatable&lt;CustomButtonInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Sender` | [Object?](https://learn.microsoft.com/dotnet/api/system.object) | The source driver or object that dispatched the event, or <see langword="null" />. |
| `public get; set; SourceId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | A unique [Guid](https://learn.microsoft.com/dotnet/api/system.guid) identifying the source peripheral driver or hardware interface. |
| `public get; set; ChannelName` | [String](https://learn.microsoft.com/dotnet/api/system.string) | The name of the button channel or input line (e.g., <c>"Trigger"</c>, <c>"ShifterUp"</c>). |
| `public get; set; DeviceId` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The hardware instance index, used to differentiate multiple connected devices of the same driver type. |
| `public get; set; IsDown` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | <see langword="true" /> if the button is currently held down; <see langword="false" /> if it was released. |
| `public get; set; IsRepeating` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) | Indicates whether this event was triggered by software- or hardware-assisted repeat pulses. |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([CustomButtonInputEventArgs](./custombuttoninputeventargs.md) other)

**Parameters:**

- `other` ([CustomButtonInputEventArgs](./custombuttoninputeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Guid](https://learn.microsoft.com/dotnet/api/system.guid) SourceId, out [String](https://learn.microsoft.com/dotnet/api/system.string) ChannelName, out [Int32](https://learn.microsoft.com/dotnet/api/system.int32) DeviceId, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsDown, out [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) IsRepeating)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `SourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 

- `ChannelName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `DeviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `IsDown` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 

- `IsRepeating` ([Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)): 


---


---