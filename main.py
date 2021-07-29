from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout  import BoxLayout
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivymd.uix.chip import MDChip
from kivymd.toast import toast
from kivymd.uix.picker import MDThemePicker
from plyer import vibrator,notification, storagepath, uniqueid 
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager
import random
from MyQR import myqr
import os
import barcode
import qrcode
from barcode.writer import ImageWriter
from PIL import Image
from kivymd.uix.dialog import MDDialog


from kivy.clock import Clock
Clock.max_iteration = 200




Window.clear()
#Window.clearcolor = (0,0,0,0)
Window.borderless = True
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"  

Builder.load_string('''

#: import random random
#:import wb webbrowser







<xp>:
	#color1 : color1
	rename:rename
	#textarea : textarea
	MDBackdrop:
		
		header : False
        header_text : 'hii '
        title :  "Stylish Bar Code Genrator"  #app.title
        id: backdrop
        padding : [40]
        #close_icon : 'account'
        #right_action_items : [['login',lambda x : quit() ],['apple', lambda x : print("Apple button")]]
        
		MDBackdropBackLayer:
			ScreenManager:
				id :backlayer
			    Screen:
			        name: "screen1"
			    
			        ScrollView
			            BoxLayout:
			                size_hint_y: None
			                height:    1200#self.minimum_height
			                padding: 20
			                spacing: 30
			                orientation: "vertical"
			                #MDIconButton:
			                    #icon: "theater"
			                    #on_press: root.show_theme_picker()	
							MDFillRoundFlatButton:
								text: "Change Theme"
								size_hint_x:1
								md_bg_color: app.theme_cls.accent_color
								on_press: root.show_theme_picker()
							MDFillRoundFlatButton:
								text: "Buy ADS Free"
								size_hint_x:1
								md_bg_color: app.theme_cls.accent_color
								on_release : backlayer.current = "screen2"
							MDFillRoundFlatButton:
								text: "About Us"
								size_hint_x:1
								md_bg_color: app.theme_cls.accent_color
								on_release : backlayer.current = "screen3"
							Label:
								text: "Image save as"
								size_hint_y:None
								height:30
							MDTextFieldRound:
								id: rename
								md_bg_color: app.theme_cls.accent_color
								#icon_left: "email"
								size_hint_x :0.9
								pos_hint: {"center_x":0.5, "center_y":0.5}
								size_hint_y:None
								height: 40
								hint_text: "image name"
								text:"name_"+str(random.randint(1,100000))+".png"
							
							MDCard:
								orientation: "vertical"
					        	size_hint: 0.9,0.9
					        	elevation: 10
					        	border_radius: 50
								radius: [50]
					        	pos_hint: {"center_x":0.5, "center_y":0.5}
					        	md_bg_color: app.theme_cls.accent_color
					        	Label:
					        		size_hint_y:0.2
					        		text: "Buy add free version"
					        	MDLabel:
					        		text:"We don't show ads offline , so, don't buy if you are offline user"
					        	Image:
					        		source:"1.png"
					        	MDRectangleFlatIconButton:
									icon:"square-inc-cash"
					        		text:"Buy now"
					        		#size_hint:0.6,0.6
					        		pos_hint: {"center_x":0.5, "center_y":0.5}
					        	
							MDCard:								
					        	size_hint: 0.9,0.9
					        	elevation: 10
					        	border_radius: 50
								radius: [50]
					        	pos_hint: {"center_x":0.5, "center_y":0.5}
					        	md_bg_color: app.theme_cls.accent_color
					        	MDLabel:
					        		#size_hint_y:0.2
					        		#adaptive_size: True
					        		halign: 'center'
					        		text: "You can Download This Same Software for other Operating System in just one click"
					        	ScrollView:
					        		size_hint_x:None
					        		width:"150dp"
					        		BoxLayout:
					        			size_hint_y: None
					        			height: "300dp"
					        			bar_size : 0
					        			orientation: "vertical"
							        	MDRectangleFlatIconButton:
											icon:"android"
							        		text:"Android"
							        	MDRectangleFlatIconButton:
											icon:"apple"
							        		text:"iphone"
							        	MDRectangleFlatIconButton:
											icon:"apple"
							        		text:"imac"
							        	MDRectangleFlatIconButton:
											icon:"raspberry-pi"
							        		text:"Raspberry"
							        	MDRectangleFlatIconButton:
											icon:"windows"
							        		text:"Windows 32-bit"
							        	MDRectangleFlatIconButton:
											icon:"windows"
							        		text:"Windows 64-bit"
							        	MDRectangleFlatIconButton:
											icon:"linux"
							        		text:"Linux 32-bit"
							        	MDRectangleFlatIconButton:
											icon:"linux"
							        		text:"Linux 64-bit"
							        				
					        		
					        	
							
							
			                                
			    Screen:
			        name: "screen2"
			        MDCard:
						orientation: "vertical"
			        	size_hint: 0.8,0.8
			        	elevation: 10
			        	border_radius: 50
						radius: [50]
			        	pos_hint: {"center_x":0.5, "center_y":0.5}
						md_bg_color: color1.color
						BoxLayout:
							size_hint_y:0.1
							Label:
								text:"Choose Color"
						ColorPicker:
							id: color1
						BoxLayout:
							size_hint_y:None
							height: bbb.height
							padding: 50
							MDFillRoundFlatButton:
								id: bbb
								text:"set line color"
								on_press: self.md_bg_color=color1.color
								on_press: root.line_fun(color1)
								size_hint_x:1
							MDFillRoundFlatButton:
								text:"set background color"
								on_press: self.md_bg_color=color1.color
								on_press: root.back_fun(color1)
								size_hint_x:1
							
			
			                            
			    Screen:
			        name: "screen3"        
			        MDCard:
			        	orientation: "vertical"
			        	size_hint: 0.8,0.8
			        	elevation: 10
			        	border_radius: 50
						radius: [50]
						md_bg_color: app.theme_cls.accent_color
			        	pos_hint: {"center_x":0.5, "center_y":0.55}
				        BoxLayout:
				        	size_hint_y:0.1
							Label:
								text: "About Me"
								font_name: "DancingScript-Regular.ttf"
								font_size:100
								color:  app.theme_cls.primary_color		
						BoxLayout:
							size_hint_y: 0.2
							Image:
								source: "image/me.png"
						BoxLayout:
							padding: 40
							size_hint_y:0.4
							orientation: "vertical"
							BoxLayout:
								Label:
									text_size:  self.size
									markup : True
									font_name: "DancingScript-Regular.ttf"
									text: "I am A.I assistant based tool, which is made by [b]pankaj jangir[/b] to maximize your prodactivity and save time .   I can help you in programming , content writing , achiving daily goals , fitness and I can work as a keybord  to speed up typing, spacially in touch devices by using tools like file explorer, color picker, and many more"
							
							BoxLayout:
								size_hint_y: 0.2
								MDIconButton:
									icon: "github-box"
									on_release: wb.open("https://github.com/pankaj-jangid")
								MDIconButton:
									icon: "linkedin-box"
									on_release: wb.open("https://www.linkedin.com/in/pankaj-jangir-590a661a8")
								MDIconButton:
									icon: "youtube"
									on_release: wb.open("https://youtube.com/channel/UCATl9ths1GPSrxyD3RVn9GQ")
								MDIconButton:
									icon: "facebook"
									on_release: wb.open("https://www.facebook.com/scanta.calous.1")
								MDIconButton:
									icon: "instagram"
									on_release: wb.open("https://www.instagram.com/lazy__scientist/")
					
			           	                               
	                  
                      

                          
                                                    

                                                                                                        
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                      
		MDBackdropFrontLayer:	
			orientation: "vertical"
			AnchorLayout:
				anchor_x: "right"
				size_hint_y: 0
				BoxLayout:
					size_hint_x: None
					width: 300
					spacing: 10
					MDIconButton:
						icon:"xbox-controller-menu"
						#md_bg_color: app.theme_cls.accent_color
						
						on_release : backlayer.current = "screen1"
					MDIconButton:
						icon: "format-color-fill"
						#md_bg_color: app.theme_cls.accent_color
						on_release : backlayer.current = "screen2"
						
					Button:
						id: bar_img
						text:"image/21.gif"
						font_size:0
						background_color: app.theme_cls.primary_color
						Image:
					        source: bar_img.text
					        center_x: self.parent.center_x
					        center_y: self.parent.center_y
					 

			BoxLayout:
				size_hint_y: 0.1	
				ScrollView:
					size_hint: 1,1
					BoxLayout:
						size_hint_x:2.5
						MDRectangleFlatIconButton:
							text: "QR code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen1"
						MDRectangleFlatIconButton:
							text: "Wifi code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen2"
						MDRectangleFlatIconButton:
							text: "Event code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen3"
						MDRectangleFlatIconButton:
							text: "Visiting code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen4"
						
						MDRectangleFlatIconButton:
							text: "Contact code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen5"
						MDRectangleFlatIconButton:
							text: "Link QR code"
							icon: "qrcode"
							text_color:app.theme_cls.accent_color
							on_release : sm.current = "screen6"
					
					

								



																																								
							
			BoxLayout:
				size_hint_y:0.6
				orientation: "vertical"
				id: textarea
				ScreenManager:
					id: sm
					
					Screen:
						name: "screen1"
						TextInput:
							id: bar_input
							padding: "4dp"
							font_size:"20dp"
							hint_text: "enter contet here"
							background_color:app.theme_cls.accent_color
						MDFillRoundFlatIconButton:
							icon: "qrcode"
							text: "Genrate"
							pos_hint: {"center_x":0.5, "center_y": 0.1}
							on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
							on_press: root.make_qr(bar_input.text,image11,bar_img,save=False)
							on_press: root.make_qr22(bar_input.text,image22,bar_img,save=False)
							on_press: root.make_qr33(bar_input.text,image33,bar_img,save=False)
							on_press: root.make_qr44(bar_input.text,image44,bar_img,save=False)
							#########
							
							on_press: image11_btn.on_press =  root.make_qr(bar_input.text,image11,bar_img,save=False)
							on_press: image22_btn.on_press =  root.make_qr22(bar_input.text,image22,bar_img,save=False)
							on_press: image33_btn.on_press =  root.make_qr33(bar_input.text,image33,bar_img,save=False)
							on_press: image44_btn.on_press =  root.make_qr44(bar_input.text,image44,bar_img,save=False)
							
						
								
					Screen:
						name: "screen2"
						ScrollView:
							bar_width : 0
							BoxLayout:
								orientation: "vertical"
								size_hint_y: None
								height: "220dp"
								MDTextField:
									id: bar11
									hint_text: "Serial id"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar12
									hint_text: "Password"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar13
									hint_text: "Type"
									#line_color_normal: 0,2,5,0
								MDFillRoundFlatIconButton:
									icon: "qrcode"
									text: "Genrate"
									pos_hint: {"center_x":0.5, "center_y":0.5}
									on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
									on_press: root.make_qr(bar11.text+bar12.text+bar13.text          ,image11,bar_img,save=False)
									on_press: root.make_qr22(bar11.text+bar12.text+bar13.text     ,image22,bar_img,save=False)
									on_press: root.make_qr33(bar11.text+bar12.text+bar13.text     ,image33,bar_img,save=False)
									on_press: root.make_qr44(bar11.text+bar12.text+bar13.text    ,image44,bar_img,save=False)
									
									########
									on_press: image11_btn.on_press =  root.make_qr(bar11.text+bar12.text+bar13.text          ,image11,bar_img,save=False)
									on_press: image22_btn.on_press =  root.make_qr22(bar11.text+bar12.text+bar13.text     ,image22,bar_img,save=False)
									on_press: image33_btn.on_press =  root.make_qr33(bar11.text+bar12.text+bar13.text     ,image33,bar_img,save=False)
									on_press: image44_btn.on_press =  root.make_qr44(bar11.text+bar12.text+bar13.text    ,image44,bar_img,save=False)
									
									
								
		
						
					Screen:
						name: "screen3"
						ScrollView:
							BoxLayout:
								orientation: "vertical"
								size_hint_y: None
								height: "320dp"
								MDTextField:
									id: bar21
									hint_text: "Location"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar22
									hint_text: "Summary"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar23
									hint_text: "Start date"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar24
									hint_text: "End date"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar25
									hint_text: "URL"
									#line_color_normal: 0,2,5,0
								MDFillRoundFlatIconButton:
									icon: "qrcode"
									text: "Genrate"
									pos_hint: {"center_x":0.5, "center_y":0.5}
									on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
									on_press: root.make_qr(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text     ,image11,bar_img,save=False)
									on_press: root.make_qr22(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text   ,image22,bar_img,save=False)
									on_press: root.make_qr33(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text     ,image33,bar_img,save=False)
									on_press: root.make_qr44(bar_input.text,image44,bar_img,save=False)
									#######
									
									on_press: image11_btn.on_press =  root.make_qr(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text     ,image11,bar_img,save=False)
									on_press: image22_btn.on_press = root.make_qr22(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text   ,image22,bar_img,save=False)
									on_press: image33_btn.on_press =  root.make_qr33(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text     ,image33,bar_img,save=False)
									on_press: image44_btn.on_press =  root.make_qr44(bar_input.text,image44,bar_img,save=False)
									
				
							
					Screen:
						name: "screen4"
						ScrollView:
							BoxLayout:
								orientation: "vertical"
								size_hint_y: None
								height: "520dp"
								MDTextField:
									id: bar31
									hint_text: "Name"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar32
									hint_text: "Full Name"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar33
									hint_text: "Company"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar34
									hint_text: "Title"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar35
									hint_text: "Telephone"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar36
									hint_text: "Email"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar36
									hint_text: "Address"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar36
									hint_text: "URL"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar36
									hint_text: "Note"
									#line_color_normal: 0,2,5,0
								MDFillRoundFlatIconButton:
									icon: "qrcode"
									text: "Genrate"
									pos_hint: {"center_x":0.5, "center_y":0.5}
									on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
									on_press: root.make_qr(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text      ,image11,bar_img,save=False)
									on_press: root.make_qr22(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text      ,image22,bar_img,save=False)
									on_press: root.make_qr33(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text        ,image33,bar_img,save=False)
									on_press: root.make_qr44(bar_input.text,image44,bar_img,save=False)
									
									
									####
									on_press: image11_btn.on_press =  root.make_qr(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text      ,image11,bar_img,save=False)
									on_press: image22_btn.on_press =  root.make_qr22(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text      ,image22,bar_img,save=False)
									on_press: image33_btn.on_press =   root.make_qr33(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text        ,image33,bar_img,save=False)
									on_press: image44_btn.on_press =   root.make_qr44(bar_input.text,image44,bar_img,save=False)
									
													
					Screen:
						name: "screen5"
						ScrollView:
							bar_width : 0
							BoxLayout:
								orientation: "vertical"
								size_hint_y: None
								height: "170dp"
								MDTextField:
									id: bar11
									hint_text: "Contact Name"
									#line_color_normal: 0,2,5,0
								MDTextField:
									id: bar12
									hint_text: "Contact Number"
									#line_color_normal: 0,2,5,0
								MDFillRoundFlatIconButton:
									icon: "qrcode"
									text: "Genrate"
									pos_hint: {"center_x":0.5, "center_y":0.5}
									on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
									on_press: root.make_qr(bar_input.text,image11,bar_img,save=False)
									on_press: root.make_qr22(bar_input.text,image22,bar_img,save=False)
									on_press: root.make_qr33(bar_input.text,image33,bar_img,save=False)
									on_press: root.make_qr44(bar_input.text,image44,bar_img,save=False)
									
									######
									on_press: image11_btn.on_press =   root.make_qr(bar_input.text,image11,bar_img,save=False)
									on_press: image22_btn.on_press =   root.make_qr22(bar_input.text,image22,bar_img,save=False)
									on_press: image33_btn.on_press =   root.make_qr33(bar_input.text,image33,bar_img,save=False)
									on_press: image44_btn.on_press =   root.make_qr44(bar_input.text,image44,bar_img,save=False)
									
									
								
						
					Screen:
						name: "screen6"
						TextInput:
							id: link_input
							padding: "4dp"
							font_size:"20dp"
							hint_text: "Paste link  here"
							background_color: app.theme_cls.accent_color
						MDFillRoundFlatIconButton:
							icon: "qrcode"
							text: "Genrate"
							pos_hint: {"center_x":0.5, "center_y":0.1}
							on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
							on_press: root.make_qr(link_input.text,image11,bar_img,save=False)
							#on_press: root.make_qr22(link_input.text,image22,bar_img,save=False)
							#on_press: root.make_qr33(link_input.text,image33,bar_img,save=False)
							on_press: root.make_qr44(bar_input.text,image44,bar_img,save=False)
							
							#######
							
							on_press: image11_btn.on_press =   root.make_qr(link_input.text,image11,bar_img,save=False)
							on_press: image22_btn.on_press =   root.make_qr22(link_input.text,image22,bar_img,save=False)
							on_press: image33_btn.on_press =   root.make_qr33(link_input.text,image33,bar_img,save=False)
							on_press: image44_btn.on_press =   root.make_qr44(bar_input.text,image44,bar_img,save=False)
						
									

																					










																					
							
			BoxLayout:
				size_hint_y:0.4
				orientation: "vertical"

				ScrollView:
					bar_width : 0
					BoxLayout:
						size_hint_x: 2
						spacing:30
						MDCard:
							size_hint: 0.8,0.8
					        elevation: 10
					        border_radius: 50
							radius: [50]
					        pos_hint: {"center_x":0.5, "center_y":0.5}
							md_bg_color: app.theme_cls.primary_color					
							Image:
								id: image11
							RelativeLayout:
								size_hint:0,0
								MDFloatingActionButton:
									id: image11_btn
									icon: "content-save"
									on_press: root.make_qr(bar_input.text,image11,bar_img,save=True)
									pos_hint:{"center_x":-0.5,"center_y":0}
														
						MDCard:
							size_hint: 0.8,0.8
					        elevation: 10
					        border_radius: 50
							radius: [50]
					        pos_hint: {"center_x":0.5, "center_y":0.5}
							md_bg_color: app.theme_cls.primary_color					
							Image:
								id: image22
							RelativeLayout:
								size_hint:0,0
								MDFloatingActionButton:
									id: image22_btn
									icon: "content-save"
									on_press: root.make_qr22(bar_input.text,image22,bar_img,save=True)
									pos_hint:{"center_x":-0.5,"center_y":0}
								
							
						MDCard:
							size_hint: 0.8,0.8
					        elevation: 10
					        border_radius: 50
							radius: [50]
					        pos_hint: {"center_x":0.5, "center_y":0.5}
							md_bg_color: app.theme_cls.primary_color					
							Image:
								id: image33
							RelativeLayout:
								size_hint:0,0
								MDFloatingActionButton:
									id: image33_btn
									icon: "content-save"
									on_press: root.make_qr33(bar_input.text,image33,bar_img,save=True)
									pos_hint:{"center_x":-0.5,"center_y":0}
						
							
								
										
						MDCard:
							size_hint: 0.8,0.8
					        elevation: 10
					        border_radius: 50
							radius: [50]
					        pos_hint: {"center_x":0.5, "center_y":0.5}
							md_bg_color: app.theme_cls.primary_color					
							Image:
								id: image44
							RelativeLayout:
								size_hint:0,0
								MDFloatingActionButton:
									id: image44_btn
									icon: "content-save"
									on_press: root.make_qr44(bar_input.text,image44,bar_img,save=True)
									pos_hint:{"center_x":-0.5,"center_y":0}
							
										
														
	
				
										
				
				
				
				
						
								
								
				
''')
	



