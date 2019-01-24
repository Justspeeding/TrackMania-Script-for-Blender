bl_info = {
    "name": "TM_Modding",
    "author": "JustSpeeding",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Tool Shelf > TM",
    "description": "Script for Carpark ManiaPark",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }

import bpy

# apply rotation and scale  'Xform 3dsmax'
class ApplyRotSca(bpy.types.Operator):
    """Apply Rotation & Scale\nApplies the current rotation and scale"""
    bl_idname = "myops.add_applyrotsca"
    bl_label = "Reset Xform"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        self.report({'INFO'}, "reset Done")
        return {'FINISHED'}


		# Selection To Cursor 
class SelCurs(bpy.types.Operator):
    """set selection to cursor"""
    bl_idname = "myops.add_selcurs"
    bl_label = "SelectionToCursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        return {'FINISHED'}
		
			# set Cursor 0.0.0
class Cursor(bpy.types.Operator):
    """set cursor to 0.0.0"""
    bl_idname = "myops.add_curs"
    bl_label = "set cursor to 0.0.0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        return {'FINISHED'}

		# Cursor To Selection
class CursorTOSelection(bpy.types.Operator):
    """set cursor to selection"""
    bl_idname = "myops.add_cursortoselection"
    bl_label = "CursorToSelection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {'FINISHED'}

		# Origin TO Cursor
class OriginToCursor(bpy.types.Operator):
    """set origin to cursor """
    bl_idname = "myops.add_origintocursor"
    bl_label = "OriginToCursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return {'FINISHED'}

		# Edit objectmode
class EditMode(bpy.types.Operator):
    """switch edit object mode"""
    bl_idname = "myops.add_edit"
    bl_label = "Edit/object Mode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


 		# Edit objectmode
 
 #fakeshad
class FakeShad(bpy.types.Operator):
    """Make FakeShad"""
    bl_idname = "myops.add_fakeshad"
    bl_label = "FakeShad"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'FakeShad'
        me.name = 'FakeShad'
        bpy.ops.transform.resize(value=(2, 3, 1))
        bpy.ops.transform.translate(value=(0, 0,-0.03))
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        
        return {'FINISHED'}
    
#Projshad
class ProjShad(bpy.types.Operator):
    """Make ProjShad"""
    bl_idname = "myops.add_projshad"
    bl_label = "ProjShad"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'ProjShad'
        me.name = 'ProjShad'
        bpy.ops.transform.resize(value=(2, 3, 1))
        bpy.ops.transform.translate(value=(0, 0,-0.03))
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        
        return {'FINISHED'}
#maxbox
class MaxBox(bpy.types.Operator):
    """Make MaxBox"""
    bl_idname = "myops.add_maxbox"
    bl_label = "MaxBox"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_cube_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'MaxBox'
        me.name = 'MaxBox'
        bpy.ops.transform.resize(value=(1.5, 3, 1.35))
        bpy.ops.transform.translate(value=(0, 0, 1.15))
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return {'FINISHED'}
#lightFProjProj
class LightFProj(bpy.types.Operator):
    """Make LightFProj"""
    bl_idname = "myops.add_lightfproj"
    bl_label = "LightFProj"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFProj'
        me.name = 'LightFProj'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0, -2.20, 0.58))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return {'FINISHED'}
		
		#Ligts
		
class Light(bpy.types.Operator):
    """Make Lights"""
    bl_idname = "myops.add_light"
    bl_label = "Lights"
    bl_options = {'REGISTER', 'UNDO'}
#RR
    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightRR'
        me.name = 'LightRR'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.7,2.14,0.8))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
  #RL
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightRL'
        me.name = 'LightRL'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.7,2.14,0.8))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

  #FR1
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFR1'
        me.name = 'LightFR1'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.78,-1.95,0.58))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

  #FR2
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFR2'
        me.name = 'LightFR2'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.675,-1.95,0.516))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

  #FR3
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFR3'
        me.name = 'LightFR3'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.57,-1.95,0.452))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)      

 #FL1
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFL1'
        me.name = 'LightFL1'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.78,-1.95,0.58))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

  #FL2
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFL2'
        me.name = 'LightFL2'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.675,-1.95,0.516))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

  #FL3
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'LightFL3'
        me.name = 'LightFL3'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.57,-1.95,0.452))
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
              
        return {'FINISHED'}
    
    
 #WheelMin
 
 
class WheelMin(bpy.types.Operator):
    """Make WheelMin"""
    bl_idname = "myops.add_wheelmin"
    bl_label = "WheelMin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'WheelMin'
        me.name = 'WheelMin'
        bpy.ops.transform.resize(value=(0.25, 0.25, 0.25)) 
        bpy.ops.transform.translate(value=(0, 0,0.5))
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        
        return {'FINISHED'}
    
    
    # Flames
    
class Flames(bpy.types.Operator):
    """Make Exhausts"""
    bl_idname = "myops.add_flames"
    bl_label = "Exhausts"
    bl_options = {'REGISTER', 'UNDO'}
    
#FLAME1
    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust1'
        me.name = 'Exhaust1'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.7,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        
#FLAME2
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust2'
        me.name = 'Exhaust2'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.54,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

#FLAME3
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust3'
        me.name = 'Exhaust3'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.38,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

#FLAME4
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust4'
        me.name = 'Exhaust4'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(-0.2,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

#FLAME5
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust5'
        me.name = 'Exhaust5'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.2,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

#FLAME6
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust6'
        me.name = 'Exhaust6'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.38,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)     

