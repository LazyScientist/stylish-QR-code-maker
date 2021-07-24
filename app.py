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
import os
import barcode
import qrcode
from barcode.writer import ImageWriter
from PIL import Image
from kivymd.uix.dialog import MDDialog

Window.clear()
#Window.clearcolor = (0,0,0,0)
Window.borderless = True
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"  

Builder.load_string('''

#: import random random
#:import wb webbrowser







<xp>:
	color1 : color1
	rename:rename
	#orientation: "vertical"
	textarea : textarea
	MDBackdrop:
		header : False
        header_text : ' '
        title :  "Stylish Bae QR Genrator"  #app.title
        id: backdrop
        padding : [40]
        #close_icon : 'account'
        right_action_items : [['login',lambda x : quit() ],['apple', lambda x : print("Apple button")]]
        
		MDBackdropBackLayer:
			ScreenManager:
				id :backlayer
			    Screen:
			        name: "screen1"
			    
			        ScrollView
			            BoxLayout:
			                size_hint_y: None
			                height: self.minimum_height
			                padding: 20
			                spacing: 20
			                orientation: "vertical"
			                #MDIconButton:
			                    #icon: "theater"
			                    #on_press: root.show_theme_picker()	
							MDFillRoundFlatButton:
								text: "Change Theme"
								size_hint_x:1
								md_bg_color: [1, 0, 0, 1]
								on_press: root.show_theme_picker()
							MDFillRoundFlatButton:
								text: "Buy ADS Free"
								size_hint_x:1
								md_bg_color: [1, 0, 0, 1]
								on_release : backlayer.current = "screen2"
							MDFillRoundFlatButton:
								text: "About Us"
								size_hint_x:1
								md_bg_color: [1, 0, 0, 1]
								on_release : backlayer.current = "screen3"
							Label:
								text: "Image save as"
								size_hint_y:None
								height:30
							MDTextFieldRound:
								id: rename
								md_bg_color: [1, 0, 0, 1]
								#icon_left: "email"
								size_hint_x :0.9
								pos_hint: {"center_x":0.5, "center_y":0.5}
								hint_text: "image name"
								text:"name_"+str(random.randint(1,100000))+".png"
							
			                                
			    Screen:
			        name: "screen2"
			        MDCard:
			        	orientation: "vertical"
			        	size_hint: 0.8,0.8
			        	border_radius: 50
			        	elevation: 10
						radius: [50]
			        	pos_hint: {"center_x":0.5, "center_y":0.5}
				        BoxLayout:
				        	size_hint_y:0.1
							Label:
								text: "ADS Free"
								font_name: "DancingScript-Regular.ttf"
								font_size:100
								color:  app.theme_cls.primary_color
						BoxLayout:
							padding: 40
							size_hint_y:0.4
							orientation: "vertical"
							Label:
								text_size:  self.size
								font_name: "DancingScript-Regular.ttf"
								text: "I am A.I assistant based tool, which is made by [b]pankaj jangir[/b] to maximize your prod"
						AnchorLayout:
							size_hint_y: None
							height: 100
							MDIconButton:
								#text: "Buy"
								#pos_hint: {"center_x":0.5, "center_y":0.5}
			
			                            
			    Screen:
			        name: "screen3"        
			        MDCard:
			        	orientation: "vertical"
			        	size_hint: 0.8,0.8
			        	elevation: 10
			        	border_radius: 50
						radius: [50]
			        	pos_hint: {"center_x":0.5, "center_y":0.5}
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
					
			           			
			                     
			    Screen:
			        name: "screen4"
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
							size_hint_y:0.2
							padding: 50
							Button:
								text:"set line color"
								on_press: self.background_color = color1.color
								on_press: root.line_fun(color1)
		
							Button:
								text:"background line color"
								on_press: self.background_color = color1.color
								on_press: root.back_fun(color1)
		
	                
                                
    
                                                
                                                                                            

  
      
          
              
                  
                      

                          
                                                    

                                                                                                        
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                      
                                      
		MDBackdropFrontLayer:	
			orientation: "vertical"
			MDBoxLayout:
				size_hint_y: 0.05
				pos_hint: {"center_x":0.5, "center_y": 0.5} 
				MDIconButton:
					on_release : backlayer.current = "screen1"
				MDIconButton:
					icon: "format-paint"
					on_release : backlayer.current = "screen4"
				MDIconButton:
					
					on_release : backlayer.current = "screen1"
				MDIconButton:
					icon:"content-save"
					on_press:on_press: root.make_qr(bar_input.text,image11,bar_img,save=True)

				
				
			BoxLayout:
				padding: 0
				size_hint_y: 0.1
				ScreenManager:
					id: ll
					Screen:
						name: "ll1"
						Label:
							text: "QR Code"
							pos_hint_x: 0.5
							font_name: "DancingScript-Regular.ttf" 
							font_size:100
							color:  app.theme_cls.primary_color
					Screen:
						name: "ll2"
						Label:
							text: "Wifi Card"
							pos_hint_x: 0.5
							font_name: "DancingScript-Regular.ttf" 
							font_size:100
							color:  app.theme_cls.primary_color
					Screen:
						name: "ll3"
						Label:
							text: "Event Card"
							pos_hint_x: 0.5
							font_name: "DancingScript-Regular.ttf" 
							font_size:100
							color:  app.theme_cls.primary_color
					Screen:
						name: "ll4"
						Label:
							text: "Visiting Card"
							pos_hint_x: 0.5
							font_name: "DancingScript-Regular.ttf" 
							font_size:100
							color:  app.theme_cls.primary_color
					Screen:
						name: "ll5"
						Label:
							text: "Bar Code"
							pos_hint_x: 0.5
							font_name: "DancingScript-Regular.ttf" 
							font_size:100
							color:  app.theme_cls.primary_color
							
				
			BoxLayout:
				size_hint_y: 0.05
				ScrollView:
					size_hint: 1,1
					BoxLayout:
						size_hint_x:3
						MDRectangleFlatIconButton:
							text: "QR code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_release : sm.current = "screen1"
							on_release : ll.current = "ll1"
							on_release : dd.current = "dd1"
						MDRectangleFlatIconButton:
							text: "Wifi code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_release : sm.current = "screen2"
							on_release : ll.current = "ll2"
							on_release : dd.current = "dd1"
						MDRectangleFlatIconButton:
							text: "Event code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_release : sm.current = "screen3"
							on_release : ll.current = "ll3"
							on_release : dd.current = "dd1"
						MDRectangleFlatIconButton:
							text: "Visiting code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_release : sm.current = "screen4"
							on_release : ll.current = "ll4"
							on_release : dd.current = "dd1"
						MDRectangleFlatIconButton:
							text: "Normal QR code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
						MDRectangleFlatIconButton:
							text: "Gif code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
						MDRectangleFlatIconButton:
							text: "Contact code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
						MDRectangleFlatIconButton:
							text: "Link QR code"
							icon: "qrcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_press: root.textfun(self)
						
						MDRectangleFlatIconButton:
							text: "Bar code"
							icon: "barcode"
							text_color:app.theme_cls.primary_color
							line_color: app.theme_cls.primary_color
							icon_color:app.theme_cls.primary_color
							on_release : sm.current = "screen5"
							on_release : ll.current = "ll5"
							on_release : dd.current = "dd2"
					
					
			BoxLayout:
				size_hint_y: 0.15
				orientation: "vertical"	
				BoxLayout:
					MDTextField:
						id: bar_name
						text: "barcode.jpg"
						#hint_text: "Name"
						line_color_focus: 0,5,2,1
						line_color_normal: 0,2,5,0
						helper_text : "Enter name"
						helper_text_mode : "on_focus"
			
				ScreenManager:
					id: dd	
					Screen:
						name: "dd1"
						BoxLayout:	
							orientation: "vertical"
							BoxLayout:
								Button:
									text: "Change_color"
									background_color: color1.color
									on_release : backlayer.current = "screen4"
								
								MDTextField:
								MDTextField:
								MDTextField:
									id: bar_img
									text: "1.png"
									helper_text: "Image"
									helper_text_mode : "persistent"
									line_color_focus: 0,5,2,1
									line_color_normal: 0,2,5,1
					Screen:
						name: "dd2"
					
				
				
			BoxLayout:
				size_hint_y: 0.7
				orientation: "vertical"
				id: textarea
				ScreenManager:
					id: sm
					
					Screen:
						name: "screen1"
						ScrollView:
							bar_width : 0
							size_hint: 1,1
							BoxLayout:
								orientation: "vertical"
								size_hint: 1,1.1
								TextInput:
									id: bar_input
									padding: "4dp"
									font_size:"20dp"
									size_hint_y: 0.4
									hint_text: "enter contet here"
									allow_copy: True
									auto_indent:True
									background_color: 2,5,8,0.1
								MDIconButton:
									icon: "qrcode"
									on_press: rename.text= "name_"+str(random.randint(1,100000))+".png"
									on_press: root.make_qr(bar_input.text,image11,bar_img,save=False)
								Image:
									id: image11
								
							
									
				
					Screen:
						name: "screen2"
						ScrollView:
							bar_width : 0
							size_hint: 1,1
							BoxLayout:
								orientation: "vertical"
								size_hint: 1,1.2
								MDTextField:
									id: bar11
									hint_text: "Serial id"
									#line_color_focus: 0,5,2,1
									line_color_normal: 0,2,5,0
								MDTextField:
									id: bar12
									hint_text: "Password"
									#line_color_focus: 0,5,2,1
									line_color_normal: 0,2,5,0
								MDTextField:
									id: bar13
									hint_text: "Type"
									#line_color_focus: 0,5,2,1
									line_color_normal: 0,2,5,0
								MDIconButton:
									icon: "qrcode"
									on_press: root.make_qr(bar11.text+bar12.text+bar13.text ,image22,bar_img)
								Image:
									id: image22
				
#		
#						
#					Screen:
#						name: "screen3"
#						ScrollView:
#							bar_width : 0
#							size_hint: 1,1
#							BoxLayout:
#								orientation: "vertical"
#								size_hint: 1,1.5
#								MDTextField:
#									id: bar21
#									hint_text: "Location"
#									#line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar22
#									hint_text: "Summary"
#									#line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar23
#									hint_text: "Start date"
#									#line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar24
#									hint_text: "End date"
#									#line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar25
#									hint_text: "URL"
#									#line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDIconButton:
#									icon: "qrcode"
#									on_press: root.make_qr(bar21.text+bar22.text+bar23.text+bar24.text+bar25.text ,image33,bar_img)
#								Image:
#									id: image33
#				
#							
#					Screen:
#						name: "screen4"
#						ScrollView:
#							bar_width : 0
#							size_hint: 1,1
#							BoxLayout:
#								orientation: "vertical"
#								size_hint: 1,1.7
#								MDTextField:
#									id: bar31
#									hint_text: "Name"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar32
#									hint_text: "Full Name"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar33
#									hint_text: "Company"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar34
#									hint_text: "Title"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar35
#									hint_text: "Telephone"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar36
#									hint_text: "Email"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar36
#									hint_text: "Address"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar36
#									hint_text: "URL"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDTextField:
#									id: bar36
#									hint_text: "Note"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#								MDIconButton:
#									icon: "qrcode"
#									on_press: root.make_qr(bar31.text+bar32.text+bar33.text + bar34.text+bar35.text+bar36.text  ,image44,bar_img)
#								Image:
#									id: image44
#				
#					
#					Screen:
#						name: "screen5"
#						ScrollView:
#							bar_width : 0
#							size_hint: 1,1
#							BoxLayout:
#								orientation: "vertical"
#								size_hint: 1,1.1	
#								MDTextField:
#									id: bar_text
#									hint_text: "Bar code"
#									line_color_focus: 0,5,2,1
#									line_color_normal: 0,2,5,0
#									helper_text : "Enter number only"
#									helper_text_mode : "on_focus"
#								MDIconButton:
#									icon: "barcode"
#									on_press: root.bar_fun(bar_text,bar_image)
#								BoxLayout:
#									size_hint_y: 0.3
#									Image:
#										id: bar_image
				
								
								
				
''')
	