class xp(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#textarea = ObjectProperty(None)
		color1 = ObjectProperty(None)
		rename = ObjectProperty(None)
	
	line_color = '#000000'
	def line_fun(self,col):
		self.line_color = col.hex_color
	back_color = '#ffffff'
	def back_fun(self,col):
		self.back_color = col.hex_color
	
	
	def show_theme_picker(self):
		theme_dialog = MDThemePicker()
		theme_dialog.open()
	
	def  textfun(self,btn,textarea):
		textarea.clear_widgets()
		if btn.text == "Wifi code":
			t1 = MDTextField(hint_text= "URL")
			textarea.add_widget(t1)
			
			
			
		
	def color_fun(self,btn):
		dialog = MDDialog(size_hint=(0.8,0.5))
		dialog.add_widget(color_pick())
		dialog.open()
		btn.background_color = color_pick().get()
	

#	def bar_fun(self,bar_text,bar_image):
#		bb = barcode.get_barcode_class("Code39")
#		bb =  bb(bar_text, writer = ImageWriter())
#		bb.save("t"+self.rename.text.replace(".png",""))
#		bar_image.source = "t"+self.rename.text
#		try:
#			os.remove("t"+self.rename.text)
#		except:
#			pass

	def  make_qr(self,text,image,bar_img,save):
		qr_big = qrcode.QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)
		qr_big.add_data(text)
		qr_big.make()
		img_qr_big = qr_big.make_image(fill_color= self.line_color, back_color= self.back_color).convert("RGB")
		img_qr_big.save(self.rename.text+"nn.png")
		image.source = self.rename.text+"nn.png"
		if save :
			pass
		else:
			try:
				pass
				os.remove(self.rename.text+"nn.png")
			except:
				pass
			


	def  make_qr22(self,text,image,bar_img,save):
		logo = Image.open(bar_img.text)
		logo = logo.resize((60, 60), Image.ANTIALIAS)
		qr_big = qrcode.QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)
		qr_big.add_data(text)
		qr_big.make()
		img_qr_big = qr_big.make_image(fill_color= self.line_color, back_color= self.back_color).convert("RGB")
		pos= ((img_qr_big.size[0] - logo.size[0])  // 2 , (img_qr_big.size[1] - logo.size[1])  // 2)
		img_qr_big.paste(logo,pos)
		img_qr_big.save(self.rename.text+".png")
		image.source = self.rename.text+".png"
		if save :
			pass
		else:
			try:
				pass
				os.remove(self.rename.text+".png")
			except:
				pass






	def  make_qr33(self,text,image,bar_img,save):
		version,level,qr_name = myqr.run(words=text,level="H",picture=bar_img.text , colorized=False , save_name=self.rename.text+"bk.gif",  save_dir=os.getcwd())
		image.source = self.rename.text+"bk.gif"
		if save :
			pass
		else:
			try:
				pass
				os.remove(self.rename.text+"bk.gif")
			except:
				pass



	def  make_qr44(self,text,image,bar_img,save):
		version,level,qr_name = myqr.run(words=text,level="H",picture=bar_img.text , colorized=True , save_name=self.rename.text+".gif",  save_dir=os.getcwd())
		image.source = self.rename.text+".gif"
		if save :
			pass
		else:
			try:
				pass
				os.remove(self.rename.text+".gif")
			except:
				pass






						
		
				
				

class MyClockApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        #theme_cls = ThemeManager()
        #self.theme("dark")
        clock = xp()
        return clock

MyClockApp().run()











