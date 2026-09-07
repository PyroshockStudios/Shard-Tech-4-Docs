# CustomAxisInputEventArgs

## Summary
Provides event data for continuous analogue, rotational, or positional inputs originating from custom input devices.



## Definition

**Namespace:** `SDT4.Managed.Input.Custom.Events`  
**Assembly:** `SDT4.Managed.Input.dll`

```csharp
struct CustomAxisInputEventArgs
```
**Implements:**

##### [IEquatable&lt;CustomAxisInputEventArgs&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
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
| `public get; set; ChannelName` | [String](https://learn.microsoft.com/dotnet/api/system.string) | The name of the axis channel (e.g., <c>"Throttle"</c>, <c>"SteeringAngle"</c>, <c>"Pitch"</c>). |
| `public get; set; DeviceId` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | The hardware instance index, used to differentiate multiple connected devices of the same driver type. |
| `public get; set; Value` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The calibrated or normalised axis value after software deadzones and scaling curves are applied. |
| `public get; set; RawValue` | [Double](https://learn.microsoft.com/dotnet/api/system.double) | The unfiltered, raw hardware readout provided by the device driver. |



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
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([CustomAxisInputEventArgs](./customaxisinputeventargs.md) other)

**Parameters:**

- `other` ([CustomAxisInputEventArgs](./customaxisinputeventargs.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [Object?](https://learn.microsoft.com/dotnet/api/system.object) Sender, out [Guid](https://learn.microsoft.com/dotnet/api/system.guid) SourceId, out [String](https://learn.microsoft.com/dotnet/api/system.string) ChannelName, out [Int32](https://learn.microsoft.com/dotnet/api/system.int32) DeviceId, out [Double](https://learn.microsoft.com/dotnet/api/system.double) Value, out [Double](https://learn.microsoft.com/dotnet/api/system.double) RawValue)

**Parameters:**

- `Sender` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 

- `SourceId` ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)): 

- `ChannelName` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `DeviceId` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `Value` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 

- `RawValue` ([Double](https://learn.microsoft.com/dotnet/api/system.double)): 


---


---