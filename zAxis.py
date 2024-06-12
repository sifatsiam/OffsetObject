import bpy

def offset_objects_on_z():
    # Get all objects in the scene
    objects = bpy.context.scene.objects
    
    # Iterate over objects and apply the offset
    for index, obj in enumerate(objects):
        # Calculate the offset
        offset = (index + 1) * 0.1
        # Apply the offset on the Z axis
        obj.location.z += offset

# Run the function
offset_objects_on_z()
