# ##### BEGIN GPL LICENSE BLOCK #####
#
# Mesh Align Plus-Build precision models using scene geometry/measurements.
# Copyright (C) 2015 Eric Gentry
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####
#
# <pep8 compliant>





# Blender requires addons to provide this information.
bl_info = {
    "name": "TM script",
    "description": (
        "Script for Carpark ManiaPark"
    ),
    "author": "JustSpeeding",
    "version": (1, 0, 3),
    "blender": (2, 80, 0),
    "location": ("3D View > N Panel > TM tab, and"),
    "warning": (""),
    "wiki_url": ("https://github.com/Justspeeding/TM_Script-2.79b/wiki"),
    "support": "COMMUNITY",
    "category": "Mesh"
}

import bpy
#panel1

class JS_PT_panel1(bpy.types.Panel):
    bl_idname = "JS_PT_panel1"
    bl_label = "ObjectData" 
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
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


 #panel2       
class JS_PT_panel2(bpy.types.Panel):
    bl_idname = "JS_PT_panel2"
    bl_label = "Suspention Helpers"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = "TM"
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        

        col = layout.column(align=True)
        obj = context.active_object
        obj = context.object
        col.operator_menu_enum("object.origin_set", "type", text="Set Origin")
        row = layout.row()
        row.operator("myops.add_selcurs", icon='EMPTY_DATA')
        row = layout.row()
        row.operator("myops.add_cursortoselection", icon='OUTLINER_OB_EMPTY')
        row = layout.row()
        row.operator("myops.add_curs", icon='ARROW_LEFTRIGHT')
        row = layout.row()
        row.operator("myops.add_origintocursor", icon='ADD')
        row = layout.row()		       
        row.operator("myops.add_applyrotsca", icon='NDOF_DOM')
        row = layout.row()
        row.operator("myops.add_edit", icon='OBJECT_DATA')
 #panel3       
class JS_PT_panel3(bpy.types.Panel):
    bl_idname = "JS_PT_panel3"
    bl_label = "Add TM Objects"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = "TM"
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        obj = context.object
       
        row = layout.row()
        row.operator("myops.add_fakeshad" , icon='MESH_PLANE')
        
       
        row = layout.row()
        row.operator("myops.add_maxbox" , icon='MESH_CUBE')       
		
                        
        row = layout.row()
        row.operator("myops.add_wheelmin" , icon='AUTO')     

        row = layout.row()
        row.operator("myops.add_flames" , icon='PMARKER_ACT')  

 #panel4      
class JS_PT_panel4(bpy.types.Panel):
    bl_idname = "JS_PT_panel4"
    bl_label = "Add TMUF Objects"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = "TM"
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        obj = context.object
       
        row = layout.row()
        row.operator("myops.add_projshad" , icon='MESH_PLANE')
        row = layout.row() 	
        row.operator("myops.add_light" , icon='RADIOBUT_ON') 
        row = layout.row()
        row.operator("myops.add_lightfproj" , icon='RADIOBUT_OFF')  
        
 #panel5      
class JS_PT_panel5(bpy.types.Panel):
    bl_idname = "JS_PT_panel5"
    bl_label = "Add Modifier"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = "TM"
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        obj = context.object

        row = layout.row()
        row.operator("object.modifier_add", text="CURVE", icon="MOD_CURVE").type='CURVE' 
        row = layout.row()
        row.operator("object.modifier_add", text="ARRAY", icon="MOD_ARRAY").type='ARRAY'
        row = layout.row()
        row.operator("object.modifier_add", text="DECIMATE", icon="MOD_DECIM").type='DECIMATE'  
 
 
 
        
# apply rotation and scale  'Xform 3dsmax'
class JS_OT_ApplyRotSca(bpy.types.Operator):
    """Apply Rotation & Scale\nApplies the current rotation and scale"""
    bl_idname = "myops.add_applyrotsca"
    bl_label = "Reset Xform"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        self.report({'INFO'}, "reset Done")
        return {'FINISHED'}
    
		# Selection To Cursor 
class JS_OT_SelCurs(bpy.types.Operator):
    """set selection to cursor"""
    bl_idname = "myops.add_selcurs"
    bl_label = "SelectionToCursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        return {'FINISHED'}
		
			# set Cursor 0.0.0
class JS_OT_Cursor(bpy.types.Operator):
    """set cursor to 0.0.0"""
    bl_idname = "myops.add_curs"
    bl_label = "set cursor to 0.0.0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        return {'FINISHED'}

		# Cursor To Selection
