def getnew(paragraph,substring_to_be_replaced,replace_word):
	for i in range(len(paragraph)):
		new_para=paragraph.replace(substring_to_be_replaced,replace_word )
	return f"{new_para}"
