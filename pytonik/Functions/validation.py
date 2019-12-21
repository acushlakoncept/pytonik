import re

class validation:

	def __getattr__(self, item):
		return item

	def __init__(self, var_string, **kwargs):
		self.varstring = var_string
		self.msg_error = ""
		self.msg_success = ""

	
	def length(self, min='', max=''):
		len_count = len(self.varstring)
		if min is not '' and max is not '':
			if int(min) >= len_count and int(min) <= len_count:
				return True
			else:
				return False
		if min is not '':
			if len_count >= int(min):
				return True
			else:
				return False


	def count(self):
		return len(self.varstring)


	def email(self):
		regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

		if re.search(regex, self.varstring) is False:
			self.msg_error = "Invalid email Address"
		else:
			self.msg_success = "Valid email Address"

		return re.search(regex, self.varstring)
	
	def url(self):
		regex = re.compile(
			r'^(?:http|ftp)s?://'  # http:// or https://
			r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
			r'localhost|'  # localhost...
			r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
			r'(?::\d+)?'  # optional port
			r'(?:/?|[/?]\S+)$', re.IGNORECASE)

		if regex.match(self.varstring) is False:
			self.msg_error = "Invalid URL link"
		else:
			self.msg_success = "Valid URL link"

		return re.match(regex, self.varstring)

	
	def ip(self):
		regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(

		            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(

		            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(

		            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
		if re.match(regex, self.varstring) is False:
			self.msg_error = "invalid IP address"
		else:
			self.msg_success = "Valid IP address"
		return regex.match(self.varstring)

		return re.search(regex, self.varstring)
		
	def single(self):
		regex = re.compile(r'^[a-zA-Z]+[a-zA-Z]+$',

						   re.IGNORECASE)
		if regex.search(self.varstring) is False:
			self.msg_error = "Invalid string"
		else:
			self.msg_success = "Valid String"

		return regex.search(self.varstring)


	
	def phone(self):
		regex = re.compile(r'([+]?\d{1,4}[.\-\s]?)?(\d{3}[.-]?){2}\d{4}$')
		if regex.match(self.varstring) is False:
			self.msg_error = "Invalid Phone Number"
		else:
			self.msg_success = "Valid"
		return regex.match(self.varstring)




	def number(self):
		regex = re.compile(r'(\d+)')

		if regex.match(self.varstring) is False:
			self.msg_error = "Invalid Number"
		else:
			self.msg_success = "Valid Number"
		return regex.search(self.varstring)




	def fullname(self):
		regex = re.compile(r'(^[a-zA-Z\- ]+)$', re.IGNORECASE)
		if regex.search(self.varstring) is False:
			self.msg_error = "Invalid Full name"
		else:
			self.msg_success = "Valid Full name"
		return regex.search(self.varstring)




	def trim(self):
		regex = re.sub('<[^<]+?>', '', self.varstring)
		return regex




	def error(self, m_string, bool = False):
		msg = {
			'msg': str(m_string),
			'bool': bool(bool),
		}
		return msg.get(msg, self.msg_error)


	
	def success(self, m_string, bool = True):
		msg = {
			'msg': str(m_string),
			'bool': bool(bool),
		}
		return msg.get(msg, self.msg_success)
