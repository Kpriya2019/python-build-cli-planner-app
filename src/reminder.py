class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteRemainder(PrefixedReminder):


	def __init__(self,text):
		super().__init__(self,prefix="please")
		self.prefix =  prefix
		