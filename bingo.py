import ui, random, dialogs

words = ['Mary', 'Joseph', 'Jesus', 'Frosty', 'Manger', 'Presents', 'Snow', 'Chimney', 'Fireplace', 'Star', 'Garland', 'Ornaments', 'Tinsel', 'Mistletoe', 'Church', 'Carols', 'Santa', 'Candy Cane', 'Sledding', 'Elf', 'North Pole', 'Rudolph', 'Hot Cocoa', 'Wise Men', 'Nativity', 'Bethlehem', 'Stockings', 'Gingerbread', 'Egg Nog', 'Lights', 'Donkey', 'Wreath', 'Nice List', 'Sprinkles', 'Cookies', 'Noel', 'Angel', 'Mittens', 'Silver Bells', 'Holly', 'Gift Wrap', 'Grinch', 'Drummer Boy', 'Icicles', 'Marshmallows', 'Nutcracker', 'Frankincense', 'Silent Night', 'Chestnuts']

def draw_button(sender):
	view = sender.superview['textview']
	if len(words) == 0:
		view.text += 'All words have been drawn!\n'
		scroll(sender)
	else:
		drawn = random.choice(words)
		words.remove(drawn)
		view.text += drawn + '\n'
		scroll(sender)
	
def clear_card(sender):
	global words
	words = ['Mary', 'Joseph', 'Jesus', 'Frosty', 'Manger', 'Presents', 'Snow', 'Chimney', 'Fireplace', 'Star', 'Garland', 'Ornaments', 'Tinsel', 'Mistletoe', 'Church', 'Carols', 'Santa', 'Candy Cane', 'Sledding', 'Elf', 'North Pole', 'Rudolph', 'Hot Cocoa', 'Wise Men', 'Nativity', 'Bethlehem', 'Stockings', 'Gingerbread', 'Egg Nog', 'Lights', 'Donkey', 'Wreath', 'Nice List', 'Sprinkles', 'Cookies', 'Noel', 'Angel', 'Mittens', 'Silver Bells', 'Holly', 'Gift Wrap', 'Grinch', 'Drummer Boy', 'Icicles', 'Marshmallows', 'Nutcracker', 'Frankincense', 'Silent Night', 'Chestnuts']
	random.shuffle(words)
	view = sender.superview['textview']
	view.text = ''
	view.text += 'New Round: Clear your boards!\n'
	view.text += '----------\n'
	scroll(sender)
	
def show_bingo_menu(sender):
	modal = dialogs.alert('Clear your boards?', '', 'Yes')
	if modal == 1:
		clear_card(sender)
	
def scroll(sender):
	view = sender.superview['textview']
	view.content_offset = (0, view.content_size[1] - view.height)
	
	
v = ui.load_view()
v['imageview1'].image = ui.Image.named('lights.PNG')
v['imageview2'].image = ui.Image.named('lights.PNG')

v.present('sheet')
