# RmlDataModels

Shard Tech 4 integrates RmlUi's two-way data-binding engine via [RmlDataModel](../../../../cs-api-ref/sdt4.managed.ui/rml/data/rmldatamodel.md). Data models allow C# fields and methods to be bound directly to RML templates, synchronizing DOM content and handling UI events without manual element traversal.

## Defining a Data Model

Subclass [RmlDataModel](../../../../cs-api-ref/sdt4.managed.ui/rml/data/rmldatamodel.md) and pass through the required `RmlDataModelToken`.

Fields exposed to the UI must be marked with `[RmlDataVariable]`. Callback methods exposed to UI events must be marked with `[RmlDataEvent]`.

```csharp
using System.Collections.Generic;
using SDT4.Managed.Core.Graphics;
using SDT4.Managed.Core.Math;
using SDT4.Managed.UI.Rml;
using SDT4.Managed.UI.Rml.Attributes;
using SDT4.Managed.UI.Rml.Data;

namespace MyGame.UI;

// 1. Nested structs must implement IRmlDataStruct
public sealed class InventorySlot : IRmlDataStruct
{
    [RmlDataVariable] public int Id;
    [RmlDataVariable] public string Name = string.Empty;
    [RmlDataVariable] public int Quantity;

    // Called whenever RmlUi writes directly to a member
    public void MemberSetEvent(string memberName)
    {
    }
}

// 2. Custom collection implementing IRmlDataArray<T>
public sealed class SimpleDataArray<T> : IRmlDataArray<T> where T : IRmlData
{
    private readonly List<T> _items = [];

    public void Add(T item) => _items.Add(item);
    public int Size() => _items.Count;
    public T Get(int index) => _items[index];
    public void Set(int index, T value) => _items[index] = value;

    // If you wish to use it as an enumerator, you may specify the implementation manually
    // However, IRmlDataArray<> already implements it by default.

    // public IEnumerator<T> GetEnumerator() => _items.GetEnumerator();
    // IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}

// 3. The primary Data Model class
public sealed class PlayerHudModel : RmlDataModel
{
    [RmlDataVariable] public string PlayerName = "Warrior";
    [RmlDataVariable] public int Health = 100;
    [RmlDataVariable] public int MaxHealth = 100;
    [RmlDataVariable] public bool IsDead = false;
    [RmlDataVariable] public ColorRgba HealthBarColor = ColorRgba.Green;

    [RmlDataVariable] public readonly SimpleDataArray<InventorySlot> Slots = new();

    public PlayerHudModel(RmlDataModelToken token) : base(token)
    {
    }

    // Parameterless event callback
    [RmlDataEvent]
    public void OnDrinkPotion()
    {
        Health = Scalar.Min(Health + 25, MaxHealth);
        FlagDirty("Health");
    }

    // Event callback receiving arguments from RML markup
    [RmlDataEvent]
    public void OnDropSlot(int slotIndex, string reason)
    {
        // ...
        FlagDirty("Slots");
    }
}

```

### Allowed Member Types

* **`[RmlDataVariable]` Fields:**
* Primitives: `bool`, `byte`, `char`, `int`, `uint`, `long`, `ulong`, `string`
* Math & Core: `Vector2f`, `Vector3f`, `Vector4f`, `ColorRgba`, `RmlVariant`
* Custom Structs: classes/structs implementing `IRmlDataStruct`
* Scalars: classes implementing `IRmlDataScalar` (`Get()` / `Set()`)
* Collections: classes implementing `IRmlDataArray<T>` or `IRmlDataArray` (untyped variant arrays)


* **`[RmlDataEvent]` Parameters:**
* Only primitives (`bool`, `int`, `uint`, `long`, `ulong`, `byte`, `char`, `string`), math/graphics types (`Vector2f`, `Vector3f`, `Vector4f`, `ColorRgba`), and `RmlVariant`.



## Instantiation and Lifecycle

Data models are created through the [RmlContext](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlcontext.md) using a unique model name:

```csharp
// 1. Create the data model before loading or binding documents
PlayerHudModel? model = uiContext.CreateDataModel<PlayerHudModel>("player_hud");

// 2. Load the document bound to this model
RmlDocument? hudDoc = uiContext.LoadDocument(new AssetId("Master/UI/PlayerHud.rml"));
hudDoc?.Show();

// 3. When finished or changing scenes
uiContext.DestroyDataModel(model);

```

## Markup Binding Directives

Declare `data-model="model_name"` on the root document or container element to activate bindings:

```html
<rml>
<head>
  <link type="text/rcss" href="Engine/UI/Styles/UI_Core.rcss"></link>
</head>
<body data-model="player_hud">

  <!-- 1. Text interpolation -->
  <h1>{{PlayerName}}</h1>
  <p>HP: {{Health}} / {{MaxHealth}}</p>

  <!-- 2. Two-way form binding (inputs, selects) -->
  <input type="text" data-value="PlayerName" />

  <!-- 3. Conditionals -->
  <div data-if="IsDead" class="death-banner">
    YOU DIED
  </div>

  <!-- 4. Dynamic styling -->
  <div class="health-bar" data-style-background-color="HealthBarColor"></div>

  <!-- 5. Collection loops (data-for) -->
  <ul class="inventory-list">
    <li data-for="slot : Slots" class="item">
      <span>{{slot.Name}} (x{{slot.Quantity}})</span>
      <button data-event-click="OnDropSlot(it_index, 'user_action')">Drop</button>
    </li>
  </ul>

  <!-- 6. Button click events -->
  <button data-event-click="OnDrinkPotion()">Heal</button>

</body>
</rml>

```

## Notifying Changes (`FlagDirty`)

RmlUi does not poll fields every frame. When you modify data model fields from gameplay scripts, you must notify the data engine to update the DOM:

```csharp
// Flag an individual variable as dirty
playerModel.Health -= 15;
playerModel.FlagDirty("Health");

// Flag the entire model to sync all variables
playerModel.FlagDirty(null);

```