class JS_OT_CursorTOSelection(bpy.types.Operator):
    """set cursor to selection"""
    bl_idname = "myops.add_cursortoselection"
    bl_label = "CursorToSelection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {'FINISHED'}

		# Origin TO Cursor
class JS_OT_OriginToCursor(bpy.types.Operator):
    """set origin to cursor """
    bl_idname = "myops.add_origintocursor"
    bl_label = "OriginToCursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return {'FINISHED'}

		# Edit objectmode
class JS_OT_EditMode(bpy.types.Operator):
    """switch edit object mode"""
    bl_idname = "myops.add_edit"
    bl_label = "Edit/object Mode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


 		# Edit objectmode
 
 #fakeshad
class JS_OT_FakeShad(bpy.types.Operator):
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
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False))
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False))

        
       


        
        return {'FINISHED'}
    
#Projshad
class JS_OT_ProjShad(bpy.types.Operator):
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
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False))
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False))

        
        return {'FINISHED'}

#maxbox
class JS_OT_MaxBox(bpy.types.Operator):
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

class JS_OT_LightFProj(bpy.types.Operator):
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
		
class JS_OT_Light(bpy.types.Operator):
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
 
 
class JS_OT_WheelMin(bpy.types.Operator):
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
    
class JS_OT_Flames(bpy.types.Operator):
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

classes = (
	JS_PT_panel1,
    JS_PT_panel2,
    JS_PT_panel3,
    JS_PT_panel4,
    JS_PT_panel5,
    JS_OT_ApplyRotSca,
    JS_OT_SelCurs,
    JS_OT_CursorTOSelection,
    JS_OT_Cursor,
    JS_OT_OriginToCursor,
    JS_OT_EditMode,
    JS_OT_FakeShad,
    JS_OT_ProjShad,
    JS_OT_MaxBox,
    JS_OT_LightFProj,
    JS_OT_Light,
    JS_OT_WheelMin,
    JS_OT_Flames
    
	)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
def register():
    bpy.utils.register_class(JS_PT_panel1)
    bpy.utils.register_class(JS_PT_panel2)
    bpy.utils.register_class(JS_PT_panel3)
    bpy.utils.register_class(JS_PT_panel4)
    bpy.utils.register_class(JS_PT_panel5)
    bpy.utils.register_class(JS_OT_ApplyRotSca)
    bpy.utils.register_class(JS_OT_SelCurs)
    bpy.utils.register_class(JS_OT_CursorTOSelection)
    bpy.utils.register_class(JS_OT_Cursor)
    bpy.utils.register_class(JS_OT_OriginToCursor)
    bpy.utils.register_class(JS_OT_EditMode)
    bpy.utils.register_class(JS_OT_FakeShad)
    bpy.utils.register_class(JS_OT_ProjShad)
    bpy.utils.register_class(JS_OT_MaxBox)
    bpy.utils.register_class(JS_OT_LightFProj)
    bpy.utils.register_class(JS_OT_Light)
    bpy.utils.register_class(JS_OT_WheelMin)
    bpy.utils.register_class(JS_OT_Flames)
	
def unregister():
    bpy.utils.unregister_class(JS_PT_panel1)
    bpy.utils.unregister_class(JS_PT_panel2)
    bpy.utils.unregister_class(JS_PT_panel3)
    bpy.utils.unregister_class(JS_PT_panel4)
    bpy.utils.unregister_class(JS_PT_panel5)
    bpy.utils.unregister_class(JS_OT_ApplyRotSca)
    bpy.utils.unregister_class(JS_OT_SelCurs)
    bpy.utils.unregister_class(JS_OT_CursorTOSelection)
    bpy.utils.unregister_class(JS_OT_Cursor)
    bpy.utils.unregister_class(JS_OT_OriginToCursor)
    bpy.utils.unregister_class(JS_OT_EditMode)
    bpy.utils.unregister_class(JS_OT_FakeShad)
    bpy.utils.unregister_class(JS_OT_ProjShad)
    bpy.utils.unregister_class(JS_OT_MaxBox)
    bpy.utils.unregister_class(JS_OT_LightFProj)
    bpy.utils.unregister_class(JS_OT_Light)
    bpy.utils.unregister_class(JS_OT_WheelMin)
    bpy.utils.unregister_class(JS_OT_Flames)



if __name__ == "__main__":
    register()