class xp(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		textarea = ObjectProperty(None)
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
	
	def  textfun(self,btn):
		if btn.text == "Link QR code":
			t1 = MDTextField(hint_text= "URL",line_color_focus=(0,5,2,1),line_color_normal=(0,2,5,0))
			self.textarea.add_widget(t1)
			
			
			
		
	def color_fun(self,btn):
		dialog = MDDialog(size_hint=(0.8,0.5))
		dialog.add_widget(color_pick())
		dialog.open()
		btn.background_color = color_pick().get()
	

	def bar_fun(self,bar_text,bar_image):
		bb = barcode.get_barcode_class("Code39")
		bb =  bb(bar_text.text, writer = ImageWriter())
		bb.save(self.rename.text)
		bar_image.source = self.rename.text
		try:
			os.remove(self.rename.text)
		except:
			pass

	def  make_qr(self,text,image,bar_img,save):
		logo = Image.open(bar_img.text)
		logo = logo.resize((60, 60), Image.ANTIALIAS)
		qr_big = qrcode.QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)
		qr_big.add_data(text)
		qr_big.make()
		img_qr_big = qr_big.make_image(fill_color= self.line_color, back_color= self.back_color).convert("RGB")
		pos= ((img_qr_big.size[0] - logo.size[0])  // 2 , (img_qr_big.size[1] - logo.size[1])  // 2)
		img_qr_big.paste(logo,pos)
		img_qr_big.save(self.rename.text)
		image.source = self.rename.text
		if save :
			pass
		else:
			try:
				os.remove(self.rename.text)
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











