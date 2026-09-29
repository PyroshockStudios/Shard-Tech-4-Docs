# Accessing Elements and Using Them

The [RmlElement](../../../../cs-api-ref/sdt4.managed.ui/rml/rmlelement.md) class is the base abstraction for every node in the DOM tree, exposing querying, manipulation, dynamic styling, and event registration.

## Querying Elements

Query descendant nodes using standard DOM selector mechanisms:

```csharp
// Locate element by its ID
RmlElement? saveBtn = doc.GetElementById("save-button");

// Query first match by RCSS selector
RmlElement? activeTab = doc.QuerySelector(".tab-strip > button.active");

// Query all matching elements
RmlElement[] allPanels = doc.QuerySelectorAll("div.panel");

// Fetch collections by class name or tag name
RmlElement[] listItems = doc.GetElementsByClassName("list-item");
RmlElement[] inputs = doc.GetElementsByTagName("input");

// Traverse upwards to the nearest matching ancestor
RmlElement? dialog = saveBtn?.Closest("div.modal-dialog");

```

## Creating and Modifying the DOM

You can spawn new elements using `doc.CreateElement(tag)`:

```csharp
// 1. Create an orphan element
RmlElement newItem = doc.CreateElement("div");

// 2. Configure properties and classes
newItem.Id = "item-101";
newItem.ClassName = "inventory-slot equipped";

// 3. Set text or markup
newItem.InnerText = "Iron Sword";
// Or parse raw RML markup as children:
newItem.InnerRml = "<span class=\"icon\"></span><span class=\"label\">Iron Sword</span>";

// 4. Append to parent
RmlElement? inventoryContainer = doc.GetElementById("inventory");
inventoryContainer?.AppendChild(newItem);

// 5. Remove elements from the DOM
inventoryContainer?.RemoveChild(newItem);
newItem.Dispose(); // Child nodes unparented and not reattached must be disposed manually

```

## Manipulating Classes (`ClassList`)

Use `ClassList` for token-based class modification without string concatenation:

```csharp
// Add one or multiple classes
el.ClassList.Add("selected", "highlighted");

// Remove classes
el.ClassList.Remove("highlighted");

// Toggle class
bool isNowActive = el.ClassList.Toggle("active");

// Forced toggle (adds if true, removes if false)
el.ClassList.Toggle("disabled", true);

// Verify presence
if (el.ClassList.Contains("selected"))
{
    // ...
}

```

## Attributes: Strongly Typed vs. Dynamic

Attributes can be accessed via methods or using C# dynamic properties:

```csharp

// Dynamic property dispatch (PascalCase maps to kebab-case)
el.Attributes.MaxQuantity = 50;           // Sets attribute 'max-quantity="50"'
el.Attributes.TabIndex = 1;               // Sets attribute 'tab-index="1"'
string maxQ = el.Attributes.MaxQuantity;  // Reads attribute 'max-quantity'

// Strongly typed methods
el.SetAttribute("data-item-id", 1024);
if (el.HasAttribute("data-item-id"))
{
    int itemId = el.GetAttribute("data-item-id");
}
el.RemoveAttribute("data-item-id");

```

## Styles: Strongly Typed vs. Dynamic

Inline RCSS styles can be modified via `StyleTyped` or `dynamic Style`:

```csharp
using SDT4.Managed.Core.Graphics;

// Dynamic style dispatch (PascalCase maps to kebab-case)
el.Style.BackgroundColor = ColorRgba.Red; // Sets 'background-color'
el.Style.ZIndex = 10;                     // Sets 'z-index'
el.Style.FontSize = "16dp";               // Sets 'font-size'

// Strongly typed inline styling
el.StyleTyped.SetProperty("margin-left", "20dp");
el.StyleTyped.SetProperty("width", "100%");
el.StyleTyped.Remove("margin-left"); // Reverts to stylesheet default

```

## Event Handling

Register listeners using string event names or strongly typed `RmlEventId` values:

```csharp
using SDT4.Managed.UI.Rml;

// Method listener
void OnButtonClicked(RmlEvent ev)
{
    // The RmlEvent object is ONLY valid during the execution of this callback!

    // Inspect event properties
    RmlElement? target = ev.Target;
    
    // Read event payload parameters
    if (ev.Parameters.TryGetValue("mouse_x", out RmlVariant x))
    {
        int mouseX = x;
    }

    // Example: stop propagation of event
    ev.StopPropagation();
}

// Subscribe to events (useCapture defaults to false)
button.AddEventListener("click", OnButtonClicked);
button.AddEventListener(RmlEventId.Focus, ev => { /* Handle focus */ });

// Unsubscribe
button.RemoveEventListener("click", OnButtonClicked);

// Dispatch a synthetic event
button.DispatchEvent("custom_action", new Dictionary<string, RmlVariant>
{
    { "payload_key", 42 }
});

```