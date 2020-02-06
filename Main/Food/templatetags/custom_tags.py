from django import template

register = template.Library()


@register.filter
def index(self_list, list_index):
	if type(self_list) == list and len(self_list) > list_index:
		return self_list[list_index]
	elif type(self_list) != list:
		return "First argument has to be a list."
	elif len(self_list) <= list_index :
		return "Passed index is higher than list length."



