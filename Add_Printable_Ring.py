'''
Copyright (C) 2016 Ákos Nikházy
nikhazy.akos@gmail.com

Created by Ákos Nikházy
	
    This will work only with Blender 2.7 only.
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
bl_info = {
    "name": "Add Basic 3D Printable Ring",
    "author": "Ákos Nikházy",
    "version": (1, 0),
    "blender": (2, 70, 0),
    "location": "View3D",
    "description": "Add a 3D printable basic ring. 80 different ring size from all over the world, US sizes shown, international ones in tooltips",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

import bpy
from bpy.props import StringProperty

def mmToUnit(n):
    return n/1000

def basicRingFor3DPrint(objName, v, d):
    bpy.ops.mesh.primitive_circle_add(
        vertices=v, 
        radius=mmToUnit(d)/2,
        enter_editmode=False, 
    )
    ob = bpy.context.active_object
    ob.name = objName
    me = ob.data
    me.name = objName + 'Mesh'
    
    bpy.ops.object.mode_set( mode   = 'EDIT'   )
    bpy.ops.mesh.select_mode( type  = 'VERT'   )
    bpy.ops.mesh.select_all( action = 'SELECT' )

    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(0, 0, 0.005)}
    )

    bpy.ops.object.mode_set( mode = 'OBJECT' )
    
    bpy.ops.object.modifier_add(type = 'SOLIDIFY')
    ob.modifiers['Solidify'].thickness = 0.002
    
    bpy.ops.object.modifier_add(type = 'BEVEL')
    ob.modifiers['Bevel'].width = 0.0003
    ob.modifiers['Bevel'].segments = 2
    
    return ob


class AddPrintableRingOperator0(bpy.types.Operator):
     """Add 9.91mm (US 0000 | British - | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator0"
     bl_label = "Add 9.91mm (0000)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 9.91)
         return {'FINISHED'}
		 
class AddPrintableRingOperator1(bpy.types.Operator):
     """Add 10.72mm (US 00 | British - | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator1"
     bl_label = "Add 10.72mm (00)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 10.72)
         return {'FINISHED'}
		 
class AddPrintableRingOperator2(bpy.types.Operator):
     """Add 11.53mm (US 0 | British - | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator2"
     bl_label = "Add 11.53mm (0)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 11.53)
         return {'FINISHED'}
		 
class AddPrintableRingOperator3(bpy.types.Operator):
     """Add 11.95mm (US 1/2 | British A | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator3"
     bl_label = "Add 11.95mm (1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 11.95)
         return {'FINISHED'}
		 
class AddPrintableRingOperator4(bpy.types.Operator):
     """Add 12.18mm (US 3/4 | British A 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator4"
     bl_label = "Add 12.18mm (3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 12.18)
         return {'FINISHED'}
		 
class AddPrintableRingOperator5(bpy.types.Operator):
     """Add 12.37mm (US 1 | British B | French - | German - | Japanese 1 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator5"
     bl_label = "Add 12.37mm (1)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 12.37)
         return {'FINISHED'}
		 
class AddPrintableRingOperator6(bpy.types.Operator):
     """Add 12.6mm (US 1 1/4 | British B 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator6"
     bl_label = "Add 12.6mm (1 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 12.6)
         return {'FINISHED'}
		 
class AddPrintableRingOperator7(bpy.types.Operator):
     """Add 12.78mm (US 1 1/2 | British C | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator7"
     bl_label = "Add 12.78mm (1 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 12.78)
         return {'FINISHED'}
		 
class AddPrintableRingOperator8(bpy.types.Operator):
     """Add 13mm (US 1 3/4 | British C 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator8"
     bl_label = "Add 13mm (1 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 13)
         return {'FINISHED'}
		 
class AddPrintableRingOperator9(bpy.types.Operator):
     """Add 13.21mm (US 2 | British D | French 41 1/2 | German 13 1/2 | Japanese 2 | Swiss 1 1/2)"""
     bl_idname = "addongen.add_printable_ring_operator9"
     bl_label = "Add 13.21mm (2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 13.21)
         return {'FINISHED'}
		 
class AddPrintableRingOperator10(bpy.types.Operator):
     """Add 13.41mm (US 2 1/4 | British D 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator10"
     bl_label = "Add 13.41mm (2 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 13.41)
         return {'FINISHED'}
		 
class AddPrintableRingOperator11(bpy.types.Operator):
     """Add 13.61mm (US 2 1/2 | British E | French 42 3/4 | German 13 3/4 | Japanese 3 | Swiss 2 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator11"
     bl_label = "Add 13.61mm (2 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 13.61)
         return {'FINISHED'}
		 
class AddPrintableRingOperator12(bpy.types.Operator):
     """Add 13.83mm (US 2 3/4 | British E 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator12"
     bl_label = "Add 13.83mm (2 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 13.83)
         return {'FINISHED'}
		 
class AddPrintableRingOperator13(bpy.types.Operator):
     """Add 14.05mm (US 3 | British F | French 44 | German 14 | Japanese 4 | Swiss 4)"""
     bl_idname = "addongen.add_printable_ring_operator13"
     bl_label = "Add 14.05mm (3)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.05)
         return {'FINISHED'}
		 
class AddPrintableRingOperator14(bpy.types.Operator):
     """Add 14.15mm (US 3 1/8 | British F 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator14"
     bl_label = "Add 14.15mm (3 1/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.15)
         return {'FINISHED'}
		 
class AddPrintableRingOperator15(bpy.types.Operator):
     """Add 14.25mm (US 3 1/4 | British F 3/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator15"
     bl_label = "Add 14.25mm (3 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.25)
         return {'FINISHED'}
		 
class AddPrintableRingOperator16(bpy.types.Operator):
     """Add 14.36mm (US 3 3/8 | British G | French 45 1/4 | German - | Japanese 5 | Swiss 5 1/4)"""
     bl_idname = "addongen.add_printable_ring_operator16"
     bl_label = "Add 14.36mm (3 3/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.36)
         return {'FINISHED'}
		 
class AddPrintableRingOperator17(bpy.types.Operator):
     """Add 14.45mm (US 3 1/2 | British G 1/4 | French - | German 14 1/2 | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator17"
     bl_label = "Add 14.45mm (3 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.45)
         return {'FINISHED'}
		 
class AddPrintableRingOperator18(bpy.types.Operator):
     """Add 14.56mm (US 3 5/8 | British G 1/2 | French - | German - | Japanese 6 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator18"
     bl_label = "Add 14.56mm (3 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.56)
         return {'FINISHED'}
		 
class AddPrintableRingOperator19(bpy.types.Operator):
     """Add 14.65mm (US 3 3/4 | British H | French 46 1/2 | German - | Japanese - | Swiss 6 1/2)"""
     bl_idname = "addongen.add_printable_ring_operator19"
     bl_label = "Add 14.65mm (3 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.65)
         return {'FINISHED'}
		 
class AddPrintableRingOperator20(bpy.types.Operator):
     """Add 14.86mm (US 4 | British H 1/2 | French - | German 15 | Japanese 7 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator20"
     bl_label = "Add 14.86mm (4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 14.86)
         return {'FINISHED'}
		 
class AddPrintableRingOperator21(bpy.types.Operator):
     """Add 15.04mm (US 4 1/4 | British I | French 47 3/4 | German - | Japanese - | Swiss 7 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator21"
     bl_label = "Add 15.04mm (4 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.04)
         return {'FINISHED'}
		 
class AddPrintableRingOperator22(bpy.types.Operator):
     """Add 15.27mm (US 4 1/2 | British I 1/2 | French - | German 15 1/4 | Japanese 8 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator22"
     bl_label = "Add 15.27mm (4 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.27)
         return {'FINISHED'}
		 
class AddPrintableRingOperator23(bpy.types.Operator):
     """Add 15.4mm (US 4 5/8 | British J | French 49 | German 15 1/2 | Japanese - | Swiss 9)"""
     bl_idname = "addongen.add_printable_ring_operator23"
     bl_label = "Add 15.4mm (4 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.4)
         return {'FINISHED'}
		 
class AddPrintableRingOperator24(bpy.types.Operator):
     """Add 15.53mm (US 4 3/4 | British J 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator24"
     bl_label = "Add 15.53mm (4 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.53)
         return {'FINISHED'}
		 
class AddPrintableRingOperator25(bpy.types.Operator):
     """Add 15.7mm (US 5 | British J 1/2 | French - | German 15 3/4 | Japanese 9 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator25"
     bl_label = "Add 15.7mm (5)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.7)
         return {'FINISHED'}
		 
class AddPrintableRingOperator26(bpy.types.Operator):
     """Add 15.8mm (US 5 1/8 | British K | French 50 | German - | Japanese - | Swiss 10)"""
     bl_idname = "addongen.add_printable_ring_operator26"
     bl_label = "Add 15.8mm (5 1/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.8)
         return {'FINISHED'}
		 
class AddPrintableRingOperator27(bpy.types.Operator):
     """Add 15.9mm (US 5 1/4 | British K 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator27"
     bl_label = "Add 15.9mm (5 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 15.9)
         return {'FINISHED'}
		 
class AddPrintableRingOperator28(bpy.types.Operator):
     """Add 16mm (US 5 3/8 | British K 1/2 | French - | German - | Japanese 10 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator28"
     bl_label = "Add 16mm (5 3/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16)
         return {'FINISHED'}
		 
class AddPrintableRingOperator29(bpy.types.Operator):
     """Add 16.1mm (US 5 1/2 | British L | French 51 3/4 | German 16 | Japanese - | Swiss 11 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator29"
     bl_label = "Add 16.1mm (5 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.1)
         return {'FINISHED'}
		 
class AddPrintableRingOperator30(bpy.types.Operator):
     """Add 16.3mm (US 5 3/4 | British L 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator30"
     bl_label = "Add 16.3mm (5 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.3)
         return {'FINISHED'}
		 
class AddPrintableRingOperator31(bpy.types.Operator):
     """Add 16.41mm (US 5 7/8 | British L 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator31"
     bl_label = "Add 16.41mm (5 7/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.41)
         return {'FINISHED'}
		 
class AddPrintableRingOperator32(bpy.types.Operator):
     """Add 16.51mm (US 6 | British M | French 52 3/4 | German 16 1/2 | Japanese 12 | Swiss 12 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator32"
     bl_label = "Add 16.51mm (6)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.51)
         return {'FINISHED'}
		 
class AddPrintableRingOperator33(bpy.types.Operator):
     """Add 16.71mm (US 6 1/4 | British M 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator33"
     bl_label = "Add 16.71mm (6 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.71)
         return {'FINISHED'}
		 
class AddPrintableRingOperator34(bpy.types.Operator):
     """Add 16.92mm (US 6 1/2 | British N | French 54 | German 17 | Japanese 13 | Swiss 14)"""
     bl_idname = "addongen.add_printable_ring_operator34"
     bl_label = "Add 16.92mm (6 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 16.92)
         return {'FINISHED'}
		 
class AddPrintableRingOperator35(bpy.types.Operator):
     """Add 17.13mm (US 6 3/4 | British N 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator35"
     bl_label = "Add 17.13mm (6 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 17.13)
         return {'FINISHED'}
		 
class AddPrintableRingOperator36(bpy.types.Operator):
     """Add 17.35mm (US 7 | British O | French 55 1/4 | German 17 1/4 | Japanese 14 | Swiss 15 1/4)"""
     bl_idname = "addongen.add_printable_ring_operator36"
     bl_label = "Add 17.35mm (7)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 17.35)
         return {'FINISHED'}
		 
class AddPrintableRingOperator37(bpy.types.Operator):
     """Add 17.45mm (US 7 1/4 | British O 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator37"
     bl_label = "Add 17.45mm (7 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 17.45)
         return {'FINISHED'}
		 
class AddPrintableRingOperator38(bpy.types.Operator):
     """Add 17.75mm (US 7 1/2 | British P | French 56 1/2 | German 17 3/4 | Japanese 15 | Swiss 16 1/2)"""
     bl_idname = "addongen.add_printable_ring_operator38"
     bl_label = "Add 17.75mm (7 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 17.75)
         return {'FINISHED'}
		 
class AddPrintableRingOperator39(bpy.types.Operator):
     """Add 17.97mm (US 7 3/4 | British P 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator39"
     bl_label = "Add 17.97mm (7 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 17.97)
         return {'FINISHED'}
		 
class AddPrintableRingOperator40(bpy.types.Operator):
     """Add 18.19mm (US 8 | British Q | French 57 3/4 | German 18 | Japanese 16 | Swiss 17 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator40"
     bl_label = "Add 18.19mm (8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.19)
         return {'FINISHED'}
		 
class AddPrintableRingOperator41(bpy.types.Operator):
     """Add 18.35mm (US 8 1/4 | British Q 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator41"
     bl_label = "Add 18.35mm (8 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.35)
         return {'FINISHED'}
		 
class AddPrintableRingOperator42(bpy.types.Operator):
     """Add 18.53mm (US 8 1/2 | British Q 3/4 | French - | German 18 1/2 | Japanese 17 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator42"
     bl_label = "Add 18.53mm (8 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.53)
         return {'FINISHED'}
		 
class AddPrintableRingOperator43(bpy.types.Operator):
     """Add 18.61mm (US 8 5/8 | British R | French 59 | German - | Japanese - | Swiss 19)"""
     bl_idname = "addongen.add_printable_ring_operator43"
     bl_label = "Add 18.61mm (8 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.61)
         return {'FINISHED'}
		 
class AddPrintableRingOperator44(bpy.types.Operator):
     """Add 18.69mm (US 8 3/4 | British R 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator44"
     bl_label = "Add 18.69mm (8 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.69)
         return {'FINISHED'}
		 
class AddPrintableRingOperator45(bpy.types.Operator):
     """Add 18.8mm (US 8 7/8 | British R 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator45"
     bl_label = "Add 18.8mm (8 7/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.8)
         return {'FINISHED'}
		 
class AddPrintableRingOperator46(bpy.types.Operator):
     """Add 18.89mm (US 9 | British R 3/4 | French - | German 19 | Japanese 18 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator46"
     bl_label = "Add 18.89mm (9)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 18.89)
         return {'FINISHED'}
		 
class AddPrintableRingOperator47(bpy.types.Operator):
     """Add 19.1mm (US 9 1/8 | British S | French 60 1/4 | German - | Japanese - | Swiss 20 1/4)"""
     bl_idname = "addongen.add_printable_ring_operator47"
     bl_label = "Add 19.1mm (9 1/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.1)
         return {'FINISHED'}
		 
class AddPrintableRingOperator48(bpy.types.Operator):
     """Add 19.22mm (US 9 1/4 | British S 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator48"
     bl_label = "Add 19.22mm (9 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.22)
         return {'FINISHED'}
		 
class AddPrintableRingOperator49(bpy.types.Operator):
     """Add 19.31mm (US 9 3/8 | British S 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator49"
     bl_label = "Add 19.31mm (9 3/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.31)
         return {'FINISHED'}
		 
class AddPrintableRingOperator50(bpy.types.Operator):
     """Add 19.41mm (US 9 1/2 | British S 3/4 | French - | German 19 1/2 | Japanese 19 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator50"
     bl_label = "Add 19.41mm (9 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.41)
         return {'FINISHED'}
		 
class AddPrintableRingOperator51(bpy.types.Operator):
     """Add 19.51mm (US 9 5/8 | British T | French 61 1/2 | German - | Japanese - | Swiss 21 1/2)"""
     bl_idname = "addongen.add_printable_ring_operator51"
     bl_label = "Add 19.51mm (9 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.51)
         return {'FINISHED'}
		 
class AddPrintableRingOperator52(bpy.types.Operator):
     """Add 19.62mm (US 9 3/4 | British T 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator52"
     bl_label = "Add 19.62mm (9 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.62)
         return {'FINISHED'}
		 
class AddPrintableRingOperator53(bpy.types.Operator):
     """Add 19.84mm (US 10 | British T 1/2 | French - | German 20 | Japanese 20 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator53"
     bl_label = "Add 19.84mm (10)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 19.84)
         return {'FINISHED'}
		 
class AddPrintableRingOperator54(bpy.types.Operator):
     """Add 20.02mm (US 10 1/4 | British U | French 62 3/4 | German - | Japanese 21 | Swiss 22 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator54"
     bl_label = "Add 20.02mm (10 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.02)
         return {'FINISHED'}
		 
class AddPrintableRingOperator55(bpy.types.Operator):
     """Add 20.2mm (US 10 1/2 | British U 1/2 | French - | German 20 1/4 | Japanese 22 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator55"
     bl_label = "Add 20.2mm (10 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.2)
         return {'FINISHED'}
		 
class AddPrintableRingOperator56(bpy.types.Operator):
     """Add 20.32mm (US 10 5/8 | British V | French 63 | German - | Japanese - | Swiss 23 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator56"
     bl_label = "Add 20.32mm (10 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.32)
         return {'FINISHED'}
		 
class AddPrintableRingOperator57(bpy.types.Operator):
     """Add 20.44mm (US 10 3/4 | British V 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator57"
     bl_label = "Add 20.44mm (10 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.44)
         return {'FINISHED'}
		 
class AddPrintableRingOperator58(bpy.types.Operator):
     """Add 20.68mm (US 11 | British V 1/2 | French - | German 20 3/4 | Japanese 23 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator58"
     bl_label = "Add 20.68mm (11)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.68)
         return {'FINISHED'}
		 
class AddPrintableRingOperator59(bpy.types.Operator):
     """Add 20.76mm (US 11 1/8 | British W | French 65 | German - | Japanese - | Swiss 25)"""
     bl_idname = "addongen.add_printable_ring_operator59"
     bl_label = "Add 20.76mm (11 1/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.76)
         return {'FINISHED'}
		 
class AddPrintableRingOperator60(bpy.types.Operator):
     """Add 20.85mm (US 11 1/4 | British W 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator60"
     bl_label = "Add 20.85mm (11 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.85)
         return {'FINISHED'}
		 
class AddPrintableRingOperator61(bpy.types.Operator):
     """Add 20.94mm (US 11 3/8 | British W 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator61"
     bl_label = "Add 20.94mm (11 3/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 20.94)
         return {'FINISHED'}
		 
class AddPrintableRingOperator62(bpy.types.Operator):
     """Add 21.08mm (US 11 1/2 | British W 3/4 | French - | German 21 | Japanese 24 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator62"
     bl_label = "Add 21.08mm (11 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.08)
         return {'FINISHED'}
		 
class AddPrintableRingOperator63(bpy.types.Operator):
     """Add 21.18mm (US 11 5/8 | British X | French 66 1/4 | German - | Japanese - | Swiss 26 1/4)"""
     bl_idname = "addongen.add_printable_ring_operator63"
     bl_label = "Add 21.18mm (11 5/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.18)
         return {'FINISHED'}
		 
class AddPrintableRingOperator64(bpy.types.Operator):
     """Add 21.24mm (US 11 3/4 | British X 1/4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator64"
     bl_label = "Add 21.24mm (11 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.24)
         return {'FINISHED'}
		 
class AddPrintableRingOperator65(bpy.types.Operator):
     """Add 21.3mm (US 11 7/8 | British X 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator65"
     bl_label = "Add 21.3mm (11 7/8)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.3)
         return {'FINISHED'}
		 
class AddPrintableRingOperator66(bpy.types.Operator):
     """Add 21.49mm (US 12 | British Y | French 67 1/2 | German 21 1/4 | Japanese 25 | Swiss 27 1/2)"""
     bl_idname = "addongen.add_printable_ring_operator66"
     bl_label = "Add 21.49mm (12)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.49)
         return {'FINISHED'}
		 
class AddPrintableRingOperator67(bpy.types.Operator):
     """Add 21.69mm (US 12 1/4 | British Y 1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator67"
     bl_label = "Add 21.69mm (12 1/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.69)
         return {'FINISHED'}
		 
class AddPrintableRingOperator68(bpy.types.Operator):
     """Add 21.89mm (US 12 1/2 | British Z | French 68 3/4 | German 21 3/4 | Japanese 26 | Swiss 28 3/4)"""
     bl_idname = "addongen.add_printable_ring_operator68"
     bl_label = "Add 21.89mm (12 1/2)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 21.89)
         return {'FINISHED'}
		 
class AddPrintableRingOperator69(bpy.types.Operator):
     """Add 22.1mm (US 12 3/4 | British Z +1/2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator69"
     bl_label = "Add 22.1mm (12 3/4)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 22.1)
         return {'FINISHED'}
		 
class AddPrintableRingOperator70(bpy.types.Operator):
     """Add 22.33mm (US 13 | British Z+1 | French - | German 22 | Japanese 27 | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator70"
     bl_label = "Add 22.33mm (13)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 22.33)
         return {'FINISHED'}
		 
class AddPrintableRingOperator71(bpy.types.Operator):
     """Add 22.6mm (US 13.5 | British Z+1.5 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator71"
     bl_label = "Add 22.6mm (13.5)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 22.6)
         return {'FINISHED'}
		 
class AddPrintableRingOperator72(bpy.types.Operator):
     """Add 22.69mm (US - | British Z+2 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator72"
     bl_label = "Add 22.69mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 22.69)
         return {'FINISHED'}
		 
class AddPrintableRingOperator73(bpy.types.Operator):
     """Add 22.92mm (US - | British Z+2.5 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator73"
     bl_label = "Add 22.92mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 22.92)
         return {'FINISHED'}
		 
class AddPrintableRingOperator74(bpy.types.Operator):
     """Add 23.06mm (US - | British Z+3 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator74"
     bl_label = "Add 23.06mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 23.06)
         return {'FINISHED'}
		 
class AddPrintableRingOperator75(bpy.types.Operator):
     """Add 23.24mm (US - | British Z+3.5 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator75"
     bl_label = "Add 23.24mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 23.24)
         return {'FINISHED'}
		 
class AddPrintableRingOperator76(bpy.types.Operator):
     """Add 23.47mm (US - | British Z+4 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator76"
     bl_label = "Add 23.47mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 23.47)
         return {'FINISHED'}
		 
class AddPrintableRingOperator77(bpy.types.Operator):
     """Add 23.55mm (US - | British Z+4.5 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator77"
     bl_label = "Add 23.55mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 23.55)
         return {'FINISHED'}
		 
class AddPrintableRingOperator78(bpy.types.Operator):
     """Add 23.87mm (US - | British Z+5 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator78"
     bl_label = "Add 23.87mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 23.87)
         return {'FINISHED'}
		 
class AddPrintableRingOperator79(bpy.types.Operator):
     """Add 24.27mm (US - | British Z+6 | French - | German - | Japanese - | Swiss -)"""
     bl_idname = "addongen.add_printable_ring_operator79"
     bl_label = "Add 24.27mm (-)"
     bl_options = {'REGISTER'}
	 
     def execute(self, context):
         basicRingFor3DPrint('ring', 64, 24.27)
         return {'FINISHED'}
		 
    
class AddPrintableRingPanel(bpy.types.Panel):
    """Docstring of AddPrintableRing"""
    bl_idname = "VIEW3D_PT_add_printable_ring"
    bl_label = "Add Printable Ring"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Create'
    
    def draw(self, context):
        
        layout = self.layout
        layout.operator(AddPrintableRingOperator0.bl_idname, text = "Add 9.91mm (US 0000)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator1.bl_idname, text = "Add 10.72mm (US 00)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator2.bl_idname, text = "Add 11.53mm (US 0)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator3.bl_idname, text = "Add 11.95mm (US 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator4.bl_idname, text = "Add 12.18mm (US 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator5.bl_idname, text = "Add 12.37mm (US 1)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator6.bl_idname, text = "Add 12.6mm (US 1 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator7.bl_idname, text = "Add 12.78mm (US 1 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator8.bl_idname, text = "Add 13mm (US 1 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator9.bl_idname, text = "Add 13.21mm (US 2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator10.bl_idname, text = "Add 13.41mm (US 2 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator11.bl_idname, text = "Add 13.61mm (US 2 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator12.bl_idname, text = "Add 13.83mm (US 2 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator13.bl_idname, text = "Add 14.05mm (US 3)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator14.bl_idname, text = "Add 14.15mm (US 3 1/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator15.bl_idname, text = "Add 14.25mm (US 3 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator16.bl_idname, text = "Add 14.36mm (US 3 3/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator17.bl_idname, text = "Add 14.45mm (US 3 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator18.bl_idname, text = "Add 14.56mm (US 3 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator19.bl_idname, text = "Add 14.65mm (US 3 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator20.bl_idname, text = "Add 14.86mm (US 4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator21.bl_idname, text = "Add 15.04mm (US 4 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator22.bl_idname, text = "Add 15.27mm (US 4 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator23.bl_idname, text = "Add 15.4mm (US 4 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator24.bl_idname, text = "Add 15.53mm (US 4 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator25.bl_idname, text = "Add 15.7mm (US 5)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator26.bl_idname, text = "Add 15.8mm (US 5 1/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator27.bl_idname, text = "Add 15.9mm (US 5 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator28.bl_idname, text = "Add 16mm (US 5 3/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator29.bl_idname, text = "Add 16.1mm (US 5 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator30.bl_idname, text = "Add 16.3mm (US 5 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator31.bl_idname, text = "Add 16.41mm (US 5 7/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator32.bl_idname, text = "Add 16.51mm (US 6)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator33.bl_idname, text = "Add 16.71mm (US 6 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator34.bl_idname, text = "Add 16.92mm (US 6 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator35.bl_idname, text = "Add 17.13mm (US 6 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator36.bl_idname, text = "Add 17.35mm (US 7)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator37.bl_idname, text = "Add 17.45mm (US 7 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator38.bl_idname, text = "Add 17.75mm (US 7 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator39.bl_idname, text = "Add 17.97mm (US 7 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator40.bl_idname, text = "Add 18.19mm (US 8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator41.bl_idname, text = "Add 18.35mm (US 8 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator42.bl_idname, text = "Add 18.53mm (US 8 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator43.bl_idname, text = "Add 18.61mm (US 8 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator44.bl_idname, text = "Add 18.69mm (US 8 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator45.bl_idname, text = "Add 18.8mm (US 8 7/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator46.bl_idname, text = "Add 18.89mm (US 9)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator47.bl_idname, text = "Add 19.1mm (US 9 1/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator48.bl_idname, text = "Add 19.22mm (US 9 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator49.bl_idname, text = "Add 19.31mm (US 9 3/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator50.bl_idname, text = "Add 19.41mm (US 9 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator51.bl_idname, text = "Add 19.51mm (US 9 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator52.bl_idname, text = "Add 19.62mm (US 9 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator53.bl_idname, text = "Add 19.84mm (US 10)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator54.bl_idname, text = "Add 20.02mm (US 10 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator55.bl_idname, text = "Add 20.2mm (US 10 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator56.bl_idname, text = "Add 20.32mm (US 10 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator57.bl_idname, text = "Add 20.44mm (US 10 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator58.bl_idname, text = "Add 20.68mm (US 11)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator59.bl_idname, text = "Add 20.76mm (US 11 1/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator60.bl_idname, text = "Add 20.85mm (US 11 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator61.bl_idname, text = "Add 20.94mm (US 11 3/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator62.bl_idname, text = "Add 21.08mm (US 11 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator63.bl_idname, text = "Add 21.18mm (US 11 5/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator64.bl_idname, text = "Add 21.24mm (US 11 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator65.bl_idname, text = "Add 21.3mm (US 11 7/8)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator66.bl_idname, text = "Add 21.49mm (US 12)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator67.bl_idname, text = "Add 21.69mm (US 12 1/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator68.bl_idname, text = "Add 21.89mm (US 12 1/2)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator69.bl_idname, text = "Add 22.1mm (US 12 3/4)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator70.bl_idname, text = "Add 22.33mm (US 13)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator71.bl_idname, text = "Add 22.6mm (US 13.5)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator72.bl_idname, text = "Add 22.69mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator73.bl_idname, text = "Add 22.92mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator74.bl_idname, text = "Add 23.06mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator75.bl_idname, text = "Add 23.24mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator76.bl_idname, text = "Add 23.47mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator77.bl_idname, text = "Add 23.55mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator78.bl_idname, text = "Add 23.87mm (US -)")
        layout = self.layout
        layout.operator(AddPrintableRingOperator79.bl_idname, text = "Add 24.27mm (US -)")
        
class AddPrintableRingMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_add_printable_ring"
    bl_label = "Add Printable Ring Menu"

    def draw(self, context):
        
        layout = self.layout
        layout.operator(AddPrintableRingOperator0.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator1.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator2.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator3.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator4.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator5.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator6.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator7.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator8.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator9.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator10.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator11.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator12.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator13.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator14.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator15.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator16.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator17.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator18.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator19.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator20.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator21.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator22.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator23.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator24.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator25.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator26.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator27.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator28.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator29.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator30.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator31.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator32.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator33.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator34.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator35.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator36.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator37.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator38.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator39.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator40.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator41.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator42.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator43.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator44.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator45.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator46.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator47.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator48.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator49.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator50.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator51.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator52.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator53.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator54.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator55.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator56.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator57.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator58.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator59.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator60.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator61.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator62.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator63.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator64.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator65.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator66.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator67.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator68.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator69.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator70.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator71.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator72.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator73.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator74.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator75.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator76.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator77.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator78.bl_idname)
        layout = self.layout
        layout.operator(AddPrintableRingOperator79.bl_idname)
        layout.separator()
        layout.menu("VIEW3D_MT_transform")
        layout.operator_menu_enum("object.select_by_type", "type", text="Select All by Type...")



def register():
        bpy.utils.register_class(AddPrintableRingOperator0)
        bpy.utils.register_class(AddPrintableRingOperator1)
        bpy.utils.register_class(AddPrintableRingOperator2)
        bpy.utils.register_class(AddPrintableRingOperator3)
        bpy.utils.register_class(AddPrintableRingOperator4)
        bpy.utils.register_class(AddPrintableRingOperator5)
        bpy.utils.register_class(AddPrintableRingOperator6)
        bpy.utils.register_class(AddPrintableRingOperator7)
        bpy.utils.register_class(AddPrintableRingOperator8)
        bpy.utils.register_class(AddPrintableRingOperator9)
        bpy.utils.register_class(AddPrintableRingOperator10)
        bpy.utils.register_class(AddPrintableRingOperator11)
        bpy.utils.register_class(AddPrintableRingOperator12)
        bpy.utils.register_class(AddPrintableRingOperator13)
        bpy.utils.register_class(AddPrintableRingOperator14)
        bpy.utils.register_class(AddPrintableRingOperator15)
        bpy.utils.register_class(AddPrintableRingOperator16)
        bpy.utils.register_class(AddPrintableRingOperator17)
        bpy.utils.register_class(AddPrintableRingOperator18)
        bpy.utils.register_class(AddPrintableRingOperator19)
        bpy.utils.register_class(AddPrintableRingOperator20)
        bpy.utils.register_class(AddPrintableRingOperator21)
        bpy.utils.register_class(AddPrintableRingOperator22)
        bpy.utils.register_class(AddPrintableRingOperator23)
        bpy.utils.register_class(AddPrintableRingOperator24)
        bpy.utils.register_class(AddPrintableRingOperator25)
        bpy.utils.register_class(AddPrintableRingOperator26)
        bpy.utils.register_class(AddPrintableRingOperator27)
        bpy.utils.register_class(AddPrintableRingOperator28)
        bpy.utils.register_class(AddPrintableRingOperator29)
        bpy.utils.register_class(AddPrintableRingOperator30)
        bpy.utils.register_class(AddPrintableRingOperator31)
        bpy.utils.register_class(AddPrintableRingOperator32)
        bpy.utils.register_class(AddPrintableRingOperator33)
        bpy.utils.register_class(AddPrintableRingOperator34)
        bpy.utils.register_class(AddPrintableRingOperator35)
        bpy.utils.register_class(AddPrintableRingOperator36)
        bpy.utils.register_class(AddPrintableRingOperator37)
        bpy.utils.register_class(AddPrintableRingOperator38)
        bpy.utils.register_class(AddPrintableRingOperator39)
        bpy.utils.register_class(AddPrintableRingOperator40)
        bpy.utils.register_class(AddPrintableRingOperator41)
        bpy.utils.register_class(AddPrintableRingOperator42)
        bpy.utils.register_class(AddPrintableRingOperator43)
        bpy.utils.register_class(AddPrintableRingOperator44)
        bpy.utils.register_class(AddPrintableRingOperator45)
        bpy.utils.register_class(AddPrintableRingOperator46)
        bpy.utils.register_class(AddPrintableRingOperator47)
        bpy.utils.register_class(AddPrintableRingOperator48)
        bpy.utils.register_class(AddPrintableRingOperator49)
        bpy.utils.register_class(AddPrintableRingOperator50)
        bpy.utils.register_class(AddPrintableRingOperator51)
        bpy.utils.register_class(AddPrintableRingOperator52)
        bpy.utils.register_class(AddPrintableRingOperator53)
        bpy.utils.register_class(AddPrintableRingOperator54)
        bpy.utils.register_class(AddPrintableRingOperator55)
        bpy.utils.register_class(AddPrintableRingOperator56)
        bpy.utils.register_class(AddPrintableRingOperator57)
        bpy.utils.register_class(AddPrintableRingOperator58)
        bpy.utils.register_class(AddPrintableRingOperator59)
        bpy.utils.register_class(AddPrintableRingOperator60)
        bpy.utils.register_class(AddPrintableRingOperator61)
        bpy.utils.register_class(AddPrintableRingOperator62)
        bpy.utils.register_class(AddPrintableRingOperator63)
        bpy.utils.register_class(AddPrintableRingOperator64)
        bpy.utils.register_class(AddPrintableRingOperator65)
        bpy.utils.register_class(AddPrintableRingOperator66)
        bpy.utils.register_class(AddPrintableRingOperator67)
        bpy.utils.register_class(AddPrintableRingOperator68)
        bpy.utils.register_class(AddPrintableRingOperator69)
        bpy.utils.register_class(AddPrintableRingOperator70)
        bpy.utils.register_class(AddPrintableRingOperator71)
        bpy.utils.register_class(AddPrintableRingOperator72)
        bpy.utils.register_class(AddPrintableRingOperator73)
        bpy.utils.register_class(AddPrintableRingOperator74)
        bpy.utils.register_class(AddPrintableRingOperator75)
        bpy.utils.register_class(AddPrintableRingOperator76)
        bpy.utils.register_class(AddPrintableRingOperator77)
        bpy.utils.register_class(AddPrintableRingOperator78)
        bpy.utils.register_class(AddPrintableRingOperator79)
        bpy.utils.register_class(AddPrintableRingPanel)
        bpy.utils.register_class(AddPrintableRingMenu)
    
        

def unregister():
    bpy.utils.unregister_class(AddPrintableRingOperator0)
    bpy.utils.unregister_class(AddPrintableRingOperator0)
    bpy.utils.unregister_class(AddPrintableRingOperator1)
    bpy.utils.unregister_class(AddPrintableRingOperator2)
    bpy.utils.unregister_class(AddPrintableRingOperator3)
    bpy.utils.unregister_class(AddPrintableRingOperator4)
    bpy.utils.unregister_class(AddPrintableRingOperator5)
    bpy.utils.unregister_class(AddPrintableRingOperator6)
    bpy.utils.unregister_class(AddPrintableRingOperator7)
    bpy.utils.unregister_class(AddPrintableRingOperator8)
    bpy.utils.unregister_class(AddPrintableRingOperator9)
    bpy.utils.unregister_class(AddPrintableRingOperator10)
    bpy.utils.unregister_class(AddPrintableRingOperator11)
    bpy.utils.unregister_class(AddPrintableRingOperator12)
    bpy.utils.unregister_class(AddPrintableRingOperator13)
    bpy.utils.unregister_class(AddPrintableRingOperator14)
    bpy.utils.unregister_class(AddPrintableRingOperator15)
    bpy.utils.unregister_class(AddPrintableRingOperator16)
    bpy.utils.unregister_class(AddPrintableRingOperator17)
    bpy.utils.unregister_class(AddPrintableRingOperator18)
    bpy.utils.unregister_class(AddPrintableRingOperator19)
    bpy.utils.unregister_class(AddPrintableRingOperator20)
    bpy.utils.unregister_class(AddPrintableRingOperator21)
    bpy.utils.unregister_class(AddPrintableRingOperator22)
    bpy.utils.unregister_class(AddPrintableRingOperator23)
    bpy.utils.unregister_class(AddPrintableRingOperator24)
    bpy.utils.unregister_class(AddPrintableRingOperator25)
    bpy.utils.unregister_class(AddPrintableRingOperator26)
    bpy.utils.unregister_class(AddPrintableRingOperator27)
    bpy.utils.unregister_class(AddPrintableRingOperator28)
    bpy.utils.unregister_class(AddPrintableRingOperator29)
    bpy.utils.unregister_class(AddPrintableRingOperator30)
    bpy.utils.unregister_class(AddPrintableRingOperator31)
    bpy.utils.unregister_class(AddPrintableRingOperator32)
    bpy.utils.unregister_class(AddPrintableRingOperator33)
    bpy.utils.unregister_class(AddPrintableRingOperator34)
    bpy.utils.unregister_class(AddPrintableRingOperator35)
    bpy.utils.unregister_class(AddPrintableRingOperator36)
    bpy.utils.unregister_class(AddPrintableRingOperator37)
    bpy.utils.unregister_class(AddPrintableRingOperator38)
    bpy.utils.unregister_class(AddPrintableRingOperator39)
    bpy.utils.unregister_class(AddPrintableRingOperator40)
    bpy.utils.unregister_class(AddPrintableRingOperator41)
    bpy.utils.unregister_class(AddPrintableRingOperator42)
    bpy.utils.unregister_class(AddPrintableRingOperator43)
    bpy.utils.unregister_class(AddPrintableRingOperator44)
    bpy.utils.unregister_class(AddPrintableRingOperator45)
    bpy.utils.unregister_class(AddPrintableRingOperator46)
    bpy.utils.unregister_class(AddPrintableRingOperator47)
    bpy.utils.unregister_class(AddPrintableRingOperator48)
    bpy.utils.unregister_class(AddPrintableRingOperator49)
    bpy.utils.unregister_class(AddPrintableRingOperator50)
    bpy.utils.unregister_class(AddPrintableRingOperator51)
    bpy.utils.unregister_class(AddPrintableRingOperator52)
    bpy.utils.unregister_class(AddPrintableRingOperator53)
    bpy.utils.unregister_class(AddPrintableRingOperator54)
    bpy.utils.unregister_class(AddPrintableRingOperator55)
    bpy.utils.unregister_class(AddPrintableRingOperator56)
    bpy.utils.unregister_class(AddPrintableRingOperator57)
    bpy.utils.unregister_class(AddPrintableRingOperator58)
    bpy.utils.unregister_class(AddPrintableRingOperator59)
    bpy.utils.unregister_class(AddPrintableRingOperator60)
    bpy.utils.unregister_class(AddPrintableRingOperator61)
    bpy.utils.unregister_class(AddPrintableRingOperator62)
    bpy.utils.unregister_class(AddPrintableRingOperator63)
    bpy.utils.unregister_class(AddPrintableRingOperator64)
    bpy.utils.unregister_class(AddPrintableRingOperator65)
    bpy.utils.unregister_class(AddPrintableRingOperator66)
    bpy.utils.unregister_class(AddPrintableRingOperator67)
    bpy.utils.unregister_class(AddPrintableRingOperator68)
    bpy.utils.unregister_class(AddPrintableRingOperator69)
    bpy.utils.unregister_class(AddPrintableRingOperator70)
    bpy.utils.unregister_class(AddPrintableRingOperator71)
    bpy.utils.unregister_class(AddPrintableRingOperator72)
    bpy.utils.unregister_class(AddPrintableRingOperator73)
    bpy.utils.unregister_class(AddPrintableRingOperator74)
    bpy.utils.unregister_class(AddPrintableRingOperator75)
    bpy.utils.unregister_class(AddPrintableRingOperator76)
    bpy.utils.unregister_class(AddPrintableRingOperator77)
    bpy.utils.unregister_class(AddPrintableRingOperator78)
    bpy.utils.unregister_class(AddPrintableRingOperator79)
    bpy.utils.unregister_class(AddPrintableRingPanel)
    bpy.utils.unregister_class(AddPrintableRingMenu)
    
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
if __name__ == "__main__":
    register()
