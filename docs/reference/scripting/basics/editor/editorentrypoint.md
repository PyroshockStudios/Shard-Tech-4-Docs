# What about when I'm running the editor?

You may have noticed that the guide so far has focussed on standalone builds, however
developing with the editor in mind is no less important.

## Setting up the editor entry

Unlike the [Game.OnInit](../entrypoint.md) entry point, the `Game.OnEditorStart` entry provides an already loaded app instance, no arguments and a scene.


```csharp
using SDT4.Managed.Editor;
static class GameEditor 
{
    static void OnEditorStart(EditorRunContext editorRunContext) 
    {
        // ...   
    }
}

```

!!! important
    Note that the `OnEditorStart` is called BEFORE any scripts have been initialised! This means, `OnCreate`, `On[Pre/Post]Begin`, have NOT been called yet. These will be instantiated in a defined order after the editor entry point has been run.

Inside the [EditorRunContext](../../../../cs-api-ref/sdt4.managed.editor/editorruncontext.md) structure, there are many useful fields, such as editor viewports, the running window, the app instance, the scene and the scene script.

```csharp

// Instead of creating a render canvas of the main window,
// we can just use the primary viewport provided by the editor!

editorRunContext.PrimaryViewport.SetCameraActor(/*...*/);

// It is also possible to use multiple viewports that are open in the editor!
// Note that this is not available when launched in a standalone window!
// editorRunContext.Viewports;

```

## The editor exit

Unlike [Game.OnInit](../entrypoint.md), `Game.OnEditorStart` has a corresponding `Game.OnEditorStop` that may be defined when the editor shuts down. This is useful for any manual clean up that may be needed to be performed

```csharp
// ...
static void OnEditorStop(EditorRunContext editorRunContext) 
{
    // Clean up state...

    // Do not dispose the viewports as they are owned by the editor.
    // And the original camera states are restored automatically.
}

```

!!! important
    Note that the `OnEditorStop` is called AFTER all scripts have been destroyed! This means, `OnDestroy`, `On[Pre/Post]End`, have ALREADY been called. 

!!! note
    The standard [Game.OnInit](../entrypoint.md) logic applies when launching a preview build of the game in the editor. This is purely for running instances of a scene inside of the Shard Tech 4 editor. 