#FLAME7
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust7'
        me.name = 'Exhaust7'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.54,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)      

#FLAME8
        bpy.ops.mesh.primitive_plane_add()
        ob = bpy.context.object
        me = ob.data
        ob.name = 'Exhaust8'
        me.name = 'Exhaust8'
        bpy.ops.transform.resize(value=(0.05, 0.05,0))
        bpy.ops.transform.translate(value=(0.7,2.14,0.2))
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.00)
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
             
        return {'FINISHED'} 

#Make The Panal And Buttons


# Panel 1
class TM_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "object data"
    bl_idname = "TM_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TM"
	
    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Edit the object", icon='OBJECT_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")
       
    
      
        
#Panel 2
class TM_Panel2(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Suspention Helpers"
    bl_idname = "TM_Panel2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TM"
	
    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        obj = context.active_object
        obj = context.object
        row = layout.row()
        col = layout.column(align=True)
        col = layout.column(align=True)
        col.operator_menu_enum("object.origin_set", "type", text="Set Origin")
        row.operator("myops.add_selcurs", icon='CURSOR')
        row = layout.row()
        row.operator("myops.add_cursortoselection", icon='CURSOR')
        row = layout.row()
        row.operator("myops.add_curs", icon='CURSOR')
        row = layout.row()
        row.operator("myops.add_origintocursor", icon='MANIPUL')
        row = layout.row()		       
        row.operator("myops.add_applyrotsca", icon='NDOF_DOM')
        row = layout.row()
        row.operator("myops.add_edit", icon='OBJECT_DATA')

     #Panel 3
     
class TM_Panel3(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Add TM Objects"
    bl_idname = "TM_Panel3"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TM"
	
    def draw(self, context):
        layout = self.layout

        obj = context.object
       
        row = layout.row()
        row.operator("myops.add_fakeshad" , icon='MESH_PLANE')
        
       
        row = layout.row()
        row.operator("myops.add_maxbox" , icon='MESH_CUBE')       
		
        row = layout.row()
        row.operator("myops.add_lightfproj" , icon='LAMP_SPOT')   	
                
        row = layout.row()
        row.operator("myops.add_wheelmin" , icon='AUTO')     

        row = layout.row()
        row.operator("myops.add_flames" , icon='PMARKER_ACT')  

     #Panel 3b
     
class TM_Panel3b(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Add TMUF Objects"
    bl_idname = "TM_Panel3b"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TM"
	
    def draw(self, context):
        layout = self.layout

        obj = context.object
       
        row = layout.row()
        row.operator("myops.add_projshad" , icon='MESH_PLANE')
        row = layout.row()
        row.operator("myops.add_lightfproj" , icon='LAMP_SPOT')  
        row = layout.row() 	
        row.operator("myops.add_light" , icon='LAMP_POINT') 
        
 
     #Panel 4
     		
class TM_Panel4(bpy.types.Panel):
    """Creates the Modifier Panel"""
    bl_label = "Add Modifier"
    bl_idname = "TM_Panel4"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TM"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("object.modifier_add", text="CURVE", icon="MOD_CURVE").type='CURVE' 
        row = layout.row()
        row.operator("object.modifier_add", text="ARRAY", icon="MOD_ARRAY").type='ARRAY'
        row = layout.row()
        row.operator("object.modifier_add", text="DECIMATE", icon="MOD_DECIM").type='DECIMATE'  		


		
# define operators

def register():
    bpy.utils.register_class(TM_Panel)
    bpy.utils.register_class(TM_Panel2)
    bpy.utils.register_class(TM_Panel3)
    bpy.utils.register_class(TM_Panel3b)
    bpy.utils.register_class(TM_Panel4)
    bpy.utils.register_class(ApplyRotSca)
    bpy.utils.register_class(SelCurs)
    bpy.utils.register_class(CursorTOSelection)
    bpy.utils.register_class(Cursor)
    bpy.utils.register_class(OriginToCursor)
    bpy.utils.register_class(EditMode)
    bpy.utils.register_class(FakeShad)
    bpy.utils.register_class(ProjShad)
    bpy.utils.register_class(MaxBox)
    bpy.utils.register_class(LightFProj)
    bpy.utils.register_class(Light)
    bpy.utils.register_class(WheelMin)
    bpy.utils.register_class(Flames)
	
def unregister():
    bpy.utils.unregister_class(TM_Panel)
    bpy.utils.unregister_class(TM_Panel2)
    bpy.utils.unregister_class(TM_Panel3)
    bpy.utils.unregister_class(TM_Panel3b)
    bpy.utils.unregister_class(TM_Panel4)
    bpy.utils.unregister_class(ApplyRotSca)
    bpy.utils.unregister_class(SelCurs)
    bpy.utils.unregister_class(CursorTOSelection)
    bpy.utils.unregister_class(Cursor)
    bpy.utils.unregister_class(OriginToCursor)
    bpy.utils.unregister_class(EditMode)
    bpy.utils.unregister_class(FakeShad)
    bpy.utils.unregister_class(ProjShad)
    bpy.utils.unregister_class(MaxBox)
    bpy.utils.unregister_class(LightFProj)
    bpy.utils.unregister_class(Light)
    bpy.utils.unregister_class(WheelMin)
    bpy.utils.unregister_class(Flames)
    
if __name__ == "__main__":
    register()